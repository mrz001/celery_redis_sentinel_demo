# tasks.py
from celery_redis_sentinel import register
from celery import Celery
from celery_redis_sentinel.task import EnsuredRedisTask

# has to be called before creating celery app
register()

app = Celery('tasks',backend='redis-sentinel://172.25.128.16:26379/')
#app.config_from_object('celeryconfig')

@app.task(base=EnsuredRedisTask)
def add(a, b):
    return a + b
