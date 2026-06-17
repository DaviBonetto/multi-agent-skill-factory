# Desenvolvimento de Microserviços com Kubernetes
Ensina como projetar, desenvolver e implantar microserviços escaláveis utilizando Kubernetes

## Objetivo
O objetivo deste guia é fornecer uma abordagem prática e técnica para o desenvolvimento de microserviços escaláveis utilizando Kubernetes. Ao final deste guia, você estará capacitado a projetar, desenvolver e implantar microserviços eficientes e escaláveis.

## Pré-requisitos
Para seguir este guia, é necessário ter conhecimento em:
- Desenvolvimento de software
- Conceitos de microserviços
- Noções básicas de containerização com Docker
- Familiaridade com linhas de comando e terminais

## Passo a Passo Técnico / Exemplos de Código
### 1. Configurando o Ambiente
Primeiramente, é necessário configurar o ambiente de desenvolvimento. Isso inclui a instalação do Docker e do Kubernetes. Para instalar o Docker, você pode seguir os passos abaixo:
```bash
# Atualize a lista de pacotes
sudo apt update

# Instale o Docker
sudo apt install docker.io
```
Para o Kubernetes, você pode usar um cluster local como o Minikube:
```bash
# Instale o Minikube
curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.23.0/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

### 2. Desenvolvendo o Microserviço
Desenvolva um microserviço simples em uma linguagem de sua escolha (por exemplo, Python com Flask). O microserviço deve expor uma API REST.
```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/saudacao', methods=['GET'])
def saudacao():
    try:
        return jsonify({'mensagem': 'Olá, mundo!'})
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### 3. Containerizando o Microserviço
Crie um arquivo `Dockerfile` para containerizar o microserviço:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]
```
Construa a imagem Docker:
```bash
docker build -t meu-microservico .
```

### 4. Implantando no Kubernetes
Crie um arquivo de definição de deployment para o Kubernetes:
```yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: meu-microservico
spec:
  replicas: 3
  selector:
    matchLabels:
      app: meu-microservico
  template:
    metadata:
      labels:
        app: meu-microservico
    spec:
      containers:
      - name: meu-microservico
        image: meu-microservico:latest
        ports:
        - containerPort: 5000
```
Aplique a configuração:
```bash
kubectl apply -f deployment.yaml
```

## Validação
Para validar a implantação, você pode usar o comando `kubectl` para verificar o status dos pods:
```bash
kubectl get pods
```
Acesse o microserviço através do serviço exposto pelo Kubernetes:
```bash
kubectl port-forward svc/meu-microservico 5000:5000 &
curl http://localhost:5000/api/saudacao
```
Deve ser retornado: `{"mensagem": "Olá, mundo!"}`. Isso confirma que o microserviço está funcionando corretamente e escalável com o Kubernetes.

## ⚠️ Tratamento de Exceções e Edge Cases
### Tratamento de Erros
No exemplo acima, o tratamento de erros foi implementado no microserviço para retornar uma resposta com um erro 500 em caso de exceção.
```python
try:
    return jsonify({'mensagem': 'Olá, mundo!'})
except Exception as e:
    return jsonify({'erro': str(e)}), 500
```
### Edge Cases
Alguns exemplos de edge cases que devem ser considerados:
- **Conexão perdida**: O que acontece se a conexão com o banco de dados for perdida?
- **Sobrecarga de requisições**: O que acontece se o microserviço receber mais requisições do que pode processar?
- **Falha no container**: O que acontece se o container do microserviço falhar?

Para lidar com esses edge cases, é importante implementar mecanismos de:
- **Retentativa**: Tente novamente a operação em caso de falha.
- **Timeout**: Estabeleça um tempo limite para a operação e retorne um erro se não for concluída dentro desse tempo.
- **Load Balancing**: Distribua as requisições entre múltiplos containers para evitar sobrecarga.
- **Monitoramento**: Monitore o desempenho do microserviço e alerte em caso de problemas.

Exemplo de como implementar retentativa e timeout no microserviço:
```python
import time

def saudacao():
    try:
        # Tente novamente a operação em caso de falha
        for i in range(3):
            try:
                return jsonify({'mensagem': 'Olá, mundo!'})
            except Exception as e:
                time.sleep(1)  # Aguarde 1 segundo antes de tentar novamente
        # Se todas as tentativas falharem, retorne um erro
        return jsonify({'erro': 'Falha ao processar a requisição'}), 500
    except Exception as e:
        # Estabeleça um tempo limite para a operação
        if time.time() - inicio > 10:
            return jsonify({'erro': 'Timeout'}), 500
        return jsonify({'erro': str(e)}), 500
