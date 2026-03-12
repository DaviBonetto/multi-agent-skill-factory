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
- **Erro de inicialização**: Caso ocorra um erro durante a inicialização do CLI, o programa deve exibir uma mensagem de erro clara e sair com um código de erro não zero.
- **Erro de parsing de flags**: Se um flag for passado com um valor inválido, o programa deve exibir uma mensagem de erro clara e sair com um código de erro não zero.
- **Erro de geração de fractal**: Se ocorrer um erro durante a geração de um fractal, o programa deve exibir uma mensagem de erro clara e sair com um código de erro não zero.
### Edge Cases
- **Tamanho de saída muito grande**: Se o tamanho de saída for muito grande, o programa deve ser capaz de lidar com isso sem travar ou consumir muita memória.
- **Profundidade de recursão muito grande**: Se a profundidade de recursão for muito grande, o programa deve ser capaz de lidar com isso sem estourar a pilha de chamadas.
- **Caractere inválido**: Se um caractere inválido for passado como parâmetro, o programa deve exibir uma mensagem de erro clara e sair com um código de erro não zero.
- **Flags conflitantes**: Se flags conflitantes forem passados, o programa deve exibir uma mensagem de erro clara e sair com um código de erro não zero.
### Testes
- **Testes unitários**: Devem ser escritos testes unitários para garantir que cada parte do programa esteja funcionando corretamente.
- **Testes de integração**: Devem ser escritos testes de integração para garantir que o programa esteja funcionando corretamente como um todo.
- **Testes de edge cases**: Devem ser escritos testes para garantir que o programa esteja lidando corretamente com edge cases.