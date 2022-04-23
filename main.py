from fastapi import FastAPI

app = FastAPI(docs_url='/')


@app.get('/health')
def make_request():
    return 'Hello World!'