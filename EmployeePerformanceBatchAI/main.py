from fastapi import FastAPI

from routers.employee_router import router

app = FastAPI(
    title="Employee Performance Batch AI"
)

app.include_router(router)