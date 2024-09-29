# backend/main.py
from fastapi import FastAPI
from task_routes import router  # Importa as rotas de tarefas

app = FastAPI()

# Inclui as rotas de tarefas
app.include_router(router)

# Mensagem de verificação de saúde da API
@app.get("/")
async def root():
    return {"message": "API de gerenciamento de tarefas está funcionando!"}

