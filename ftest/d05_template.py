from fastapi import FastAPI, Request
# 引入模板引擎
from fastapi.templating import Jinja2Templates

app = FastAPI()
template = Jinja2Templates("pages")  # 参数是HTML文档的存放位置


@app.get("/")
# 返回HTML，动态变化的数据
def user(username, req: Request):
    return template.TemplateResponse("index.html", context={"request": req, "name": username})
