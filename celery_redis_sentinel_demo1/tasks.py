# tasks.py
from celery_redis_sentinel import register
from celery import Celery
from celery_redis_sentinel.task import EnsuredRedisTask

# has to be called before creating celery app
register()

app = Celery('tasks',backend='redis://172.25.128.16/5', broker='redis://172.25.128.16/5')
#app = Celery('tasks')
#app.config_from_object('celeryconfig')

app.conf.BROKER_URL = 'redis-sentinel://redis-sentinel:26379/0'
app.conf['BROKER_TRANSPORT_OPTIONS'] = {
    'sentinels': [('172.25.128.16', 26379),
                  ('172.25.128.16', 26380),
                  ('172.25.128.16', 26381)],
    'service_name': 'mymaster',
    'socket_timeout': 0.1,
}
app.conf['CELERY_RESULT_BACKEND'] = app.conf['BROKER_URL']
app.conf['CELERY_RESULT_BACKEND_TRANSPORT_OPTIONS'] = app.conf['BROKER_TRANSPORT_OPTIONS']
app.conf['CELERY_TASK_RESULT_EXPIRES'] = 60*60*1
app.conf['CELERY_RESULT_SERIALIZER'] = 'json'

@app.task(base=EnsuredRedisTask)
def add(a, b):
    return a + b
