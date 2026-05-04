# Go Fractals CLI - Design
## Overview
A command-line tool that generates ASCII art fractals. Supports two fractal types with configurable output.
## Usage
```bash
# Sierpinski triangle
fractals sierpinski --size 32 --depth 5
# Mandelbrot set
fractals mandelbrot --width 80 --height 24 --iterations 100
# Custom character
fractals sierpinski --size 16 --char '#'
# Help
fractals --help
fractals sierpinski --help
```
## Commands
### `sierpinski`
Generates a Sierpinski triangle using recursive subdivision.
Flags:
- `--size` (default: 32) - Width of the triangle base in characters
- `--depth` (default: 5) - Recursion depth
- `--char` (default: '*') - Character to use for filled points
Output: Triangle printed to stdout, one line per row.
### `mandelbrot`
Renders the Mandelbrot set as ASCII art. Maps iteration count to characters.
Flags:
- `--width` (default: 80) - Output width in characters
- `--height` (default: 24) - Output height in characters
- `--iterations` (default: 100) - Maximum iterations for escape calculation
- `--char` (default: gradient) - Single character, or omit for gradient " .:-=+*#%@"
Output: Rectangle printed to stdout.
## Architecture
```
cmd/
  fractals/
    main.go           # Entry point, CLI setup
internal/
  sierpinski/
    sierpinski.go     # Algorithm
    sierpinski_test.go
  mandelbrot/
    mandelbrot.go     # Algorithm
    mandelbrot_test.go
  cli/
    root.go           # Root command, help
    sierpinski.go     # Sierpinski subcommand
    mandelbrot.go     # Mandelbrot subcommand
```
## Dependencies
- Go 1.21+
- `github.com/spf13/cobra` for CLI
## Acceptance Criteria
1. `fractals --help` shows usage
2. `fractals sierpinski` outputs a recognizable triangle
3. `fractals mandelbrot` outputs a recognizable Mandelbrot set
4. `--size`, `--width`, `--height`, `--depth`, `--iterations` flags work
5. `--char` customizes output character
6. Invalid inputs produce clear error messages
7. All tests pass
## ⚠️ Tratamento de Exceções e Edge Cases
### Exceções
- **Entradas inválidas**: O programa deve lidar com entradas inválidas, como valores negativos para `--size`, `--width`, `--height`, `--depth` e `--iterations`. Nesses casos, o programa deve exibir uma mensagem de erro clara e sair com um código de status não zero.
- **Caracteres inválidos**: O programa deve lidar com caracteres inválidos para o flag `--char`. Nesse caso, o programa deve exibir uma mensagem de erro clara e sair com um código de status não zero.
- **Erros de inicialização**: O programa deve lidar com erros de inicialização, como falhas ao carregar bibliotecas ou configurar o ambiente. Nesses casos, o programa deve exibir uma mensagem de erro clara e sair com um código de status não zero.
### Edge Cases
- **Tamanhos mínimos**: O programa deve lidar com tamanhos mínimos para `--size`, `--width` e `--height`. Nesses casos, o programa deve exibir uma mensagem de erro clara e sair com um código de status não zero se o tamanho for menor que o mínimo permitido.
- **Profundidade máxima**: O programa deve lidar com a profundidade máxima para `--depth`. Nesse caso, o programa deve exibir uma mensagem de erro clara e sair com um código de status não zero se a profundidade for maior que a máxima permitida.
- **Iterações máximas**: O programa deve lidar com o número máximo de iterações para `--iterations`. Nesse caso, o programa deve exibir uma mensagem de erro clara e sair com um código de status não zero se o número de iterações for maior que o máximo permitido.
### Implementação
Para lidar com essas exceções e edge cases, o programa pode utilizar as seguintes estratégias:
- **Validação de entrada**: Validar as entradas antes de processá-las para garantir que elas sejam válidas e dentro dos limites permitidos.
- **Tratamento de erros**: Implementar tratamento de erros para lidar com exceções e edge cases, exibindo mensagens de erro claras e saindo com um código de status não zero quando necessário.
- **Testes**: Implementar testes para garantir que o programa lide corretamente com exceções e edge cases.