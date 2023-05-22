import os
from pathlib import Path

CELERY_DIR = os.environ.get("CELERY_DIR", "/tmp/monitoring_system/celery")
CELERY_DIR_PATH = Path(CELERY_DIR)
DB_CONNECTION_STRING = "postgresql://guest:guest@postgres:5432/monitoring_system"
