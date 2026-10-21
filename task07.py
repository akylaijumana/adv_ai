import logging

logging.basicConfig(filename="app.log", level=logging.INFO)
logging.info("program started")
logging.error("something went wrong")