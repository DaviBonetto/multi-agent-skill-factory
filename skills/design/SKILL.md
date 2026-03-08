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
- **Validação de entrada**: Verificar se o texto do todo é vazio antes de adicioná-lo à lista.
- **Tratamento de erros de armazenamento**: Lidar com erros que ocorrem ao salvar ou carregar dados do localStorage.
- **Prevenção de duplicatas**: Verificar se um todo com o mesmo texto já existe antes de adicioná-lo à lista.
- **Limite de tamanho da lista**: Definir um limite para o número de todos que podem ser adicionados à lista.
- **Tratamento de erros de filtro**: Lidar com erros que ocorrem ao filtrar a lista de todos.
- **Prevenção de exclusão acidental**: Solicitar confirmação antes de excluir um todo.
- **Tratamento de erros de inicialização**: Lidar com erros que ocorrem ao inicializar a aplicação, como falhas ao carregar dados do localStorage.
- **Segurança**: Validar e sanitizar todos os dados de entrada para prevenir ataques de injeção de código malicioso.
- **Acessibilidade**: Garantir que a aplicação seja acessível para usuários com deficiência, seguindo as diretrizes de acessibilidade web.
- **Testes**: Realizar testes unitários e de integração para garantir que a aplicação funcione corretamente em diferentes cenários.