import logging
import os
import sys

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
handler = handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
LOGGER.addHandler(handler)

BOT_TOKEN = os.getenv("BOT_TOKEN")
