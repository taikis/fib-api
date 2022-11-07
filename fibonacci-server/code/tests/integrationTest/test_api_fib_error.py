from urllib import response
from src.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

# 異常系テスト

# 上限越え

def test_get_fib_99999():
    response = client.get("/fib?n=99999")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "msg": f"The number of digits result exceeds 4300.",
            }
        ]
    }

def test_get_fib_100000():
    response = client.get("/fib?n=100000")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["query", "n"],
                "msg": "ensure this value is less than 100000",
                "type": "value_error.number.not_lt",
                "ctx": {"limit_value": 100000},
            }
        ]
    }

# 異常クエリ


def test_get_fib_bad_query():
    response = client.get("/fib?n=abc")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["query", "n"],
                "msg": "value is not a valid integer",
                "type": "type_error.integer",
            }
        ]
    }


def test_get_fib_bad_query():
    response = client.get("/fib?n=abc")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["query", "n"],
                "msg": "value is not a valid integer",
                "type": "type_error.integer",
            }
        ]
    }


def test_get_fib_negative():
    response = client.get("/fib?n=-1")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["query", "n"],
                "msg": "ensure this value is greater than or equal to 0",
                "type": "value_error.number.not_ge",
                "ctx": {"limit_value": 0},
            }
        ]
    }
