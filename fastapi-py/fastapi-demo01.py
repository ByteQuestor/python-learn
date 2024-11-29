#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：fastapi-py 
@File    ：fastapi-demo01.py
@Author  ：【闲鱼】：混吃等死真君
@Date    ：2024/11/27 16:09 
'''

from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()


@app.get("/")
def home():
    return {"wzy": "22"}


@app.get("/app/{page}")
def page(page):
    return {"wzy": int(page) * 2}


@app.post("/items/")
async def create_item(request: Request):
    # 在这里处理POST请求，比如获取请求体中的数据
    data = await request.json()
    print(f'{data["name"]}.yaml')
    return {"message": "Item created successfully", "data": data}


uvicorn.run(app, host="0.0.0.0", port=80)
