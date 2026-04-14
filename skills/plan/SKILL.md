# Svelte Todo List - Implementation Plan

Execute this plan using the `superpowers:subagent-driven-development` skill.

## Context

Building a todo list app with Svelte. See `design.md` for full specification.

## Tasks

### Task 1: Project Setup

Create the Svelte project with Vite.

**Do:**
- Run `npm create vite@latest . -- --template svelte-ts`
- Install dependencies with `npm install`
- Verify dev server works
- Clean up default Vite template content from App.svelte

**Verify:**
- `npm run dev` starts server
- App shows minimal "Svelte Todos" heading
- `npm run build` succeeds

### Task 2: Todo Store

Create the Svelte store for todo state management.

**Do:**
- Create `src/lib/store.ts`
- Define `Todo` interface with id, text, completed
- Create writable store with initial empty array
- Export functions: `addTodo(text)`, `toggleTodo(id)`, `deleteTodo(id)`, `clearCompleted()`
- Create `src/lib/store.test.ts` with tests for each function
- Handle potential errors:
  - Validate input for `addTodo` to prevent empty or null text
  - Check for existing todo before adding a new one to prevent duplicates
  - Handle cases where `toggleTodo`, `deleteTodo`, or `clearCompleted` are called with invalid or non-existent todo IDs

**Verify:**
- Tests pass: `npm run test` (install vitest if needed)

### Task 3: localStorage Persistence

Add persistence layer for todos.

**Do:**
- Create `src/lib/storage.ts`
- Implement `loadTodos(): Todo[]` and `saveTodos(todos: Todo[])`
- Handle JSON parse errors gracefully (return empty array)
- Integrate with store: load on init, save on change
- Add tests for load/save/error handling
- Consider edge cases:
  - Handle storage quota exceeded errors
  - Implement a fallback for browsers that do not support localStorage

**Verify:**
- Tests pass
- Manual test: add todo, refresh page, todo persists

### Task 4: TodoInput Component

Create the input component for adding todos.

**Do:**
- Create `src/lib/TodoInput.svelte`
- Text input bound to local state
- Add button calls `addTodo()` and clears input
- Enter key also submits
- Disable Add button when input is empty
- Add component tests
- Consider accessibility:
  - Ensure the input field is focusable and has a clear label
  - Implement ARIA attributes for screen readers

**Verify:**
- Tests pass
- Component renders input and button

### Task 5: TodoItem Component

Create the single todo item component.

**Do:**
- Create `src/lib/TodoItem.svelte`
- Props: `todo: Todo`
- Checkbox toggles completion (calls `toggleTodo`)
- Text with strikethrough when completed
- Delete button (X) calls `deleteTodo`
- Add component tests
- Handle edge cases:
  - Prevent deletion of the last todo item without confirmation
  - Display a warning when attempting to delete a todo item that has not been saved

**Verify:**
- Tests pass
- Component renders checkbox, text, delete button

### Task 6: TodoList Component

Create the list container component.

**Do:**
- Create `src/lib/TodoList.svelte`
- Props: `todos: Todo[]`
- Renders TodoItem for each todo
- Shows "No todos yet" when empty
- Add component tests
- Consider performance:
  - Use a virtualized list for large numbers of todo items
  - Optimize rendering to prevent unnecessary re-renders

**Verify:**
- Tests pass
- Component renders list of TodoItems

### Task 7: FilterBar Component

Create the filter and status bar component.

**Do:**
- Create `src/lib/FilterBar.svelte`
- Props: `todos: Todo[]`, `filter: Filter`, `onFilterChange: (f: Filter) => void`
- Show count: "X items left" (incomplete count)
- Three filter buttons: All, Active, Completed
- Active filter is visually highlighted
- "Clear completed" button (hidden when no completed todos)
- Add component tests
- Handle edge cases:
  - Prevent filter changes when there are no todos
  - Display a warning when attempting to clear completed todos without confirmation

**Verify:**
- Tests pass
- Component renders count, filters, clear button

### Task 8: App Integration

Wire all components together in App.svelte.

**Do:**
- Import all components and store
- Add filter state (default: 'all')
- Compute filtered todos based on filter state
- Render: heading, TodoInput, TodoList, FilterBar
- Pass appropriate props to each component
- Handle potential errors:
  - Validate filter state to prevent invalid filter values
  - Check for missing or invalid props before rendering components

**Verify:**
- App renders all components
- Adding todos works
- Toggling works
- Deleting works

### Task 9: Filter Functionality

Ensure filtering works end-to-end.

**Do:**
- Verify filter buttons change displayed todos
- 'all' shows all todos
- 'active' shows only incomplete todos
- 'completed' shows only completed todos
- Clear completed removes completed todos and resets filter if needed
- Add integration tests
- Consider edge cases:
  - Handle filtering when there are no todos
  - Display a warning when attempting to clear completed todos without confirmation

**Verify:**
- Filter tests pass
- Manual verification of all filter states

### Task 10: Styling and Polish

Add CSS styling for usability.

**Do:**
- Style the app to match the design mockup
- Completed todos have strikethrough and muted color
- Active filter button is highlighted
- Input has focus styles
- Delete button appears on hover (or always on mobile)
- Responsive layout
- Consider accessibility:
  - Ensure sufficient color contrast between text and background
  - Implement ARIA attributes for screen readers

**Verify:**
- App is visually usable
- Styles don't break functionality

### Task 11: End-to-End Tests

Add Playwright tests for full user flows.

**Do:**
- Install Playwright: `npm init playwright@latest`
- Create `tests/todo.spec.ts`
- Test flows:
  - Add a todo
  - Complete a todo
  - Delete a todo
  - Filter todos
  - Clear completed
  - Persistence (add, reload, verify)
- Consider edge cases:
  - Test for errors when adding, completing, or deleting todos
  - Verify that filtering works correctly in all scenarios

**Verify:**
- `npx playwright test` passes

### Task 12: README

Document the project.

**Do:**
- Create `README.md` with:
  - Project description
  - Setup: `npm install`
  - Development: `npm run dev`
  - Testing: `npm test` and `npx playwright test`
  - Build: `npm run build`
- Consider adding:
  - Troubleshooting section for common issues
  - Contributing guidelines for new contributors

**Verify:**
- README accurately describes the project
- Instructions work

## ⚠️ Tratamento de Exceções e Edge Cases

Ao longo do desenvolvimento do aplicativo, é fundamental considerar e tratar exceções e edge cases para garantir a robustez e confiabilidade do sistema. Isso inclui:

- **Validação de entrada**: Verificar a validade dos dados de entrada para prevenir erros e garantir a consistência dos dados.
- **Tratamento de erros**: Implementar mecanismos de tratamento de erros para lidar com situações inesperadas, como falhas de rede ou erros de parsing de JSON.
- **Edge cases**: Considerar cenários de borda, como a presença de caracteres especiais em entradas de texto, ou a falta de suporte a recursos específicos em navegadores mais antigos.
- **Testes**: Realizar testes abrangentes para garantir que o aplicativo se comporta corretamente em diferentes situações e ambientes.

Ao abordar esses aspectos, podemos desenvolver um aplicativo mais robusto e confiável, capaz de lidar com uma variedade de situações e fornecer uma experiência de usuário mais satisfatória.