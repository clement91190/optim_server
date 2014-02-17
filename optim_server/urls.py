# -*-coding:Utf-8 -*
from flask import request
from optim_server import app
from optim_server.db import models

import json


# Worker functions
@app.route('/get_params', methods=['GET'])
def get_params():
    optim_problem = request.args.get('optim_problem')
    try:
        obj = models.ParamInstance.objects(assigned=False, done=False, optim_problem=optim_problem).order_by('id')
        obj = obj[0]
        obj.assigned = True
        obj.save()
        return obj.to_json()
    except:
        return json.dumps(None)


@app.route('/post_results', methods=['GET'])
def post_results():
    try:
        res = request.args.get('res')
        id = request.args.get('id')
        res = float(res)
        obj = models.ParamInstance.objects.get(id=id)
        obj.done = True
        obj.assigned = False
        obj.score = res
        obj.save()
        return json.dumps(None)
    except:
        return json.dumps(None)


#TaskManager urls
@app.route('/post_params', methods=['POST'])
def post_params():
    req_json = request.get_json()
    print req_json
    data = req_json
    params = data['params']
    try:
        optim_problem = data['optim_problem']
    except:
        optim_problem = "default"
    try:
        optim_run = int(data['optim_run'])
    except:
        optim_run = 0
    params = [float(p) for p in params]
    obj = models.ParamInstance(params=params, done=False, assigned=False, optim_run=optim_run, optim_problem=optim_problem)
    obj.save()
    return str(obj.id)


@app.route('/get_results', methods=['GET'])
def get_results():
    """ return the result -> return None if no results. """
    id = request.args.get('id')
    obj = models.ParamInstance.objects.get(id=id)
    #return obj.to_json()
    return json.dumps({'res': obj.score})


@app.route('/get_run_num', methods=['GET'])
def get_run_num():
    """ return the first available value for a run on a given problem"""
    try:
        optim_problem = request.args.get('optim_problem')
    except:
        optim_problem = "default"
    try:
        obj = models.ParamInstance.objects(optim_problem=optim_problem).sort('-optim_run').first()
        return str(obj.optim_run)
    except:
        return str(0)


