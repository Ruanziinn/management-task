// internal/handler/task_handler.go
package handler

import (
    "encoding/json"
    "fmt"
    "net/http"
    "backend-task/internal/models"
)

// TaskHandler processa as requisições de tarefas recebidas
func TaskHandler(w http.ResponseWriter, r *http.Request) {
    var task models.Task
    err := json.NewDecoder(r.Body).Decode(&task)
    if err != nil {
        http.Error(w, "Erro ao decodificar tarefa: "+err.Error(), http.StatusBadRequest)
        return
    }

    // Enviar notificação apenas se a tarefa estiver concluída
    if task.Status == "completed" {
        sendNotification(task)
    }
    w.WriteHeader(http.StatusOK)
}

// sendNotification envia uma notificação para uma tarefa concluída
func sendNotification(task models.Task) {
    fmt.Printf("A tarefa '%s' foi marcada como concluída!\n", task.Title)
}
