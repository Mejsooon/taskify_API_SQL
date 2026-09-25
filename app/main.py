from fastapi import FastAPI

from app.api.routes import auth, tasks


def create_app() -> FastAPI:
    app = FastAPI(
        title="Task Tracker API",
        description="REST API for Task Tracker",
        version="1.0.0",
    )

    app.include_router(auth.router)
    app.include_router(tasks.router)

    return app


app = create_app()


@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Task Tracker API działa",
    }