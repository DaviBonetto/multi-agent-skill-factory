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
- **Erros de inicialização**: O programa deve lidar com erros de inicialização, como falhas ao carregar dependências ou inicializar a CLI. Nesses casos, o programa deve exibir uma mensagem de erro clara e sair com um código de status não zero.
### Edge Cases
- **Tamanho mínimo**: O programa deve lidar com tamanhos mínimos para `--size`, `--width` e `--height`. Por exemplo, se o tamanho mínimo for 1, o programa não deve permitir que esses valores sejam menores que 1.
- **Profundidade máxima**: O programa deve lidar com profundidades máximas para `--depth`. Por exemplo, se a profundidade máxima for 10, o programa não deve permitir que esse valor seja maior que 10.
- **Iterações máximas**: O programa deve lidar com iterações máximas para `--iterations`. Por exemplo, se a iteração máxima for 1000, o programa não deve permitir que esse valor seja maior que 1000.
- **Caracteres inválidos**: O programa deve lidar com caracteres inválidos para `--char`. Por exemplo, se o caractere for um caractere de controle ou um caractere não imprimível, o programa deve exibir uma mensagem de erro clara e sair com um código de status não zero.
### Exemplos de Edge Cases
- `fractals sierpinski --size 0` deve exibir uma mensagem de erro clara e sair com um código de status não zero.
- `fractals mandelbrot --width 0` deve exibir uma mensagem de erro clara e sair com um código de status não zero.
- `fractals sierpinski --depth 11` deve exibir uma mensagem de erro clara e sair com um código de status não zero, se a profundidade máxima for 10.
- `fractals mandelbrot --iterations 1001` deve exibir uma mensagem de erro clara e sair com um código de status não zero, se a iteração máxima for 1000.
- `fractals sierpinski --char \n` deve exibir uma mensagem de erro clara e sair com um código de status não zero, se o caractere for um caractere de controle ou um caractere não imprimível.