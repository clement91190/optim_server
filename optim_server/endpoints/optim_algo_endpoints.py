# -*-coding:Utf-8 -*
import urllib2
import json
import time
#from optim_algos.methods.interface import square_function
import numpy as np


def eval_fitness_function(tab, optim_problem="default", optim_run=0):
    """ tab is a list of parameters array"""
    ids = []
    results = []
    for params in tab:
        print params
        ids.append(send_parameters(list(params), optim_problem, optim_run))
    for id in ids:
        res = get_results(id)
        print res
        results.append(res)
    return list(np.array(results))


def get_results(id):
    url = "http://127.0.0.1:5000/get_results?id={}".format(id)
    req = urllib2.Request(url)
    res = None
    while res is None:
        f = urllib2.urlopen(req)
        res = f.read()
        res = json.loads(res)
        res = res['res']
        if res is None:
            time.sleep(0.1)
    #print "result received : ", res
    return float(res)


def send_parameters(params, optim_problem="default", optim_run=0):
    data = {'params': params, 'optim_run': optim_run, 'optim_problem': optim_problem}
    data = json.dumps(data)
    url = "http://127.0.0.1:5000/post_params"
    req = urllib2.Request(url, data, {"Content-Type": 'application/json'})
    f = urllib2.urlopen(req)
    res = f.read()
    return res


def get_run_num(optim_problem="default"):
    url = "http://127.0.0.1:5000/get_run_num?optim_problem={}".format(optim_problem)
    req = urllib2.Request(url)
    f = urllib2.urlopen(req)
    res = f.read()
    try:
        return int(res)
    except:
        return 0
 
