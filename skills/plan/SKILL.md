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
- Error handling: verify that the app can recover from common setup errors, such as missing dependencies or invalid template

---

### Task 2: Todo Store

Create the Svelte store for todo state management.

**Do:**
- Create `src/lib/store.ts`
- Define `Todo` interface with id, text, completed
- Create writable store with initial empty array
- Export functions: `addTodo(text)`, `toggleTodo(id)`, `deleteTodo(id)`, `clearCompleted()`
- Create `src/lib/store.test.ts` with tests for each function
- Implement error handling for store operations, such as handling duplicate todo IDs or invalid todo data

**Verify:**
- Tests pass: `npm run test` (install vitest if needed)
- Error handling: verify that the store can handle edge cases, such as adding a todo with an empty text or deleting a non-existent todo

---

### Task 3: localStorage Persistence

Add persistence layer for todos.

**Do:**
- Create `src/lib/storage.ts`
- Implement `loadTodos(): Todo[]` and `saveTodos(todos: Todo[])`
- Handle JSON parse errors gracefully (return empty array)
- Integrate with store: load on init, save on change
- Add tests for load/save/error handling
- Handle potential storage limitations, such as maximum storage size or storage quota exceeded errors

**Verify:**
- Tests pass
- Manual test: add todo, refresh page, todo persists
- Error handling: verify that the app can recover from storage-related errors, such as storage quota exceeded or JSON parse errors

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
- Handle potential input validation errors, such as empty or excessively long input

**Verify:**
- Tests pass
- Component renders input and button
- Error handling: verify that the component can handle invalid input, such as empty or excessively long text

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
- Handle potential rendering errors, such as missing or invalid todo data

**Verify:**
- Tests pass
- Component renders checkbox, text, delete button
- Error handling: verify that the component can handle edge cases, such as rendering a todo with missing or invalid data

---

### Task 6: TodoList Component

Create the list container component.

**Do:**
- Create `src/lib/TodoList.svelte`
- Props: `todos: Todo[]`
- Renders TodoItem for each todo
- Shows "No todos yet" when empty
- Add component tests
- Handle potential rendering errors, such as an empty or excessively large todo list

**Verify:**
- Tests pass
- Component renders list of TodoItems
- Error handling: verify that the component can handle edge cases, such as rendering an empty or excessively large todo list

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
- Handle potential filtering errors, such as an invalid filter state or an empty todo list

**Verify:**
- Tests pass
- Component renders count, filters, clear button
- Error handling: verify that the component can handle edge cases, such as an invalid filter state or an empty todo list

---

### Task 8: App Integration

Wire all components together in App.svelte.

**Do:**
- Import all components and store
- Add filter state (default: 'all')
- Compute filtered todos based on filter state
- Render: heading, TodoInput, TodoList, FilterBar
- Pass appropriate props to each component
- Handle potential integration errors, such as mismatched component props or invalid store data

**Verify:**
- App renders all components
- Adding todos works
- Toggling works
- Deleting works
- Error handling: verify that the app can recover from integration-related errors, such as mismatched component props or invalid store data

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
- Handle potential filtering errors, such as an invalid filter state or an empty todo list

**Verify:**
- Filter tests pass
- Manual verification of all filter states
- Error handling: verify that the app can handle edge cases, such as an invalid filter state or an empty todo list

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
- Handle potential styling errors, such as incompatible CSS selectors or invalid layout configurations

**Verify:**
- App is visually usable
- Styles don't break functionality
- Error handling: verify that the app can recover from styling-related errors, such as incompatible CSS selectors or invalid layout configurations

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
- Handle potential testing errors, such as test timeouts or invalid test data

**Verify:**
- `npx playwright test` passes
- Error handling: verify that the tests can handle edge cases, such as test timeouts or invalid test data

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
- Handle potential documentation errors, such as outdated or inaccurate information

**Verify:**
- README accurately describes the project
- Instructions work
- Error handling: verify that the README can handle edge cases, such as outdated or inaccurate information

---

### ⚠️ Tratamento de Exceções e Edge Cases

O tratamento de exceções e edge cases é fundamental para garantir a robustez e confiabilidade do aplicativo. Durante a implementação, é importante considerar os seguintes cenários:

* Erros de rede ou conexão durante a comunicação com o servidor
* Erros de validação de dados durante a entrada de dados do usuário
* Erros de renderização durante a exibição de componentes
* Erros de filtragem durante a aplicação de filtros
* Erros de persistência durante a gravação de dados

Para lidar com esses cenários, é importante implementar mecanismos de tratamento de exceções e edge cases, tais como:

* Try-catch blocks para capturar e tratar erros
* Validação de dados para garantir a consistência e validade dos dados
* Implementação de fallbacks para lidar com erros de renderização ou filtragem
* Uso de bibliotecas de logging para registrar erros e facilitar a depuração

Além disso, é importante realizar testes abrangentes para garantir que o aplicativo possa lidar com diferentes cenários e edge cases. Isso inclui testes unitários, integração e end-to-end para garantir que o aplicativo esteja funcionando corretamente em diferentes níveis.