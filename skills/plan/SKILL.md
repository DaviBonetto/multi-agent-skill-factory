# Go Fractals CLI - Implementation Plan

Execute this plan using the `superpowers:subagent-driven-development` skill.

## Context

Building a CLI tool that generates ASCII fractals. See `design.md` for full specification.

## Tasks

### Task 1: Project Setup

Create the Go module and directory structure.

**Do:**
- Initialize `go.mod` with module name `github.com/superpowers-test/fractals`
- Create directory structure: `cmd/fractals/`, `internal/sierpinski/`, `internal/mandelbrot/`, `internal/cli/`
- Create minimal `cmd/fractals/main.go` that prints "fractals cli"
- Add `github.com/spf13/cobra` dependency

**Verify:**
- `go build ./cmd/fractals` succeeds
- `./fractals` prints "fractals cli"

### Task 2: CLI Framework with Help

Set up Cobra root command with help output.

**Do:**
- Create `internal/cli/root.go` with root command
- Configure help text showing available subcommands
- Wire root command into `main.go`

**Verify:**
- `./fractals --help` shows usage with "sierpinski" and "mandelbrot" listed as available commands
- `./fractals` (no args) shows help

### Task 3: Sierpinski Algorithm

Implement the Sierpinski triangle generation algorithm.

**Do:**
- Create `internal/sierpinski/sierpinski.go`
- Implement `Generate(size, depth int, char rune) []string` that returns lines of the triangle
- Use recursive midpoint subdivision algorithm
- Create `internal/sierpinski/sierpinski_test.go` with tests:
  - Small triangle (size=4, depth=2) matches expected output
  - Size=1 returns single character
  - Depth=0 returns filled triangle

**Verify:**
- `go test ./internal/sierpinski/...` passes

### Task 4: Sierpinski CLI Integration

Wire the Sierpinski algorithm to a CLI subcommand.

**Do:**
- Create `internal/cli/sierpinski.go` with `sierpinski` subcommand
- Add flags: `--size` (default 32), `--depth` (default 5), `--char` (default '*')
- Call `sierpinski.Generate()` and print result to stdout

**Verify:**
- `./fractals sierpinski` outputs a triangle
- `./fractals sierpinski --size 16 --depth 3` outputs smaller triangle
- `./fractals sierpinski --help` shows flag documentation

### Task 5: Mandelbrot Algorithm

Implement the Mandelbrot set ASCII renderer.

**Do:**
- Create `internal/mandelbrot/mandelbrot.go`
- Implement `Render(width, height, maxIter int, char string) []string`
- Map complex plane region (-2.5 to 1.0 real, -1.0 to 1.0 imaginary) to output dimensions
- Map iteration count to character gradient ".:-=+*#%@" (or single char if provided)
- Create `internal/mandelbrot/mandelbrot_test.go` with tests:
  - Output dimensions match requested width/height
  - Known point inside set (0,0) maps to max-iteration character
  - Known point outside set (2,0) maps to low-iteration character

**Verify:**
- `go test ./internal/mandelbrot/...` passes

### Task 6: Mandelbrot CLI Integration

Wire the Mandelbrot algorithm to a CLI subcommand.

**Do:**
- Create `internal/cli/mandelbrot.go` with `mandelbrot` subcommand
- Add flags: `--width` (default 80), `--height` (default 24), `--iterations` (default 100), `--char` (default "")
- Call `mandelbrot.Render()` and print result to stdout

**Verify:**
- `./fractals mandelbrot` outputs recognizable Mandelbrot set
- `./fractals mandelbrot --width 40 --height 12` outputs smaller version
- `./fractals mandelbrot --help` shows flag documentation

### Task 7: Character Set Configuration

Ensure `--char` flag works consistently across both commands.

**Do:**
- Verify Sierpinski `--char` flag passes character to algorithm
- For Mandelbrot, `--char` should use single character instead of gradient
- Add tests for custom character output

**Verify:**
- `./fractals sierpinski --char '#'` uses '#' character
- `./fractals mandelbrot --char '.'` uses '.' for all filled points
- Tests pass

### Task 8: Input Validation and Error Handling

Add validation for invalid inputs.

**Do:**
- Sierpinski: size must be > 0, depth must be >= 0
- Mandelbrot: width/height must be > 0, iterations must be > 0
- Return clear error messages for invalid inputs
- Add tests for error cases

**Verify:**
- `./fractals sierpinski --size 0` prints error, exits non-zero
- `./fractals mandelbrot --width -1` prints error, exits non-zero
- Error messages are clear and helpful

### Task 9: Integration Tests

Add integration tests that invoke the CLI.

**Do:**
- Create `cmd/fractals/main_test.go` or `test/integration_test.go`
- Test full CLI invocation for both commands
- Verify output format and exit codes
- Test error cases return non-zero exit

**Verify:**
- `go test ./...` passes all tests including integration tests

### Task 10: README

Document usage and examples.

**Do:**
- Create `README.md` with:
  - Project description
  - Installation: `go install ./cmd/fractals`
  - Usage examples for both commands
  - Example output (small samples)

**Verify:**
- README accurately describes the tool
- Examples in README actually work

## ⚠️ Tratamento de Exceções e Edge Cases

### Exceções

*   Trate exceções de forma apropriada, garantindo que o programa não entre em um estado inconsistente.
*   Use `err` como tipo de retorno para funções que podem falhar.
*   Implemente tratamento de exceções personalizado para cada tipo de erro.

### Edge Cases

*   Defina casos de bordo para cada comando e algoritmo.
*   Verifique se os casos de bordo são tratados corretamente.
*   Adicione testes para casos de bordo.

### Exemplos de Tratamento de Exceções e Edge Cases

*   No comando Sierpinski:
    *   Trate o caso em que o tamanho é menor ou igual a zero.
    *   Trate o caso em que a profundidade é menor que zero.
*   No comando Mandelbrot:
    *   Trate o caso em que a largura ou altura é menor ou igual a zero.
    *   Trate o caso em que o número de iterações é menor ou igual a zero.

### Testes para Exceções e Edge Cases

*   Adicione testes para cada caso de bordo e exceção.
*   Verifique se os testes passam e se os erros são tratados corretamente.

### Código de Exemplo

```go
func GenerateSierpinski(size int, depth int, char rune) ([]string, error) {
    if size <= 0 {
        return nil, errors.New("tamanho deve ser maior que zero")
    }
    if depth < 0 {
        return nil, errors.New("profundidade deve ser maior ou igual a zero")
    }
    // Implementação do algoritmo Sierpinski
}

func RenderMandelbrot(width int, height int, maxIter int, char string) ([]string, error) {
    if width <= 0 || height <= 0 {
        return nil, errors.New("largura e altura devem ser maiores que zero")
    }
    if maxIter <= 0 {
        return nil, errors.New("número de iterações deve ser maior que zero")
    }
    // Implementação do algoritmo Mandelbrot
}
