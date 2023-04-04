import time

from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


# Shared task allows code execution async, task is used for scheduled tasks
@shared_task
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True


@shared_task
def sample_task():
    logger.info("This is a scheduled task.")
    logger.info("The sample task just ran.")
    return True
