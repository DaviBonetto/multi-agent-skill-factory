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
*   Verificar se os valores de `--size`, `--width`, `--height`, `--depth` e `--iterations` são números inteiros positivos.
*   Verificar se o caractere especificado em `--char` é um caractere único.
*   Tratar erros de saída de arquivo, como falta de permissão para escrever na saída padrão.
*   Implementar tratamento de erros para os algoritmos de Sierpinski e Mandelbrot, como overflow de pilha devido à recursão excessiva.
### Edge Cases
*   **Tamanho mínimo**: Verificar como o programa se comporta com tamanhos mínimos para `--size`, `--width` e `--height` (por exemplo, 1).
*   **Tamanho máximo**: Verificar como o programa se comporta com tamanhos máximos para `--size`, `--width` e `--height` (por exemplo, valores próximos ao limite do tipo de dados).
*   **Profundidade máxima**: Verificar como o programa se comporta com valores altos de `--depth` para o triângulo de Sierpinski, considerando o risco de overflow de pilha.
*   **Iterações máximas**: Verificar como o programa se comporta com valores altos de `--iterations` para o conjunto de Mandelbrot, considerando o impacto no desempenho.
*   **Caractere inválido**: Verificar como o programa se comporta quando um caractere inválido é especificado para `--char`.