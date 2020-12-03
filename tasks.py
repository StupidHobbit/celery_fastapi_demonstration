from time import sleep

from celery import Celery


redis_url = 'redis://localhost:6379/0'

app = Celery('tasks', broker=redis_url, backend=redis_url)


@app.task
def sleep_and_return(name: str):
    sleep(10)
    return name
