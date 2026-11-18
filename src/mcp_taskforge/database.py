import sqlite3
from pathlib import Path



project_root = Path(__file__).resolve().parents[2]
data_dir = project_root / "data"
db_path = data_dir / "tasks.db"

def init_db() -> None:
    data_dir.mkdir(parents = "True", exist_ok = "True")
    conn = sqlite3.connect(db_path)
    
