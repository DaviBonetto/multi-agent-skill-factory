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
*   Verificar se o valor de `--char` é um caractere único.
*   Tratar erros de divisão por zero e outros erros matemáticos que possam ocorrer durante a geração dos fractais.
*   Implementar tratamento de erros para casos de entrada inválida, como valores de flags não numéricos ou caracteres inválidos.
### Edge Cases
*   Caso de `--size` ou `--width`/`--height` muito grande: limitar o tamanho máximo da saída para evitar problemas de desempenho.
*   Caso de `--depth` ou `--iterations` muito grande: limitar o número máximo de iterações para evitar problemas de desempenho.
*   Caso de `--char` vazio: usar um caractere padrão ou exibir uma mensagem de erro.
*   Caso de entrada inválida: exibir uma mensagem de erro clara e concisa.
### Segurança
*   Validar todas as entradas de usuário para evitar ataques de injeção de comandos ou outros tipos de ataques.
*   Utilizar bibliotecas e frameworks seguros e atualizados para evitar vulnerabilidades conhecidas.
*   Implementar medidas de segurança para proteger contra acessos não autorizados e garantir a integridade dos dados.