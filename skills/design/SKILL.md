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
- **Tratamento de erros de entrada**: O programa deve lidar com entradas inválidas, como valores negativos para `--size`, `--width`, `--height`, `--depth` e `--iterations`. Além disso, deve verificar se o caractere fornecido para `--char` é válido.
- **Tratamento de excessão de profundidade**: O programa deve ter um limite de profundidade para evitar recursão infinita no caso do Sierpinski.
- **Tratamento de excessão de iterações**: O programa deve ter um limite de iterações para evitar loops infinitos no caso do Mandelbrot.
- **Tratamento de erro de saída**: O programa deve lidar com erros de saída, como falta de permissão para escrever na saída padrão.
- **Edge cases**:
  - Caso `--size` seja 0, o programa deve exibir uma mensagem de erro.
  - Caso `--width` ou `--height` seja 0, o programa deve exibir uma mensagem de erro.
  - Caso `--depth` seja 0, o programa deve exibir uma mensagem de erro.
  - Caso `--iterations` seja 0, o programa deve exibir uma mensagem de erro.
  - Caso o caractere fornecido para `--char` seja vazio, o programa deve exibir uma mensagem de erro.
Exemplos de tratamento de exceções e edge cases:
```go
func sierpinski(size int, depth int, char string) {
    if size <= 0 {
        log.Fatal("Tamanho deve ser maior que 0")
    }
    if depth <= 0 {
        log.Fatal("Profundidade deve ser maior que 0")
    }
    if char == "" {
        log.Fatal("Caractere não pode ser vazio")
    }
    // Lógica do Sierpinski
}

func mandelbrot(width int, height int, iterations int, char string) {
    if width <= 0 || height <= 0 {
        log.Fatal("Largura e altura devem ser maiores que 0")
    }
    if iterations <= 0 {
        log.Fatal("Número de iterações deve ser maior que 0")
    }
    if char == "" {
        log.Fatal("Caractere não pode ser vazio")
    }
    // Lógica do Mandelbrot
}
