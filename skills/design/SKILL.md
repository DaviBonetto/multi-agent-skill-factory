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
*   **Erro ao salvar no localStorage**: Caso ocorra um erro ao salvar os dados no localStorage, o aplicativo deve exibir uma mensagem de erro ao usuário e tentar salvar novamente após um curto período de tempo.
*   **Erro ao carregar do localStorage**: Se ocorrer um erro ao carregar os dados do localStorage, o aplicativo deve exibir uma mensagem de erro ao usuário e inicializar com um estado vazio.
*   **Entrada inválida**: Se o usuário digitar uma entrada inválida (por exemplo, um todo vazio), o aplicativo deve exibir uma mensagem de erro e não adicionar o todo.
### Edge Cases
*   **Lista de todos vazia**: Se a lista de todos estiver vazia, o aplicativo deve exibir uma mensagem indicando que não há todos.
*   **Todos completados**: Se todos os todos estiverem completados, o aplicativo deve exibir uma mensagem indicando que não há todos ativos.
*   **Filtro**: Se o usuário aplicar um filtro e não houver todos que atendam ao filtro, o aplicativo deve exibir uma mensagem indicando que não há todos que atendam ao filtro.
*   **Tamanho máximo de todo**: O aplicativo deve ter um tamanho máximo para o texto de cada todo para evitar que o usuário insira uma grande quantidade de texto.
*   **Quantidade máxima de todos**: O aplicativo deve ter uma quantidade máxima de todos para evitar que o usuário crie uma grande quantidade de todos.
