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
- **Erro de inicialização**: Caso ocorra um erro durante a inicialização do CLI, uma mensagem de erro clara será exibida.
- **Erro de parsing de flags**: Se os flags forem inválidos ou faltarem, uma mensagem de erro clara será exibida.
- **Erro de geração de fractal**: Se ocorrer um erro durante a geração do fractal, uma mensagem de erro clara será exibida.
### Edge Cases
- **Tamanho de saída inválido**: Se o tamanho de saída for inválido (por exemplo, menor que 1), uma mensagem de erro clara será exibida.
- **Profundidade de recursão inválida**: Se a profundidade de recursão for inválida (por exemplo, menor que 1), uma mensagem de erro clara será exibida.
- **Caractere inválido**: Se o caractere for inválido (por exemplo, não for um caractere único), uma mensagem de erro clara será exibida.
- **Iterações inválidas**: Se o número de iterações for inválido (por exemplo, menor que 1), uma mensagem de erro clara será exibida.
### Segurança
- **Validação de entrada**: Todas as entradas serão validadas para evitar ataques de injeção de código.
- **Uso de bibliotecas seguras**: Somente bibliotecas seguras e atualizadas serão utilizadas.
- **Proteção contra ataques de força bruta**: O CLI será projetado para evitar ataques de força bruta.