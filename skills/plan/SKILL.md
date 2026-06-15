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
- Handle potential errors during setup, such as network issues or incompatible dependencies

**Verify:**
- `npm run dev` starts server
- App shows minimal "Svelte Todos" heading
- `npm run build` succeeds
- Error handling: verify that the app gracefully handles and logs errors during setup

---

### Task 2: Todo Store

Create the Svelte store for todo state management.

**Do:**
- Create `src/lib/store.ts`
- Define `Todo` interface with id, text, completed
- Create writable store with initial empty array
- Export functions: `addTodo(text)`, `toggleTodo(id)`, `deleteTodo(id)`, `clearCompleted()`
- Create `src/lib/store.test.ts` with tests for each function
- Implement error handling for store operations, such as handling duplicate todo IDs

**Verify:**
- Tests pass: `npm run test` (install vitest if needed)
- Error handling: verify that the store handles and logs errors during operations

---

### Task 3: localStorage Persistence

Add persistence layer for todos.

**Do:**
- Create `src/lib/storage.ts`
- Implement `loadTodos(): Todo[]` and `saveTodos(todos: Todo[])`
- Handle JSON parse errors gracefully (return empty array)
- Integrate with store: load on init, save on change
- Add tests for load/save/error handling
- Handle potential storage limitations, such as quota exceeded errors

**Verify:**
- Tests pass
- Manual test: add todo, refresh page, todo persists
- Error handling: verify that the app handles and logs storage-related errors

---

### Task 4: TodoInput Component

Create the input component for adding todos.

**Do:**
- Create `src/lib/TodoInput.svelte`
- Text input bound to local state
- Add button calls `addTodo()` and clears input
- Enter key also submits
- Disable Add button when input is empty
- Add component tests
- Handle potential input validation errors, such as empty input

**Verify:**
- Tests pass
- Component renders input and button
- Error handling: verify that the component handles and logs input validation errors

---

### Task 5: TodoItem Component

Create the single todo item component.

**Do:**
- Create `src/lib/TodoItem.svelte`
- Props: `todo: Todo`
- Checkbox toggles completion (calls `toggleTodo`)
- Text with strikethrough when completed
- Delete button (X) calls `deleteTodo`
- Add component tests
- Handle potential rendering errors, such as missing todo data

**Verify:**
- Tests pass
- Component renders checkbox, text, delete button
- Error handling: verify that the component handles and logs rendering errors

---

### Task 6: TodoList Component

Create the list container component.

**Do:**
- Create `src/lib/TodoList.svelte`
- Props: `todos: Todo[]`
- Renders TodoItem for each todo
- Shows "No todos yet" when empty
- Add component tests
- Handle potential rendering errors, such as empty todo list

**Verify:**
- Tests pass
- Component renders list of TodoItems
- Error handling: verify that the component handles and logs rendering errors

---

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
- Handle potential filtering errors, such as invalid filter state

**Verify:**
- Tests pass
- Component renders count, filters, clear button
- Error handling: verify that the component handles and logs filtering errors

---

### Task 8: App Integration

Wire all components together in App.svelte.

**Do:**
- Import all components and store
- Add filter state (default: 'all')
- Compute filtered todos based on filter state
- Render: heading, TodoInput, TodoList, FilterBar
- Pass appropriate props to each component
- Handle potential integration errors, such as mismatched component props

**Verify:**
- App renders all components
- Adding todos works
- Toggling works
- Deleting works
- Error handling: verify that the app handles and logs integration errors

---

### Task 9: Filter Functionality

Ensure filtering works end-to-end.

**Do:**
- Verify filter buttons change displayed todos
- 'all' shows all todos
- 'active' shows only incomplete todos
- 'completed' shows only completed todos
- Clear completed removes completed todos and resets filter if needed
- Add integration tests
- Handle potential filtering errors, such as invalid filter state

**Verify:**
- Filter tests pass
- Manual verification of all filter states
- Error handling: verify that the app handles and logs filtering errors

---

### Task 10: Styling and Polish

Add CSS styling for usability.

**Do:**
- Style the app to match the design mockup
- Completed todos have strikethrough and muted color
- Active filter button is highlighted
- Input has focus styles
- Delete button appears on hover (or always on mobile)
- Responsive layout
- Handle potential styling errors, such as incompatible CSS rules

**Verify:**
- App is visually usable
- Styles don't break functionality
- Error handling: verify that the app handles and logs styling errors

---

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
- Handle potential testing errors, such as failed test assertions

**Verify:**
- `npx playwright test` passes
- Error handling: verify that the tests handle and log testing errors

---

### Task 12: README

Document the project.

**Do:**
- Create `README.md` with:
  - Project description
  - Setup: `npm install`
  - Development: `npm run dev`
  - Testing: `npm test` and `npx playwright test`
  - Build: `npm run build`
- Handle potential documentation errors, such as outdated instructions

**Verify:**
- README accurately describes the project
- Instructions work
- Error handling: verify that the README handles and logs documentation errors

## ⚠️ Tratamento de Exceções e Edge Cases

Durante a implementação do aplicativo, é importante tratar exceções e edge cases para garantir a robustez e a confiabilidade do sistema. Isso inclui:

* Tratamento de erros durante a configuração do projeto
* Tratamento de erros durante as operações de armazenamento
* Tratamento de erros durante a renderização de componentes
* Tratamento de erros durante a filtragem de todos
* Tratamento de erros durante a execução de testes

Além disso, é importante considerar os seguintes edge cases:

* Todos vazios
* Todos com IDs duplicados
* Todos com texto vazio
* Filtragem de todos com estado inválido
* Limpeza de todos completados com filtro ativo

Ao tratar esses exceções e edge cases, podemos garantir que o aplicativo seja robusto e confiável, e forneça uma experiência de usuário agradável e eficiente.