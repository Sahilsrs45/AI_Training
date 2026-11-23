from fastapi import FastAPI

from router.router import router as training_router


app = FastAPI(
    title="AI Employee Training Support Assistant",
    version="1.0.0"
)


@app.get("/")
def root():

    return {
        "message": "AI Employee Training Support Assistant Running"
    }


@app.get("/health")
def health_check():

    return {
        "status": "Healthy"
    }


app.include_router(
    training_router
)