# -*-coding:Utf-8 -*
import urllib2
import json
import time
import numpy as np


def get_task(optim_problem="default"):
    url = "http://127.0.0.1:5000/get_params?optim_problem={}".format(optim_problem)
    req = urllib2.Request(url)
    res = None
    while res is None:
        f = urllib2.urlopen(req)
        res = f.read()
        res = json.loads(res)
        if res is None:
            time.sleep(0.1)
    return (res['_id']['$oid'],  np.array(res['params'], dtype='float32'))


def send_results(id, score):
    url = "http://127.0.0.1:5000/post_results?id={}&res={}".format(id, score)
    req = urllib2.Request(url)
    f = urllib2.urlopen(req)
    f.read()
