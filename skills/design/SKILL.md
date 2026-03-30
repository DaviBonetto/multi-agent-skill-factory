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
- **Entradas inválidas**: O programa deve lidar com entradas inválidas, como valores negativos para `--size`, `--width`, `--height`, `--depth` e `--iterations`. Deve ser exibida uma mensagem de erro clara e concisa.
- **Caracteres inválidos**: O programa deve lidar com caracteres inválidos para o flag `--char`. Deve ser exibida uma mensagem de erro clara e concisa.
- **Tamanho máximo**: O programa deve lidar com tamanhos máximos para `--size`, `--width` e `--height`. Deve ser exibida uma mensagem de erro clara e concisa.
### Edge Cases
- **Tamanho mínimo**: O programa deve lidar com tamanhos mínimos para `--size`, `--width` e `--height`. Deve ser exibida uma saída válida.
- **Profundidade mínima**: O programa deve lidar com profundidades mínimas para `--depth`. Deve ser exibida uma saída válida.
- **Iterações mínimas**: O programa deve lidar com iterações mínimas para `--iterations`. Deve ser exibida uma saída válida.
- **Caracteres especiais**: O programa deve lidar com caracteres especiais para o flag `--char`. Deve ser exibida uma saída válida.
### Exemplos de Exceções e Edge Cases
- `fractals sierpinski --size -1` deve exibir uma mensagem de erro clara e concisa.
- `fractals mandelbrot --width 0` deve exibir uma mensagem de erro clara e concisa.
- `fractals sierpinski --char @` deve exibir uma saída válida.
- `fractals mandelbrot --iterations 1` deve exibir uma saída válida.