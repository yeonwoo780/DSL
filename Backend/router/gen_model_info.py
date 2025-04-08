from fastapi import APIRouter
from pydantic import BaseModel
from dotenv import load_dotenv
from sql.db_gen_model_info import (
    _check_exist_gen_model,
    _insert_gen_model_info,
    _search_gen_model_info
)
from src.gen_model import _setting_gen_model
load_dotenv()

router = APIRouter(
    prefix="/api/gen_model_info",
)

class GenModelInfo(BaseModel):
    provide: str = "openai"

@router.post("/insert_gen_model_info", tags=["gen_model_info"])
async def insert_gen_model_info(input: GenModelInfo):
    provide = input.provide

    try:
        g_model_name = _setting_gen_model(provide)
    except:
        return {"status_code": 500, "detail": "No support"}
    check_exist_gen_model = _check_exist_gen_model(g_model_name)
    if check_exist_gen_model == "fail":
        return {"status_code": 500, "detail": "model already registered"}
    else:
        _insert_gen_model_info(g_model_name)
        return {"detail": "Insert success"}
    
@router.post("/search_gen_model_info", tags=["gen_model_info"])
async def search_gen_model_info():
    response = _search_gen_model_info()
    return response