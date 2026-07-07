from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = "CNNClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]

for file in list_of_files:
    filepath = Path(file)

    filepath.parent.mkdir(parents=True, exist_ok=True)

    if not filepath.exists():
        filepath.touch()
        logging.info(f"Created: {filepath}")
    else:
        logging.info(f"Already exists: {filepath}")