from fastapi import FastAPI

from router.router import router


app = FastAPI(
    title="AI Retail Customer Query Assistant"
)


@app.get("/")
def root():

    return {
        "message": "Welcome to AI Retail Customer Query Assistant"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


app.include_router(router)