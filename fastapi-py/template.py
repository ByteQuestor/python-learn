#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：fastapi-py 
@File    ：template.py
@Author  ：【闲鱼】：混吃等死真君
@Date    ：2024/11/27 16:04 
'''
from fastapi import FastAPI
import uvicorn
import docker

app = FastAPI()
cli = docker.from_env()


@app.get("/containers")
def list_containers():
    result = []
    for x in cli.containers.list():
        item = dict()
        item['Id'] = x.attrs['Id']
        item['Name'] = x.attrs['Name']
        item['Created'] = x.attrs['Created']
        result.append(item)

    return {"result": result}


@app.get("/images")
def list_images():
    result = []
    for x in cli.images.list():
        result.append(x.attrs)

    return {"result": result}


@app.get("/images/{image_id}")
def list_images(image_id):
    print(image_id)

    if image_id == '':
        return {"result": []}

    result = []
    for x in cli.images.list():
        if x.attrs['Id'].startswith(image_id):
            result.append(x.attrs)
    return {"result": result}


@app.post('/container')
def create_container(container):
    cli.run(container['image'], container['command'], detach=True, environment=container['environment'])


uvicorn.run(app, host="0.0.0.0", port=8000)
