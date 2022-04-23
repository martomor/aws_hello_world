from fastapi import FastAPI

app = FastAPI()


@app.get('/health')
def make_request():
    return 'Hello World!'