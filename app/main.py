from fastapi import FastAPI


app = FastAPI(
    title="Task Tracker API",
    description="REST API for Task Tracker",
    version="1.0.0",
)


@app.get("/")
def root():
    return {"message": "Task Tracker API działa"}