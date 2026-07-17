---
name: Arquitetura de Sistemas Distribuídos com Apache Kafka
description: Ensina como projetar e implantar sistemas distribuídos utilizando Apache Kafka e Zookeeper
---

## Objetivo
O objetivo deste guia é fornecer uma visão geral de como projetar e implantar sistemas distribuídos utilizando Apache Kafka e Zookeeper. Ao final deste guia, você será capaz de entender como criar um sistema distribuído escalável e confiável utilizando essas tecnologias.

## Pré-requisitos
Para seguir este guia, você deve ter conhecimento básico em:
* Sistemas distribuídos
* Apache Kafka
* Zookeeper
* Linguagens de programação como Java ou Python

Além disso, é recomendado ter experiência com:
* Desenvolvimento de software
* Arquitetura de sistemas

## Passo a Passo Técnico / Exemplos de Código
### Instalação do Apache Kafka e Zookeeper
Para começar, você precisará instalar o Apache Kafka e o Zookeeper em sua máquina. Você pode fazer isso seguindo os passos abaixo:

1. Instale o Java 8 ou superior em sua máquina.
2. Baixe o Apache Kafka e o Zookeeper a partir do site oficial.
3. Extraia os arquivos baixados em uma pasta de sua escolha.
4. Configure o Zookeeper editando o arquivo `zoo.cfg` e adicionando as seguintes linhas:
```bash
tickTime=2000
initLimit=10
syncLimit=5
dataDir=/var/lib/zookeeper
clientPort=2181
```
5. Inicie o Zookeeper executando o comando `./zkServer.sh start` no terminal.

### Configuração do Apache Kafka
Agora que o Zookeeper está configurado, você pode configurar o Apache Kafka. Edite o arquivo `server.properties` e adicione as seguintes linhas:
```properties
broker.id=0
num.partitions=1
zookeeper.connect=localhost:2181
```
Inicie o Apache Kafka executando o comando `./kafka-server-start.sh` no terminal.

### Produzindo e Consumindo Mensagens
Agora que o Apache Kafka está configurado, você pode produzir e consumir mensagens. Crie um produtor de mensagens utilizando a seguinte classe Java:
```java
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;

import java.util.Properties;

public class Producer {
    public static void main(String[] args) {
        Properties props = new Properties();
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringSerializer");
        props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringSerializer");

        KafkaProducer<String, String> producer = new KafkaProducer<>(props);
        ProducerRecord<String, String> record = new ProducerRecord<>("meu-topico", "Minha mensagem");
        try {
            producer.send(record);
        } catch (Exception e) {
            System.out.println("Erro ao enviar mensagem: " + e.getMessage());
        }
    }
}
```
E crie um consumidor de mensagens utilizando a seguinte classe Java:
```java
import org.apache.kafka.clients.consumer.KafkaConsumer;
import org.apache.kafka.clients.consumer.ConsumerConfig;
import org.apache.kafka.clients.consumer.ConsumerRecord;

import java.util.Collections;
import java.util.Properties;

public class Consumer {
    public static void main(String[] args) {
        Properties props = new Properties();
        props.put(ConsumerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        props.put(ConsumerConfig.GROUP_ID_CONFIG, "meu-grupo");
        props.put(ConsumerConfig.KEY_DESERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringDeserializer");
        props.put(ConsumerConfig.VALUE_DESERIALIZER_CLASS_CONFIG, "org.apache.kafka.common.serialization.StringDeserializer");

        KafkaConsumer<String, String> consumer = new KafkaConsumer<>(props);
        consumer.subscribe(Collections.singleton("meu-topico"));
        while (true) {
            try {
                for (ConsumerRecord<String, String> record : consumer.poll(100)) {
                    System.out.println(record.value());
                }
            } catch (Exception e) {
                System.out.println("Erro ao consumir mensagem: " + e.getMessage());
            }
        }
    }
}
```
## Validação
Para validar a configuração do Apache Kafka e do Zookeeper, você pode utilizar as ferramentas de linha de comando fornecidas com o Apache Kafka. Por exemplo, você pode utilizar o comando `./kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic meu-topico` para consumir mensagens do tópico "meu-topico".

Além disso, você pode utilizar as APIs do Apache Kafka para produzir e consumir mensagens programaticamente. Isso permite que você integre o Apache Kafka com seus sistemas existentes e aproveite os benefícios de um sistema distribuído escalável e confiável.

## ⚠️ Tratamento de Exceções e Edge Cases
Ao trabalhar com o Apache Kafka, é importante considerar os seguintes casos de exceção e edge cases:

* **Conexão perdida com o Zookeeper**: Se a conexão com o Zookeeper for perdida, o Apache Kafka pode não funcionar corretamente. Para lidar com isso, você pode implementar um mecanismo de reconexão automática.
* **Tópico não existe**: Se o tópico não existir, o Apache Kafka retornará um erro. Para lidar com isso, você pode criar o tópico antes de tentar produzir ou consumir mensagens.
* **Mensagem inválida**: Se a mensagem for inválida, o Apache Kafka pode não processá-la corretamente. Para lidar com isso, você pode implementar uma validação de mensagens antes de produzi-las.
* **Desconexão do consumidor**: Se o consumidor se desconectar, as mensagens podem ser perdidas. Para lidar com isso, você pode implementar um mecanismo de reconexão automática e utilizar o offset para garantir que as mensagens sejam processadas corretamente.
* **Produção de mensagens em paralelo**: Se múltiplos produtores estiverem produzindo mensagens em paralelo, pode haver problemas de concorrência. Para lidar com isso, você pode utilizar um mecanismo de sincronização para garantir que as mensagens sejam processadas corretamente.

Exemplo de como lidar com exceções em Java:
```java
try {
    // Código que pode lançar exceção
} catch (KafkaException e) {
    // Lidar com a exceção
    System.out.println("Erro ao produzir mensagem: " + e.getMessage());
} catch (Exception e) {
    // Lidar com a exceção
    System.out.println("Erro inesperado: " + e.getMessage());
}
```
