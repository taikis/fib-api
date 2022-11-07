# Fibonacci数列API

## How to debelop

1. `make up`
1. `make shell`
1. `cd src`
1. `uvicorn main:app --reload --host 0.0.0.0 --port 8080`
1. `http://0.0.0.0:8080/fib?n=1`へアクセス
1. 下記が表示されればOK

```json
{
  "result": 1
}
```

## 仕様

### 使用方法

[ドキュメント](https://fib-api.taikis.jp/docs)を参照  

### 構成

- Python 3.11
- FastAPI
- Docker
- pytest(UT用)

### 動作環境

- GCP Cloud Run

### 処理の流れ

- FastAPIによりGETリクエストの受け取り
- 値に対する各種バリデーションを行う
  - 0以上
  - 整数値
  - 結果が4300桁以下(後述)
- 実際の計算は`sympy.fibonacci`関数が行う

### 各種制約

- 処理結果が4300桁以下
  - 一定以上のバージョンのPythonは4300桁以上の文字列↔︎整数変換ができない
  - これについては[Qiita記事](https://qiita.com/taikis/items/1b6925088b15892b212c)で解説した
- リクエストが99999以下
  - 実際の処理部分は上記影響を受けず、計算が行われる
  - 今後のPythonの改善によって、文字列↔︎整数変換ができるようになった場合、サーバーの処理速度を考えた制限を加えたいため