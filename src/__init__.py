import logging
import os
from src.constant import LOGS_DIR, LOGS_FILE_NAME

logs_path = os.path.join(os.getcwd(), LOGS_DIR)

os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOGS_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)