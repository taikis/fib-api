from fastapi import FastAPI
import fibonacci

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/fib")
def read_item(n: int = None):
    return {"result": fibonacci.fib(n)}