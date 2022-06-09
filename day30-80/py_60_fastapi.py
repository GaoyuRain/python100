"""
author :admin
Date : 2021/08/09
Description :  fastapi
启动 uvicorn 命令：
uvicorn main:app --reload
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}




