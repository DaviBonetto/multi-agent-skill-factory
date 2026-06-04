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
- **Tratamento de erros de localStorage**: Lidar com erros que ocorrem ao tentar salvar ou carregar dados do localStorage.
- **Prevenção de duplicatas**: Verificar se um todo com o mesmo texto já existe antes de adicioná-lo à lista.
- **Lidando com IDs inválidos**: Verificar se o ID do todo é válido antes de tentar deletá-lo ou atualizá-lo.
- **Manuseio de filtros**: Verificar se o filtro selecionado é válido antes de aplicá-lo à lista de todos.
- **Controle de concorrência**: Lidar com situações em que múltiplos usuários estão tentando atualizar a lista de todos ao mesmo tempo.
- **Tratamento de erros de renderização**: Lidar com erros que ocorrem durante a renderização da lista de todos.
- **Testes de unidade e integração**: Realizar testes para garantir que a aplicação funcione corretamente em diferentes cenários. 
Exemplos de código para tratamento de exceções e edge cases:
```typescript
// Validando entrada
if (todoText.trim() === '') {
  alert('Por favor, insira um texto para o todo');
  return;
}

// Tratando erros de localStorage
try {
  localStorage.setItem('todos', JSON.stringify(todos));
} catch (error) {
  console.error('Erro ao salvar dados no localStorage:', error);
}

// Prevenindo duplicatas
if (todos.find(todo => todo.text === todoText)) {
  alert('Todo com o mesmo texto já existe');
  return;
}
