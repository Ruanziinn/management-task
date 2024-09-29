# backend/config.py
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:pass@localhost/taskdb")
