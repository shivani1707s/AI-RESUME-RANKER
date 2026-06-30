from docx import Document
from src.utils.config import (
    PROJECT_ROOT,
    DATA_DIR,
    JOB_DESCRIPTION_FILE,
)

from src.utils.config import JOB_DESCRIPTION_FILE


def read_job_description():
    print("PROJECT_ROOT:", PROJECT_ROOT)
    print("DATA_DIR:", DATA_DIR)
    print("JOB_DESCRIPTION_FILE:", JOB_DESCRIPTION_FILE)
    print("Exists:", JOB_DESCRIPTION_FILE.exists())

    document = Document(str(JOB_DESCRIPTION_FILE))

    text = []

    for paragraph in document.paragraphs:
        text.append(paragraph.text)

    return "\n".join(text)


if __name__ == "__main__":

    print(read_job_description())