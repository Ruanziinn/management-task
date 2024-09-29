# backend/models.py
from pydantic import BaseModel

# Modelo de dados para a tarefa
class Task(BaseModel):
    title: str
    description: str = None
    status: str = "pending"
