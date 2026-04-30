# Fine-tuning SAM2 with HF Trainer
Fine-tune SAM2.1 on a small part of the MicroMat dataset for image matting,
using the Hugging Face Trainer with a custom loss function.

```python
!pip install -q transformers datasets monai trackio
```
## Load and explore the dataset
```python
from datasets import load_dataset

dataset = load_dataset("merve/MicroMat-mini", split="train")
dataset
```
```python
dataset = dataset.train_test_split(test_size=0.1)
train_ds = dataset["train"]
val_ds = dataset["test"]
```
```python
import json

tain_ds[0]
```
```python
json.loads(train_ds["prompt"][0])["bbox"]
```
## Visualize a sample
```python
import matplotlib.pyplot as plt
import numpy as np

def show_mask(mask, ax, bbox):
    color = np.array([0.12, 0.56, 1.0, 0.6])
    mask = np.array(mask)
    h, w = mask.shape
    mask_image = mask.reshape(h, w, 1) * color.reshape(1, 1, 4)
    ax.imshow(mask_image)
    x0, y0, x1, y1 = bbox
    ax.add_patch(
        plt.Rectangle(
            (x0, y0), x1 - x0, y1 - y0, fill=False, edgecolor="lime", linewidth=2
        )
    )

e = train_ds[0]
image = np.array(e["image"])
ground_truth_mask = np.array(e["mask"])

fig, ax = plt.subplots()
ax.imshow(image)
show_mask(ground_truth_mask, ax, json.loads(e["prompt"])["bbox"])
ax.set_title("Ground truth mask")
ax.set_axis_off()
plt.show()
```
## Build the dataset and collator
`SAMDataset` wraps each sample into the format expected by the SAM2 processor.
Ground-truth masks are stored under the key `"labels"` so the Trainer
automatically pops them before calling `model.forward()`.
```python
from torch.utils.data import Dataset
import torch
import torch.nn.functional as F

class SAMDataset(Dataset):
    def __init__(self, dataset, processor):
        self.dataset = dataset
        self.processor = processor
    
    def __len__(self):
        return len(self.dataset)
    
    def __getitem__(self, idx):
        try:
            item = self.dataset[idx]
            image = item["image"]
            prompt = json.loads(item["prompt"])["bbox"]
            inputs = self.processor(image, input_boxes=[[prompt]], return_tensors="pt")
            inputs["labels"] = (np.array(item["mask"]) > 0).astype(np.float32)
            inputs["original_image_size"] = torch.tensor(image.size[::-1])
            return inputs
        except Exception as e:
            print(f"Error occurred while processing item {idx}: {str(e)}")
            return None

def collate_fn(batch):
    batch = [item for item in batch if item is not None]
    if not batch:
        return None
    pixel_values = torch.cat([item["pixel_values"] for item in batch], dim=0)
    original_sizes = torch.stack([item["original_sizes"] for item in batch])
    input_boxes = torch.cat([item["input_boxes"] for item in batch], dim=0)
    labels = torch.cat([
        F.interpolate(
            torch.as_tensor(x["labels"]).unsqueeze(0).unsqueeze(0).float(),
            size=(256, 256),
            mode="nearest",
        )
        for x in batch
    ], dim=0).long()

    return {
        "pixel_values": pixel_values,
        "original_sizes": original_sizes,
        "input_boxes": input_boxes,
        "labels": labels,
        "original_image_size": torch.stack(
            [item["original_image_size"] for item in batch]
        ),
        "multimask_output": False,
    }
```
```python
from transformers import Sam2Processor

processor = Sam2Processor.from_pretrained("facebook/sam2.1-hiera-small")

train_dataset = SAMDataset(dataset=train_ds, processor=processor)
val_dataset = SAMDataset(dataset=val_ds, processor=processor)
```
## Load model and freeze encoder layers
```python
from transformers import Sam2Model

model = Sam2Model.from_pretrained("facebook/sam2.1-hiera-small")

for name, param in model.named_parameters():
    if name.startswith("vision_encoder") or name.startswith("prompt_encoder"):
        param.requires_grad_(False)
```
## Inference before training
```python
item = val_ds[1]
img = item["image"]
bbox = json.loads(item["prompt"])["bbox"]

inputs = processor(images=img, input_boxes=[[bbox]], return_tensors="pt").to(
    model.device
)

with torch.no_grad():
    outputs = model(**inputs)

masks = processor.post_process_masks(outputs.pred_masks.cpu(), inputs["original_sizes"])[0]
preds = masks.squeeze(0)
mask = (preds[0] > 0).cpu().numpy()

overlay = np.asarray(img, dtype=np.uint8).copy()
overlay[mask] = 0.55 * overlay[mask] + 0.45 * np.array([0, 255, 0], dtype=np.float32)

plt.imshow(overlay)
plt.title("Before training")
plt.axis("off")
plt.show()
```
## Define custom loss
SAM2 does not compute loss in its `forward()`, so we provide a
`compute_loss_func` to the Trainer. The Trainer pops `"labels"` from the
batch before calling `model.forward()`, then passes `(outputs, labels)` to
this function.
```python
import monai
from transformers import Trainer, TrainingArguments
import trackio

seg_loss = monai.losses.DiceCELoss(sigmoid=True, squared_pred=True, reduction="mean")

def compute_loss(outputs, labels, num_items_in_batch=None):
    try:
        predicted_masks = outputs.pred_masks.squeeze(1)
        return seg_loss(predicted_masks, labels.float())
    except Exception as e:
        print(f"Error occurred while computing loss: {str(e)}")
        return torch.tensor(0.0)
```
## Train with Trainer
Key settings:
- `remove_unused_columns=False`: the Trainer must keep `input_boxes`,
  `original_sizes`, etc. that are not in the model's `forward()` signature.
