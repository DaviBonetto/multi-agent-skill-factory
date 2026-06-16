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
*   Verificar se o tamanho da saída é válido (maior que 0) antes de gerar o fractal.
*   Verificar se a profundidade do fractal é válida (maior que 0) antes de gerar o Sierpinski.
*   Verificar se o número de iterações é válido (maior que 0) antes de gerar o Mandelbrot.
*   Tratar erros de leitura e escrita de arquivos, caso seja necessário ler ou escrever arquivos.
*   Tratar erros de inicialização do CLI, caso ocorra um erro ao inicializar o Cobra.
### Edge Cases
*   Tamanho mínimo e máximo para o fractal (por exemplo, 1x1 a 100x100).
*   Profundidade mínima e máxima para o Sierpinski (por exemplo, 1 a 10).
*   Número mínimo e máximo de iterações para o Mandelbrot (por exemplo, 1 a 1000).
*   Caractere inválido para o `--char` (por exemplo, um caractere não impresso).
*   Comando inválido ou desconhecido.
*   Falta de argumentos obrigatórios.
### Implementação
Para lidar com esses casos, podemos adicionar verificações e tratamentos de erros em cada parte do código que possa gerar um erro. Por exemplo:
```go
func generateSierpinski(size int, depth int, char string) error {
    if size <= 0 {
        return errors.New("tamanho inválido")
    }
    if depth <= 0 {
        return errors.New("profundidade inválida")
    }
    // ...
}

func generateMandelbrot(width int, height int, iterations int) error {
    if width <= 0 || height <= 0 {
        return errors.New("tamanho inválido")
    }
    if iterations <= 0 {
        return errors.New("número de iterações inválido")
    }
    // ...
}
```
Além disso, podemos usar o pacote `errors` do Go para criar erros personalizados e melhorar a legibilidade do código.
```go
var (
    ErrInvalidSize = errors.New("tamanho inválido")
    ErrInvalidDepth = errors.New("profundidade inválida")
    ErrInvalidIterations = errors.New("número de iterações inválido")
)
