from fastapi import FastAPI
import logging
from logging.config import dictConfig
from log_config import log_config

dictConfig(log_config)

logger = logging.getLogger('aws_hello_logger') 

app = FastAPI(info=True)

@app.get('/health')
def make_request():
    logger.info("App is ok")
    return 'Hello World!'