- `compute_loss_func`: our custom DiceCE loss.
- `report_to="trackio"`: logs the training loss to trackio.
```python
training_args = TrainingArguments(
    output_dir="sam2-finetuned",
    num_train_epochs=30,
    per_device_train_batch_size=4,
    learning_rate=1e-5,
    weight_decay=0,
    logging_steps=1,
    save_strategy="epoch",
    save_total_limit=2,
    remove_unused_columns=False,
    dataloader_pin_memory=False,
    report_to="trackio",
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    data_collator=collate_fn,
    compute_loss_func=compute_loss,
)

try:
    trainer.train()
except Exception as e:
    print(f"Error occurred during training: {str(e)}")
```
## Inference after training
```python
item = val_ds[1]
img = item["image"]
bbox = json.loads(item["prompt"])["bbox"]

inputs = processor(images=img, input_boxes=[[bbox]], return_tensors="pt").to(
    model.device
)

with torch.no_grad():
    outputs = model(**inputs)

preds = processor.post_process_masks(
    outputs.pred_masks.cpu(), inputs["original_sizes"]
)[0]
preds = preds.squeeze(0)
mask = (preds[0] > 0).cpu().numpy()

overlay = np.asarray(img, dtype=np.uint8).copy()
overlay[mask] = 0.55 * overlay[mask] + 0.45 * np.array([0, 255, 0], dtype=np.float32)

plt.imshow(overlay)
plt.title("After training")
plt.axis("off")
plt.show()
```
## ⚠️ Tratamento de Exceções e Edge Cases
Para garantir a robustez do modelo, é importante tratar exceções e edge cases. Aqui estão algumas considerações:
*   Verificar se o conjunto de dados está vazio antes de tentar carregá-lo.
*   Tratar exceções durante o processamento dos dados, como erros de parsing de JSON.
*   Verificar se as imagens e máscaras estão no formato correto antes de tentar processá-las.
*   Tratar exceções durante o treinamento do modelo, como erros de inicialização ou problemas de convergência.
*   Implementar um mecanismo de retry para lidar com falhas temporárias durante o treinamento ou inferência.

Além disso, é importante considerar edge cases, como:
*   Imagens com tamanho irregular ou formato inválido.
*   Máscaras com valores inválidos ou inconsistentes.
*   Prompt com formato inválido ou informações faltantes.

Ao tratar esses casos, é possível garantir que o modelo seja mais robusto e confiável, mesmo em situações adversas.