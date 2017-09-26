# celery_redis_sentinel_demo

Start Worker:

[mrz001@host01 ~]$ cd celery_redis_sentinel_demo1/
[mrz001@host01 celery_redis_sentinel_demo1]$ ls
celeryconfig.py  celeryconfig.pyc  tasks_one.py  tasks.py  tasks.pyc
[mrz001@host01 celery_redis_sentinel_demo1]$ celery -A tasks worker --loglevel=info
[2017-09-27 02:01:34,578: WARNING/MainProcess] /usr/lib/python2.7/site-packages/celery/apps/worker.py:161: CDeprecationWarning: 
Starting from version 3.2 Celery will refuse to accept pickle by default.

The pickle serializer is a security concern as it may give attackers
the ability to execute any command.  It's important to secure
your broker from unauthorized access when using pickle, so we think
that enabling pickle should require a deliberate action and not be
the default choice.

If you depend on pickle then you should set a setting to disable this
warning and to be sure that everything will continue working
when you upgrade to Celery 3.2::

    CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']

You must only enable the serializers that you will actually use.


  warnings.warn(CDeprecationWarning(W_PICKLE_DEPRECATED))
 
 -------------- celery@host01 v3.1.23 (Cipater)
---- **** ----- 
--- * ***  * -- Linux-3.10.0-327.el7.x86_64-x86_64-with-centos-7.2.1511-Core
-- * - **** --- 
- ** ---------- [config]
- ** ---------- .> app:         tasks:0x17b9cd0
- ** ---------- .> transport:   redis-sentinel://redis-sentinel:26379/0
- ** ---------- .> results:     redis-sentinel://redis-sentinel:26379/0
- *** --- * --- .> concurrency: 4 (prefork)
-- ******* ---- 
--- ***** ----- [queues]
 -------------- .> celery           exchange=celery(direct) key=celery
                

[tasks]
  . tasks.add

[2017-09-27 02:01:34,884: INFO/MainProcess] Connected to redis-sentinel://172.25.128.16:6379/0
[2017-09-27 02:01:34,904: INFO/MainProcess] mingle: searching for neighbors
[2017-09-27 02:01:35,916: INFO/MainProcess] mingle: all alone
[2017-09-27 02:01:35,938: WARNING/MainProcess] celery@host01 ready.


[2017-09-27 02:02:58,512: INFO/MainProcess] Received task: tasks.add[1224e204-4707-4abf-bd46-258fc8c05b13]
[2017-09-27 02:02:58,522: INFO/MainProcess] Task tasks.add[1224e204-4707-4abf-bd46-258fc8c05b13] succeeded in 0.00856882199878s: 3
[2017-09-27 02:03:56,115: INFO/MainProcess] Received task: tasks.add[2b9ba61d-2ed1-470f-827c-e88647de1294]
[2017-09-27 02:03:56,124: INFO/MainProcess] Task tasks.add[2b9ba61d-2ed1-470f-827c-e88647de1294] succeeded in 0.00659555700258s: 3


Start Client:

[mrz001@host01 ~]$ cd celery_redis_sentinel_demo1/
[mrz001@host01 celery_redis_sentinel_demo1]$ ls
celeryconfig.py  celeryconfig.pyc  tasks_one.py  tasks.py  tasks.pyc
[mrz001@host01 celery_redis_sentinel_demo1]$ python
Python 2.7.5 (default, Nov  6 2016, 00:28:07) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-11)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from tasks import add
>>> result = add.delay(1,2)
>>> result.ready()
True
>>> result.get(timeout=1)
3
>>> from celery_redis_sentinel.redis_sentinel import ensure_redis_call
>>> result1 = ensure_redis_call(add.delay, 1, 2)
>>> result1.ready()
True
>>> result1.get(timeout=1)
3





