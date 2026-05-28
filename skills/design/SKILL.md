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
- **Tratamento de erros de localStorage**: Lidar com erros que ocorrem ao tentar acessar ou manipular o localStorage.
- **Edge case: lista vazia**: Exibir uma mensagem útil quando a lista de todos estiver vazia.
- **Edge case: muitos todos**: Implementar uma solução para lidar com uma grande quantidade de todos, como paginação ou carregamento lento.
- **Segurança**: Proteger contra ataques de injeção de scripts maliciosos ao exibir o texto dos todos.
- **Acessibilidade**: Garantir que a aplicação seja acessível para usuários com deficiência, seguindo as diretrizes de acessibilidade web.
- **Testes**: Implementar testes unitários e de integração para garantir que a aplicação funcione corretamente em diferentes cenários.
- **Manuseio de erros de rede**: Lidar com erros de rede que possam ocorrer ao tentar carregar ou salvar dados.
- **Compatibilidade com diferentes navegadores**: Garantir que a aplicação seja compatível com diferentes navegadores e versões.
