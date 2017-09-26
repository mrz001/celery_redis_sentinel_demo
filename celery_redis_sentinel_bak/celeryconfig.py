# celeryconfig.py
BROKER_URL = 'redis-sentinel://redis-sentinel:26379/0'
BROKER_TRANSPORT_OPTIONS = {
    'sentinels': [('172.25.128.16', 26379),
                  ('172.25.128.16', 26380),
                  ('172.25.128.16', 26381)],
    'service_name': 'mymaster',
    'socket_timeout': 0.1,
}

CELERY_RESULT_BACKEND = 'redis-sentinel://redis-sentinel:26379/0'
CELERY_RESULT_BACKEND_TRANSPORT_OPTIONS = BROKER_TRANSPORT_OPTIONS

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
CELERY_TIMEZONE = 'Europe/Oslo'
CELERY_ENABLE_UTC = True
CELERY_TASK_RESULT_EXPIRES = 60*60*1
