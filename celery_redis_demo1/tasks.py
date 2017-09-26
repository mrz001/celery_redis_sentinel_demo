from celery import Celery

app = Celery('tasks', backend='redis://172.25.128.16', broker='redis://172.25.128.16')

@app.task
def add(x, y):
    return x + y
