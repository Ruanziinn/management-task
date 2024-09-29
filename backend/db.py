# backend/db.py
import asyncpg
from config import DATABASE_URL

# Função para estabelecer a conexão com o banco de dados
async def get_db_connection():
    return await asyncpg.connect(DATABASE_URL)
