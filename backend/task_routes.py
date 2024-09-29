# backend/task_routes.py
from fastapi import APIRouter, HTTPException
from models import Task
from db import get_db_connection
import httpx

# Criação do router
router = APIRouter()

# Rota para criar uma nova tarefa
@router.post("/tasks/create")
async def create_task(task: Task):
    conn = await get_db_connection()
    query = """INSERT INTO tasks (title, description, status) VALUES ($1, $2, $3) RETURNING id;"""
    task_id = await conn.fetchval(query, task.title, task.description, task.status)
    await conn.close()

    # Enviar a tarefa para o serviço Golang
    #try:
    #    async with httpx.AsyncClient() as client:
    #        response = await client.post("http://localhost:8081/process-task", json={"id": task_id, **task.model_dump()})
    #        if response.status_code != 200:
    #            raise HTTPException(status_code=500, detail="Erro ao comunicar com o microserviço Golang")
    #except Exception as e:
    #    raise HTTPException(status_code=500, detail=f"Erro ao enviar notificação ao Golang: {str(e)}")

    return {"id": task_id, **task.model_dump()}

# Rota para listar todas as tarefas
@router.get("/tasks/list")
async def read_tasks():
    conn = await get_db_connection()
    tasks = await conn.fetch("SELECT * FROM tasks;")
    await conn.close()
    return tasks

# Rota para atualizar o status de uma tarefa
@router.put("/tasks/update/{task_id}")
async def update_task(task_id: int, status: str):
    conn = await get_db_connection()
    result = await conn.execute("UPDATE tasks SET status=$1, updated_at=NOW() WHERE id=$2;", status, task_id)
    await conn.close()
    if result == "UPDATE 0":
        raise HTTPException(status_code=404, detail="Task not found")
    return {"status": "success", "updated_id": task_id}

# Rota para deletar uma tarefa
@router.delete("/tasks/delete/{task_id}")
async def delete_task(task_id: int):
    conn = await get_db_connection()
    result = await conn.execute("DELETE FROM tasks WHERE id=$1;", task_id)
    await conn.close()
    if result == "DELETE 0":
        raise HTTPException(status_code=404, detail="Task not found")
    return {"status": "success", "deleted_id": task_id}
