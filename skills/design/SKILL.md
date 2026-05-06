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
- **Entrada inválida**: O programa deve lidar com entradas inválidas, como valores negativos para `--size`, `--width`, `--height`, `--depth` e `--iterations`. Deve ser exibida uma mensagem de erro clara e concisa.
- **Caractere inválido**: O programa deve lidar com caracteres inválidos para `--char`. Deve ser exibida uma mensagem de erro clara e concisa.
- **Erro de saída**: O programa deve lidar com erros de saída, como falta de permissão para escrever na saída padrão.
### Edge Cases
- **Tamanho mínimo**: O programa deve lidar com tamanhos mínimos para `--size`, `--width` e `--height`. Deve ser exibida uma mensagem de erro clara e concisa se o tamanho for menor que o mínimo permitido.
- **Tamanho máximo**: O programa deve lidar com tamanhos máximos para `--size`, `--width` e `--height`. Deve ser exibida uma mensagem de erro clara e concisa se o tamanho for maior que o máximo permitido.
- **Profundidade mínima**: O programa deve lidar com profundidades mínimas para `--depth`. Deve ser exibida uma mensagem de erro clara e concisa se a profundidade for menor que a mínima permitida.
- **Profundidade máxima**: O programa deve lidar com profundidades máximas para `--depth`. Deve ser exibida uma mensagem de erro clara e concisa se a profundidade for maior que a máxima permitida.
- **Iterações mínimas**: O programa deve lidar com iterações mínimas para `--iterations`. Deve ser exibida uma mensagem de erro clara e concisa se o número de iterações for menor que o mínimo permitido.
- **Iterações máximas**: O programa deve lidar com iterações máximas para `--iterations`. Deve ser exibida uma mensagem de erro clara e concisa se o número de iterações for maior que o máximo permitido.
### Exemplos de Entradas Inválidas
- `fractals sierpinski --size -1 --depth 5`
- `fractals mandelbrot --width 80 --height 24 --iterations -1`
- `fractals sierpinski --char abc`
### Exemplos de Saídas de Erro
- `Erro: tamanho inválido para --size. Valor deve ser maior que 0.`
- `Erro: caractere inválido para --char. Valor deve ser um caractere único.`
- `Erro: falta de permissão para escrever na saída padrão.`