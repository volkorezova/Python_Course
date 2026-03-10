# Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json.
# результат для невалідного файлу виведіть через логер на рівні еррору
# файл json__<your_second_name>.log

import json
import logging
from pathlib import Path

# logger
logging.basicConfig(
    filename="json__volkorezova.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

folder = Path(".")
for file in Path(".").glob("*.json"):
    try:
        with open(file, "r", encoding="utf-8") as f:
            json.load(f)
    except json.JSONDecodeError as e:
        logger.error(f"{file.name} is invalid JSON: {e}")