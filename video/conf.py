# coding:utf-8

import multiprocessing

bind = "0.0.0.0:8989"
workers = multiprocessing.cpu_count()
worker_class = 'gevent'
