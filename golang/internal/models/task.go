// internal/models/task.go
package models

// Estrutura que representa uma tarefa
type Task struct {
    ID          int    `json:"id"`
    Title       string `json:"title"`
    Description string `json:"description"`
    Status      string `json:"status"`
}
