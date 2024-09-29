// internal/config/config.go
package config

import (
    "os"
)

// Estrutura de configuração
type Config struct {
    ServerPort string
}

// LoadConfig carrega as variáveis de ambiente e retorna a configuração
func LoadConfig() (*Config, error) {
    cfg := &Config{
        ServerPort: getEnv("SERVER_PORT", "8081"),
    }
    return cfg, nil
}

// getEnv busca a variável de ambiente ou retorna um valor padrão
func getEnv(key, defaultValue string) string {
    value, exists := os.LookupEnv(key)
    if !exists {
        return defaultValue
    }
    return value
}
