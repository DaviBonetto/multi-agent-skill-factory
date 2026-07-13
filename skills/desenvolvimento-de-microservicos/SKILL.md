---
name: Desenvolvimento de Microserviços com Spring Boot
description: Esta habilidade ensina como criar microserviços escaláveis e resilientes utilizando Spring Boot
---

## Objetivo
O objetivo desta habilidade é capacitar os desenvolvedores a criar microserviços escaláveis e resilientes utilizando Spring Boot, abordando definição de APIs, gerenciamento de dependências e deploy em contêineres.

## Pré-requisitos
Para iniciar este curso, é necessário ter conhecimentos básicos em:
- Java 8 ou superior
- Spring Framework
- Conceitos de microserviços e arquitetura de software

## Passo a Passo Técnico / Exemplos de Código
### Definição de APIs
Para começar, vamos criar uma API simples utilizando Spring Boot. Primeiro, criaremos um novo projeto Spring Boot e adicionaremos as dependências necessárias ao arquivo `pom.xml` (se estiver usando Maven) ou `build.gradle` (se estiver usando Gradle).

```xml
<!-- Maven -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```

```groovy
// Gradle
implementation 'org.springframework.boot:spring-boot-starter-web'
```

Em seguida, criaremos um controlador que irá lidar com as requisições HTTP:

```java
@RestController
@RequestMapping("/api")
public class MeuControlador {
    
    @GetMapping("/ola")
    public String ola() {
        return "Olá, mundo!";
    }
}
```

### Gerenciamento de Dependências
O Spring Boot facilita o gerenciamento de dependências, pois já vem com muitas delas configuradas por padrão. No entanto, é importante entender como elas são gerenciadas. Por exemplo, se você precisar adicionar uma dependência para trabalhar com banco de dados, poderá adicioná-la da seguinte maneira:

```xml
<!-- Maven -->
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
    <scope>runtime</scope>
</dependency>
```

```groovy
// Gradle
runtimeOnly 'com.h2database:h2'
```

### Deploy em Contêineres
Para deployar sua aplicação em contêineres, você precisará criar uma imagem Docker. Isso pode ser feito utilizando o Dockerfile:

```dockerfile
FROM openjdk:8-jdk-alpine
ARG JAR_FILE=target/meu-app-0.0.1-SNAPSHOT.jar
COPY ${JAR_FILE} app.jar
ENTRYPOINT ["java","-jar","/app.jar"]
```

E, em seguida, construir e executar a imagem:

```bash
docker build -t meu-app .
docker run -p 8080:8080 meu-app
```

## Validação
Para validar o funcionamento da sua aplicação, você pode utilizar ferramentas como o Postman para fazer requisições HTTP para a API que você criou. Além disso, é importante realizar testes unitários e de integração para garantir que a aplicação esteja funcionando corretamente.

## Tratamento de Exceções e Edge Cases
É fundamental considerar os possíveis erros e exceções que podem ocorrer durante a execução da aplicação. Aqui estão alguns exemplos de como lidar com esses casos:

*   **Tratamento de Exceções**: Utilize blocos try-catch para capturar e tratar exceções que possam ocorrer durante a execução da aplicação. Por exemplo:

    ```java
@RestControllerAdvice
public class MeuExceptionHandler {
    
    @ExceptionHandler(value = Exception.class)
    public ResponseEntity<String> handleException(Exception e) {
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Ocorreu um erro interno");
    }
}
```

*   **Validação de Dados**: Valide os dados de entrada para garantir que eles estejam corretos e consistentes. Por exemplo:

    ```java
public class MeuControlador {
    
    @GetMapping("/ola")
    public String ola(@RequestParam("nome") @NotEmpty String nome) {
        return "Olá, " + nome + "!";
    }
}
```

*   **Segurança**: Implemente medidas de segurança para proteger a aplicação contra ataques e vulnerabilidades. Por exemplo, utilize autenticação e autorização para controlar o acesso à aplicação:

    ```java
@Configuration
@EnableWebSecurity
public class MeuSecurityConfig extends WebSecurityConfigurerAdapter {
    
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.authorizeRequests()
            .antMatchers("/api/**").authenticated()
            .and()
            .httpBasic();
    }
}
```

Lembre-se de que a prática e a experimentação são fundamentais para dominar o desenvolvimento de microserviços com Spring Boot. Este guia forneceu uma visão geral dos passos necessários, mas é importante aprofundar-se em cada um desses tópicos para se tornar um desenvolvedor mais eficaz.