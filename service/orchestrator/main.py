import environ
from celery import Celery
from loguru import logger
import json

env = environ.Env(
    AMQP_HOST_STRING=(str, "")
)

celery_worker = Celery(
    'orchestrator',
    broker=env("AMQP_HOST_STRING"),
    backend='rpc://'
)
celery_queue = "orchestrator"


@celery_worker.task(queue=celery_queue)
def hello_world():
    logger.info("Another hard day of work...")
    logger.info("If only i have good models for doing my job")
