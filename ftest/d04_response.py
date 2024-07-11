from fastapi import FastAPI, Header, Body, Form
from fastapi.responses import JSONResponse, HTMLResponse, FileResponse

app = FastAPI()


@app.get("/user")
# 返回JSON
def user():
    return JSONResponse(content={"msg": "get user"},
                        status_code=202,
                        headers={"a": "b"})


@app.get("/")
# 返回HTML
def user():
    html_content = """
    <html>
        <body><p style="color:red">Hello world</p></body>
    </html>
    """
    return HTMLResponse(content=html_content)


@app.get("/avatar")
# 返回文件（以图片为例）,访问上述网址
def user():
    avatar='static/qq.jpg'
    # return语句若有filename参数则访问网址可以下载图片，若没有则访问网址可以看到图片
    return FileResponse(avatar,filename="qq.jpg")
