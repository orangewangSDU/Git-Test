from fastapi import FastAPI, Header, Body, Form

app = FastAPI()


@app.get("/user")
# 变化的参数传入函数
def user(id, token=Header(None)):
    return {"id": id, "token": token}


@app.post("/login")
def login(username=Form(None), password=Form(None)):
    return {"data": {"username": username, "password": password}}
