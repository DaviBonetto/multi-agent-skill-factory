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
- **Validação de entrada**: Verificar se o texto do todo é vazio ou contém apenas espaços em branco antes de adicioná-lo à lista.
- **Tratamento de erros de localStorage**: Implementar um mecanismo para lidar com erros ao ler ou gravar dados no localStorage, como exibir uma mensagem de erro ao usuário.
- **Prevenção de duplicatas**: Verificar se um todo com o mesmo texto já existe na lista antes de adicioná-lo.
- **Lidando com IDs únicos**: Garantir que os IDs dos todos sejam únicos, mesmo após a exclusão de itens.
- **Filtro de itens**: Implementar um filtro para evitar que itens vazios ou nulos sejam exibidos na lista.
- **Segurança**: Proteger a aplicação contra ataques de injeção de código malicioso, como o XSS, ao exibir o texto dos todos.
- **Compatibilidade com navegadores**: Testar a aplicação em diferentes navegadores e versões para garantir a compatibilidade.
- **Acessibilidade**: Garantir que a aplicação seja acessível para usuários com deficiências, seguindo as diretrizes de acessibilidade web.
- **Desempenho**: Otimizar a aplicação para garantir um desempenho rápido e eficiente, mesmo com uma grande quantidade de itens na lista.