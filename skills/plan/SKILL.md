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
- Test for potential setup issues, such as missing dependencies or incorrect configuration

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
- Test for edge cases, such as adding a todo with an empty text or deleting a non-existent todo

---

### Task 3: localStorage Persistence

Add persistence layer for todos.

**Do:**
- Create `src/lib/storage.ts`
- Implement `loadTodos(): Todo[]` and `saveTodos(todos: Todo[])`
- Handle JSON parse errors gracefully (return empty array)
- Integrate with store: load on init, save on change
- Add tests for load/save/error handling
- Handle potential storage limitations, such as exceeding the maximum storage size

**Verify:**
- Tests pass
- Manual test: add todo, refresh page, todo persists
- Test for storage-related edge cases, such as storing a large number of todos

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
- Handle potential input-related issues, such as handling non-string input or extremely long input

**Verify:**
- Tests pass
- Component renders input and button
- Test for input-related edge cases, such as adding a todo with a very long text

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
- Handle potential todo item-related issues, such as handling a todo item with a missing ID

**Verify:**
- Tests pass
- Component renders checkbox, text, delete button
- Test for todo item-related edge cases, such as deleting a todo item with a missing ID

---

### Task 6: TodoList Component

Create the list container component.

**Do:**
- Create `src/lib/TodoList.svelte`
- Props: `todos: Todo[]`
- Renders TodoItem for each todo
- Shows "No todos yet" when empty
- Add component tests
- Handle potential list-related issues, such as handling an empty list or a list with a very large number of items

**Verify:**
- Tests pass
- Component renders list of TodoItems
- Test for list-related edge cases, such as rendering a list with a very large number of items

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
- Handle potential filter-related issues, such as handling a filter change when there are no todos

**Verify:**
- Tests pass
- Component renders count, filters, clear button
- Test for filter-related edge cases, such as filtering a list with no todos

---

### Task 8: App Integration

Wire all components together in App.svelte.

**Do:**
- Import all components and store
- Add filter state (default: 'all')
- Compute filtered todos based on filter state
- Render: heading, TodoInput, TodoList, FilterBar
- Pass appropriate props to each component
- Handle potential integration-related issues, such as handling a mismatch between the filter state and the rendered todos

**Verify:**
- App renders all components
- Adding todos works
- Toggling works
- Deleting works
- Test for integration-related edge cases, such as adding a todo while the filter is set to "Completed"

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
- Handle potential filter functionality-related issues, such as handling a filter change when there are no todos

**Verify:**
- Filter tests pass
- Manual verification of all filter states
- Test for filter functionality-related edge cases, such as filtering a list with no todos

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
- Handle potential styling-related issues, such as handling a mismatch between the design mockup and the actual styling

**Verify:**
- App is visually usable
- Styles don't break functionality
- Test for styling-related edge cases, such as styling a list with a very large number of items

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
- Handle potential end-to-end testing-related issues, such as handling a test failure due to a network issue

**Verify:**
- `npx playwright test` passes
- Test for end-to-end testing-related edge cases, such as testing a user flow with a very large number of todos

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
- Handle potential documentation-related issues, such as handling a mismatch between the documentation and the actual project setup

**Verify:**
- README accurately describes the project
- Instructions work
- Test for documentation-related edge cases, such as documenting a project with a very complex setup

---

## ⚠️ Tratamento de Exceções e Edge Cases

Este projeto deve ser capaz de lidar com uma variedade de exceções e edge cases, incluindo:

*   Erros de rede durante a inicialização do projeto
*   Incompatibilidade de dependências durante a instalação
*   Erros de parse de JSON durante a carga de dados
*   Exceções durante a execução de testes
*   Erros de estilo e layout durante a renderização da aplicação
*   Comportamento inesperado durante a interação do usuário

Para lidar com esses casos, o projeto deve incluir:

*   Tratamento de erros robusto em todas as etapas do projeto
*   Testes abrangentes para garantir que o projeto funcione corretamente em diferentes cenários
*   Documentação clara e concisa para ajudar os desenvolvedores a entender como o projeto funciona e como lidar com exceções
*   Implementação de padrões de design e boas práticas para garantir que o projeto seja escalável e mantenha a qualidade ao longo do tempo.