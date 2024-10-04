import logging
import os
import sys

LOG_LEVEL = logging.INFO

root_logger = logging.getLogger()
root_logger.setLevel(LOG_LEVEL)

handler = handler = logging.StreamHandler(sys.stdout)
handler.setLevel(LOG_LEVEL)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

root_logger.addHandler(handler)

BOT_TOKEN = os.getenv("BOT_TOKEN")
