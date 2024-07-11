from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
template = Jinja2Templates("pages")  # 参数是HTML文档的存放位置

todos = ["写日记", "看电影", "玩游戏"]

@app.get("/")
def index(req: Request):
    # 通过模板引擎在html文件中编写**类似**于python的代码
    return template.TemplateResponse("index.html", context={"request": req, "todos": todos})


@app.post("/todo")
def todo(todo=Form(None)):
    """处理用户发送过来的todolist数据"""
    todos.insert(0,todo)
    return RedirectResponse("/",status_code=302)
