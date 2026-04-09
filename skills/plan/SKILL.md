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
- Handle potential errors during installation and setup

**Verify:**
- `npm run dev` starts server
- App shows minimal "Svelte Todos" heading
- `npm run build` succeeds
- Error handling: verify that the app can recover from common errors such as network issues or dependency installation failures

---

### Task 2: Todo Store

Create the Svelte store for todo state management.

**Do:**
- Create `src/lib/store.ts`
- Define `Todo` interface with id, text, completed
- Create writable store with initial empty array
- Export functions: `addTodo(text)`, `toggleTodo(id)`, `deleteTodo(id)`, `clearCompleted()`
- Create `src/lib/store.test.ts` with tests for each function
- Implement error handling for store operations (e.g., handling duplicate todo IDs)

**Verify:**
- Tests pass: `npm run test` (install vitest if needed)
- Error handling: verify that store operations handle errors correctly (e.g., duplicate IDs, invalid input)

---

### Task 3: localStorage Persistence

Add persistence layer for todos.

**Do:**
- Create `src/lib/storage.ts`
- Implement `loadTodos(): Todo[]` and `saveTodos(todos: Todo[])`
- Handle JSON parse errors gracefully (return empty array)
- Integrate with store: load on init, save on change
- Add tests for load/save/error handling
- Implement error handling for storage operations (e.g., handling storage quota exceeded errors)

**Verify:**
- Tests pass
- Manual test: add todo, refresh page, todo persists
- Error handling: verify that storage operations handle errors correctly (e.g., storage quota exceeded, JSON parse errors)

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
- Implement error handling for input validation (e.g., handling empty input)

**Verify:**
- Tests pass
- Component renders input and button
- Error handling: verify that input validation handles errors correctly (e.g., empty input)

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
- Implement error handling for todo item rendering (e.g., handling missing todo data)

**Verify:**
- Tests pass
- Component renders checkbox, text, delete button
- Error handling: verify that todo item rendering handles errors correctly (e.g., missing todo data)

---

### Task 6: TodoList Component

Create the list container component.

**Do:**
- Create `src/lib/TodoList.svelte`
- Props: `todos: Todo[]`
- Renders TodoItem for each todo
- Shows "No todos yet" when empty
- Add component tests
- Implement error handling for list rendering (e.g., handling empty list)

**Verify:**
- Tests pass
- Component renders list of TodoItems
- Error handling: verify that list rendering handles errors correctly (e.g., empty list)

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
- Implement error handling for filter rendering (e.g., handling invalid filter state)

**Verify:**
- Tests pass
- Component renders count, filters, clear button
- Error handling: verify that filter rendering handles errors correctly (e.g., invalid filter state)

---

### Task 8: App Integration

Wire all components together in App.svelte.

**Do:**
- Import all components and store
- Add filter state (default: 'all')
- Compute filtered todos based on filter state
- Render: heading, TodoInput, TodoList, FilterBar
- Pass appropriate props to each component
- Implement error handling for app integration (e.g., handling missing components)

**Verify:**
- App renders all components
- Adding todos works
- Toggling works
- Deleting works
- Error handling: verify that app integration handles errors correctly (e.g., missing components)

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
- Implement error handling for filter functionality (e.g., handling invalid filter state)

**Verify:**
- Filter tests pass
- Manual verification of all filter states
- Error handling: verify that filter functionality handles errors correctly (e.g., invalid filter state)

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
- Implement error handling for styling issues (e.g., handling CSS syntax errors)

**Verify:**
- App is visually usable
- Styles don't break functionality
- Error handling: verify that styling issues handle errors correctly (e.g., CSS syntax errors)

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
- Implement error handling for end-to-end tests (e.g., handling test failures)

**Verify:**
- `npx playwright test` passes
- Error handling: verify that end-to-end tests handle errors correctly (e.g., test failures)

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
- Implement error handling for README documentation (e.g., handling invalid Markdown syntax)

**Verify:**
- README accurately describes the project
- Instructions work
- Error handling: verify that README documentation handles errors correctly (e.g., invalid Markdown syntax)

---

### ⚠️ Tratamento de Exceções e Edge Cases

Implementar tratamento de exceções e edge cases para garantir a robustez e confiabilidade do aplicativo.

**Do:**
- Implementar tratamento de exceções para cada componente e função
- Testar edge cases para garantir que o aplicativo funcione corretamente em diferentes cenários
- Implementar logging e monitoramento para detectar e resolver problemas

**Verify:**
- O aplicativo funciona corretamente em diferentes cenários
- Exceções são tratadas e logadas corretamente
- Edge cases são testados e funcionam como esperado

---

### Edge Cases e Exceções Específicas

- **TodoItem**: lidar com casos em que o todo não tem texto ou ID
- **TodoList**: lidar com casos em que a lista de todos está vazia
- **FilterBar**: lidar com casos em que o filtro está inválido ou não está definido
- **App**: lidar com casos em que o aplicativo não consegue carregar ou renderizar corretamente

**Do:**
- Implementar tratamento de exceções para cada um desses casos
- Testar esses casos para garantir que o aplicativo funcione corretamente

**Verify:**
- O aplicativo funciona corretamente em cada um desses casos
- Exceções são tratadas e logadas corretamente