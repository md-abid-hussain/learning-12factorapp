from fastapi import FastAPI
from fastapi.responses import HTMLResponse

import uvicorn

app = FastAPI()

@app.get('/',response_class=HTMLResponse)
def greeting():
    return "<h1>Hello world</h1>"

@app.get('/{name}',response_class=HTMLResponse)
def greet_person(name:str):
    return f"<h1>Hello {name.capitalize()}</h1>"

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info", reload=True)