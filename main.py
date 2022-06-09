"""
author :admin
Date : 2021/08/09
Description :fastapi
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/my/userinfo")
async def root():
    return {"message": "Hello World"}
