# Celery on Windows 10

---

| Tool    | version  |
| ------- | -------- |
| Celery  | 4.3.0    |
| Windows | 10(1803) |
| gevent  | 1.4.0    |

---

## Why using gevent?

On Windows, Celery with version over 4.0 does not work well with multi process, so using gevent instead. [See from stackoverflow](https://stackoverflow.com/questions/45744992/celery-raises-valueerror-not-enough-values-to-unpack)

---

## Basic Usage

1. run `pipenv install --dev`, to install all relative packages
2. install redis or rabbitMQ as worker.
3. install database such as redis, mySql as backend.
4. run `celery -A tasks worker --loglevel=info -P gevent`.
5. run `trigger.py`.
6. result will be saved in worker(`redis`).
