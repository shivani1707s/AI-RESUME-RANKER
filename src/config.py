from pathlib import Path

# Root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data directory
DATA_DIR = PROJECT_ROOT / "data"

# File paths
CANDIDATES_FILE = DATA_DIR / "candidates.jsonl"
JOB_DESCRIPTION_FILE = DATA_DIR / "job_description.docx"
SCHEMA_FILE = DATA_DIR / "candidate_schema.json"
SIGNALS_DOC = DATA_DIR / "redrob_signals_doc.docx"
SAMPLE_SUBMISSION = DATA_DIR / "sample_submission.csv"

# Output directories
OUTPUT_DIR = PROJECT_ROOT / "outputs"
EMBEDDINGS_DIR = PROJECT_ROOT / "embeddings"
MODELS_DIR = PROJECT_ROOT / "models"

# Create directories if they don't exist
OUTPUT_DIR.mkdir(exist_ok=True)
EMBEDDINGS_DIR.mkdir(exist_ok=True)
MODELS_DIR.mkdir(exist_ok=True)