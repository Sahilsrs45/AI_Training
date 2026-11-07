import logging
import os
 
# step 1: create log directory
os.makedirs("logs",exist_ok=True)
 
# step 2: configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log"),
        logging.StreamHandler()
    ]
)
 
# step 3: create logger
logger=logging.getLogger("CoforgeCustomerAPI")