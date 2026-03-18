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
- **Validação de entrada**: Verificar se o texto do todo é vazio antes de adicioná-lo. Se estiver vazio, exibir uma mensagem de erro.
- **Tratamento de erros de localStorage**: Caso ocorra um erro ao salvar ou carregar os todos do localStorage, exibir uma mensagem de erro e continuar com a aplicação.
- **Prevenção de duplicatas**: Verificar se um todo com o mesmo texto já existe antes de adicioná-lo. Se existir, não adicionar o novo todo.
- **Limite de tamanho de texto**: Limitar o tamanho do texto do todo a 100 caracteres. Se o texto for maior, truncá-lo e exibir uma mensagem de aviso.
- **Tratamento de erros de UUID**: Caso ocorra um erro ao gerar um UUID para um todo, usar um identificador temporário e exibir uma mensagem de erro.
- **Prevenção de exclusão acidental**: Exibir uma confirmação antes de excluir um todo para evitar exclusões acidentais.
- **Tratamento de erros de filtro**: Caso ocorra um erro ao aplicar um filtro, exibir uma mensagem de erro e continuar com a aplicação.
- **Prevenção de sobrecarga de memoria**: Limitar a quantidade de todos armazenados no localStorage para evitar sobrecarga de memória. Se o limite for atingido, exibir uma mensagem de aviso e parar de armazenar novos todos.