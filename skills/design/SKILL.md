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
### Tratamento de Erros
- **Flags inválidos**: O programa deve retornar uma mensagem de erro clara quando um flag inválido for passado.
- **Valores inválidos**: O programa deve retornar uma mensagem de erro clara quando um valor inválido for passado para um flag.
- **Saída inválida**: O programa deve retornar uma mensagem de erro clara quando a saída for inválida (por exemplo, quando o tamanho da saída for maior que o tamanho da tela).
### Edge Cases
- **Tamanho mínimo**: O programa deve lidar corretamente com tamanhos mínimos para os fractais (por exemplo, tamanho 1 para o triângulo de Sierpinski).
- **Tamanho máximo**: O programa deve lidar corretamente com tamanhos máximos para os fractais (por exemplo, tamanho maior que o tamanho da tela).
- **Profundidade mínima**: O programa deve lidar corretamente com profundidades mínimas para o triângulo de Sierpinski (por exemplo, profundidade 0).
- **Profundidade máxima**: O programa deve lidar corretamente com profundidades máximas para o triângulo de Sierpinski (por exemplo, profundidade maior que o máximo permitido).
- **Iterações mínimas**: O programa deve lidar corretamente com iterações mínimas para o conjunto de Mandelbrot (por exemplo, iterações 0).
- **Iterações máximas**: O programa deve lidar corretamente com iterações máximas para o conjunto de Mandelbrot (por exemplo, iterações maior que o máximo permitido).