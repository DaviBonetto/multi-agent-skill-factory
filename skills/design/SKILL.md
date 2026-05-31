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
- **Erro de entrada inválida**: Caso o usuário forneça uma entrada inválida, como um valor não numérico para `--size` ou `--depth`, o programa deve exibir uma mensagem de erro clara e sair com um código de status não zero.
- **Erro de inicialização**: Se ocorrer um erro durante a inicialização do programa, como falha ao carregar uma dependência, o programa deve exibir uma mensagem de erro clara e sair com um código de status não zero.
### Edge Cases
- **Tamanho mínimo**: O programa deve lidar com tamanhos mínimos para `--size` e `--width`, como 1, e produzir uma saída válida.
- **Tamanho máximo**: O programa deve lidar com tamanhos máximos para `--size` e `--width`, como 1000, e produzir uma saída válida ou exibir uma mensagem de erro se o tamanho for muito grande.
- **Profundidade mínima**: O programa deve lidar com profundidades mínimas para `--depth`, como 1, e produzir uma saída válida.
- **Profundidade máxima**: O programa deve lidar com profundidades máximas para `--depth`, como 100, e produzir uma saída válida ou exibir uma mensagem de erro se a profundidade for muito grande.
- **Iterações mínimas**: O programa deve lidar com iterações mínimas para `--iterations`, como 1, e produzir uma saída válida.
- **Iterações máximas**: O programa deve lidar com iterações máximas para `--iterations`, como 1000, e produzir uma saída válida ou exibir uma mensagem de erro se o número de iterações for muito grande.
### Segurança
- **Injeção de comandos**: O programa deve evitar a injeção de comandos, garantindo que as entradas do usuário sejam validadas e sanitizadas antes de serem usadas para executar comandos.
- **Exposição de dados**: O programa deve evitar a exposição de dados sensíveis, como chaves de API ou credenciais de autenticação, garantindo que esses dados sejam armazenados de forma segura e não sejam expostos em logs ou saídas.