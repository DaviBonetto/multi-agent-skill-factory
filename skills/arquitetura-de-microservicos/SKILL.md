---
name: Arquitetura de Microserviços com Spring Boot
description: Ensina como projetar e implementar arquiteturas de microserviços utilizando Spring Boot
---

## Objetivo
O objetivo deste guia é fornecer uma visão geral de como projetar e implementar arquiteturas de microserviços utilizando Spring Boot, abordando os principais conceitos e práticas para desenvolver sistemas escaláveis e manuteníveis.

## Pré-requisitos
Para seguir este guia, é necessário ter conhecimento em:
- Java 8 ou superior
- Spring Framework
- Conhecimento básico de arquitetura de microserviços
- Ferramentas de desenvolvimento como Maven ou Gradle

## Passo a Passo Técnico / Exemplos de Código
### 1. Configuração do Projeto
Para começar, crie um novo projeto Spring Boot e adicione as dependências necessárias para o desenvolvimento de microserviços. Por exemplo, utilizando o Maven, adicione as seguintes dependências ao seu `pom.xml`:
```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.cloud</groupId>
        <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
    </dependency>
</dependencies>
```
### 2. Desenvolvimento do Microserviço
Desenvolva o microserviço criando uma classe que represente o serviço, por exemplo, `UserService`:
```java
@Service
public class UserService {
    
    @Autowired
    private UserRepository userRepository;
    
    public List<User> getAllUsers() {
        return userRepository.findAll();
    }
    
    // Adicionando tratamento de exceção para caso de erro na consulta
    @ExceptionHandler(value = Exception.class)
    public ResponseEntity<String> handleException(Exception e) {
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body("Ocorreu um erro: " + e.getMessage());
    }
}
```
### 3. Implementação da API REST
Crie uma API REST para expor os serviços do microserviço. Por exemplo:
```java
@RestController
@RequestMapping("/users")
public class UserController {
    
    @Autowired
    private UserService userService;
    
    @GetMapping
    public List<User> getAllUsers() {
        return userService.getAllUsers();
    }
    
    // Adicionando validação para parâmetros de entrada
    @GetMapping("/{id}")
    public User getUserById(@PathVariable Long id) {
        if (id == null || id <= 0) {
            throw new IllegalArgumentException("Id inválido");
        }
        return userService.getUserById(id);
    }
}
```
### 4. Registração no Eureka
Configure o microserviço para se registrar no Eureka:
```java
@SpringBootApplication
@EnableDiscoveryClient
public class Application {
    
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```
## Validação
Para validar a implementação, execute o microserviço e verifique se ele está registrado no Eureka. Em seguida, utilize uma ferramenta como o Postman para testar a API REST exposta pelo microserviço. Verifique se as respostas estão de acordo com o esperado e se o microserviço está funcionando corretamente.

## ⚠️ Tratamento de Exceções e Edge Cases
Além do tratamento de exceções apresentado nos exemplos acima, é importante considerar os seguintes casos de bordo:
- **Conexão com o banco de dados**: Verifique se a conexão com o banco de dados está funcionando corretamente e trate exceções relacionadas a isso.
- **Timeouts**: Defina timeouts adequados para as operações do microserviço e trate exceções relacionadas a timeouts.
- **Parâmetros de entrada inválidos**: Valide os parâmetros de entrada e trate exceções relacionadas a parâmetros inválidos.
- **Erros de rede**: Trate exceções relacionadas a erros de rede, como conexões recusadas ou timeouts de rede.
- **Segurança**: Implemente medidas de segurança, como autenticação e autorização, para proteger o microserviço contra acessos não autorizados.

Exemplo de tratamento de exceção para conexão com o banco de dados:
```java
@Repository
public class UserRepository {
    
    @Autowired
    private DataSource dataSource;
    
    public List<User> findAll() {
        try {
            // Código para consultar o banco de dados
        } catch (SQLException e) {
            throw new RuntimeException("Erro ao consultar o banco de dados", e);
        }
    }
}
```
Exemplo de tratamento de exceção para timeouts:
```java
@Service
public class UserService {
    
    @Autowired
    private UserRepository userRepository;
    
    public List<User> getAllUsers() {
        try {
            // Código para consultar o repositório com timeout
            return userRepository.findAll();
        } catch (TimeoutException e) {
            throw new RuntimeException("Timeout ao consultar o repositório", e);
        }
    }
}
