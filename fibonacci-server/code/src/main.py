import math
from fastapi import FastAPI, Query, HTTPException, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse

from src.calc import fibonacci

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


@app.get("/fib", tags=['Calculation'])
    """
    ### フィボナッチ数を返す

    - **n**: フィボナッチ数列の順番を指定する値。10以上100000未満の整数を指定する。

    ### 制約
    - 処理の制約により、リクエストが100000以下でも、結果が4300桁を超える場合はエラーとなる。
    <details>
    <summary>エラーレスポンス</summary>
    <code>
    {
    "detail": [
        {
        "msg": "The number of digits result exceeds 4300."
        }
    ]
    }
    </code>
    </details>
    """
    fib = fibonacci.fib(n)
    if fib != 0 and math.log10(fib) + 1 > 4300:
        raise TooLargeResultException(name=n)

    return {"result": fib}
