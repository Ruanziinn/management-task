// cmd/main.go
package main

import (
    "fmt"
    "net/http"
    "backend-task/internal/config"
    "backend-task/internal/handler"
)

func main() {
    // Carregar a configuração do ambiente
    cfg, err := config.LoadConfig()
    if err != nil {
        fmt.Printf("Erro ao carregar configuração: %s\n", err)
        return
    }

    // Inicializa as rotas e o servidor
    http.HandleFunc("/process-task", handler.TaskHandler)
    fmt.Printf("Iniciando serviço de tarefas no Golang na porta %s...\n", cfg.ServerPort)
    http.ListenAndServe(":"+cfg.ServerPort, nil)
}
