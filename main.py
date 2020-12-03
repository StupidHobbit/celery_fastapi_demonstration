import uvicorn
from fastapi import FastAPI

import tasks


app = FastAPI()


@app.get("/")
def root(name: str):
    result = tasks.sleep_and_return.delay(name)
    return {"id": result.id}


@app.get("/result")
def root(id: str):
    result = tasks.app.AsyncResult(id)
    if result.ready():
        return result.get()
    return "Not ready"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7000)
