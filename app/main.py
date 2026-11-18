from fastapi import FastAPI

app = FastAPI(title="Python Actions CI/CD")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello from Python Actions CI/CD"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
