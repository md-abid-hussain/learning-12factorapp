from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from redis import Redis
import uvicorn
from config import settings

app = FastAPI()
redis = Redis(host=settings.redis_host, port=settings.redis_port)


@app.get('/', response_class=HTMLResponse)
def greeting() -> HTMLResponse:
    '''
        Greet the world
    '''
    redis.incr("visitorCount")
    visit_count = str(redis.get('visitorCount'), 'utf-8')
    html_response = f"""
                        <h1>Hello world</h1>
                        <h2>Total visitor : {visit_count}</h2>
                    """
    return html_response


@app.get('/{name}', response_class=HTMLResponse)
def greet_person(name: str) -> HTMLResponse:
    '''
        Greet incoming user
    '''
    return f"<h1>Hello {name.capitalize()}</h1>"


if __name__ == "__main__":
    uvicorn.run("main:app", port=settings.server_port,
                log_level="info", reload=True)
