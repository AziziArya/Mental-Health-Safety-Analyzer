import logging
import os
from datetime import datetime

# =====================================
# Log Directory
# =====================================

LOG_DIR = "logs"


if not os.path.exists(LOG_DIR):

    os.makedirs(LOG_DIR)


# =====================================
# Log File
# =====================================

LOG_FILE = os.path.join(LOG_DIR, f"system_{datetime.utcnow().strftime('%Y%m%d')}.log")


# =====================================
# Logger Configuration
# =====================================


def create_logger(name: str = "mental_health_system"):

    logger = logging.getLogger(name)

    logger.setLevel(logging.INFO)

    if logger.handlers:

        return logger

    # File Handler

    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")

    file_handler.setLevel(logging.INFO)

    # Console Handler

    console_handler = logging.StreamHandler()

    console_handler.setLevel(logging.INFO)

    # Format

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler.setFormatter(formatter)

    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.addHandler(console_handler)

    return logger


# =====================================
# Global Logger
# =====================================

logger = create_logger()


# =====================================
# Helper Functions
# =====================================


def log_info(message: str):

    logger.info(message)


def log_warning(message: str):

    logger.warning(message)


def log_error(message: str, error: Exception = None):

    if error:

        logger.error(f"{message} | Error: {str(error)}")

    else:

        logger.error(message)


def log_exception(message: str):

    logger.exception(message)
