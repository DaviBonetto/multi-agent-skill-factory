# Svelte Todo List - Design
## Overview
A simple todo list application built with Svelte. Supports creating, completing, and deleting todos with localStorage persistence.
## Features
- Add new todos
- Mark todos as complete/incomplete
- Delete todos
- Filter by: All / Active / Completed
- Clear all completed todos
- Persist to localStorage
- Show count of remaining items
## User Interface
```
┌─────────────────────────────────────────┐
│  Svelte Todos                           │
├─────────────────────────────────────────┤
│  [________________________] [Add]       │
├─────────────────────────────────────────┤
│  [ ] Buy groceries                  [x] │
│  [✓] Walk the dog                   [x] │
│  [ ] Write code                     [x] │
├─────────────────────────────────────────┤
│  2 items left                           │
│  [All] [Active] [Completed]  [Clear ✓]  │
└─────────────────────────────────────────┘
```
## Components
```
src/
  App.svelte           # Main app, state management
  lib/
    TodoInput.svelte   # Text input + Add button
    TodoList.svelte    # List container
    TodoItem.svelte    # Single todo with checkbox, text, delete
    FilterBar.svelte   # Filter buttons + clear completed
    store.ts           # Svelte store for todos
    storage.ts         # localStorage persistence
```
## Data Model
```typescript
interface Todo {
  id: string;        // UUID
  text: string;      // Todo text
  completed: boolean;
}
type Filter = 'all' | 'active' | 'completed';
```
## Acceptance Criteria
1. Can add a todo by typing and pressing Enter or clicking Add
2. Can toggle todo completion by clicking checkbox
3. Can delete a todo by clicking X button
4. Filter buttons show correct subset of todos
5. "X items left" shows count of incomplete todos
6. "Clear completed" removes all completed todos
7. Todos persist across page refresh (localStorage)
8. Empty state shows helpful message
9. All tests pass
## ⚠️ Tratamento de Exceções e Edge Cases
### Exceções
*   **Erro ao salvar no localStorage**: Em caso de erro ao salvar os dados no localStorage, o aplicativo deve exibir uma mensagem de erro ao usuário e tentar salvar novamente após um tempo determinado.
*   **Erro ao carregar do localStorage**: Em caso de erro ao carregar os dados do localStorage, o aplicativo deve exibir uma mensagem de erro ao usuário e inicializar com um estado vazio.
*   **Erro ao adicionar todo**: Em caso de erro ao adicionar um novo todo, o aplicativo deve exibir uma mensagem de erro ao usuário e não adicionar o todo.
### Edge Cases
*   **Todos vazios**: Quando não há todos, o aplicativo deve exibir uma mensagem indicando que não há todos.
*   **Todos com texto vazio**: O aplicativo não deve permitir que o usuário adicione um todo com texto vazio.
*   **Todos com texto muito longo**: O aplicativo deve limitar o tamanho do texto do todo para evitar que o usuário insira texto muito longo.
*   **Filtro com todos vazios**: Quando o usuário seleciona um filtro e não há todos que atendam ao critério de filtro, o aplicativo deve exibir uma mensagem indicando que não há todos que atendam ao critério de filtro.
*   **Clear completed com todos vazios**: Quando o usuário clica no botão "Clear completed" e não há todos completos, o aplicativo não deve fazer nada.
*   **Todos com id duplicado**: O aplicativo deve garantir que não haja dois ou mais todos com o mesmo id.
*   **Todos com data de criação ou atualização inválida**: O aplicativo deve garantir que as datas de criação e atualização dos todos sejam válidas e não causem erros ao serem processadas.