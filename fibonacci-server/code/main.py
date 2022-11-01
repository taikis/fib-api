import math
from fastapi import FastAPI, Query, HTTPException, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse

from calc import fibonacci

app = FastAPI()


class TooLargeResultException(Exception):
    def __init__(self, name):
        self.name = name


@app.exception_handler(TooLargeResultException)
def TooLargeResult_exception_handler(request: Request, exc: TooLargeResultException):
    return JSONResponse(
        status_code=400,
        content={
            "detail": [
                {
                    "msg": f"The number of digits result exceeds 4300.",
                }
            ]
        },
    )


@app.get("/fib")
def read_item(n: int = Query(gt=0)):
    fib = fibonacci.fib(n)
    if math.log10(fib) + 1 > 4300:
        raise TooLargeResultException(name=n)

    return {"result": fib}
