from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from dotenv import load_dotenv
from src.utils import _get_uuid
from sql.db_user_info import (
    _create_user_info,
    _check_duplicate_email,
    _check_exist_email,
    _check_user_info
)
load_dotenv()

router = APIRouter(
    prefix="/api/user_info",
)

class CreateUser(BaseModel):
    email: EmailStr = "test@email.com"
    password: str = "t1234"

class JoinUser(BaseModel):
    email: EmailStr = "test@email.com"
    password: str = "t1234"

@router.post("/create_user", tags=["user_info"])
async def create_user(input: CreateUser):
    uid = _get_uuid(get_str=True)
    email = input.email
    password = input.password

    # email duplicate check
    check_duplicate_email = _check_duplicate_email(email)
    if check_duplicate_email == "fail":
        return {"status_code": 500, "detail": "Email already registered"}
    else:
        _create_user_info(uid, email, password)
        return {"detail": "Create success"}
    
@router.post("/join_user", tags=["user_info"])
async def join_user(input: JoinUser):
    email = input.email
    password = input.password
    
    # email duplicate check
    check_duplicate_email = _check_exist_email(email)
    if check_duplicate_email == "fail":
        return {"status_code": 500, "detail": "Check Email"}
    
    # check user
    response = _check_user_info(email, password)
    if response == "fail":
        return {"status_code": 500, "detail": "Check Password"}
    return response