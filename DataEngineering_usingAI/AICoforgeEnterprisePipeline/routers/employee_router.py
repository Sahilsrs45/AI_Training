from fastapi import APIRouter, HTTPException
 
from services.etl_service import (run_etl, department_summary)
 
router = APIRouter(
    prefix="/employees",
    tags=["Employee Data Engineering"]
)
 
 
@router.post("/etl")
def execute_etl():
    try:
        return run_etl()
    except Exception as err:
        raise HTTPException(
            status_code=500,
            detail=str(err)
        )
 
 
@router.get("/departments")
def get_department_summary():
    return department_summary()
 