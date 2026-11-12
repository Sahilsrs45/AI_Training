
import logging
import os

# Create logs directory if it does not exist
os.makedirs("logs", exist_ok=True)

# Create application logger
logger = logging.getLogger("training_feedback_api")

# Set logging level
logger.setLevel(logging.INFO)

# Prevent duplicate log messages
logger.propagate = False

# Avoid adding handlers multiple times
if not logger.handlers:

    # Log format
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    # File handler: writes logs to logs/app.log
    file_handler = logging.FileHandler(
        "logs/app.log",
        encoding="utf-8"
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # Console handler: displays logs in terminal
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # Attach handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
