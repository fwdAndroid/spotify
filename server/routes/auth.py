import uuid
import bcrypt
from fastapi import HTTPException, APIRouter
from models.user import User
from pydantic_schemas.user_create import UserCreate
from database import db

router = APIRouter() #use to call fast api @app methods in routes file

@router.post('/signup')
def signup_user(user: UserCreate,):
    # check if user already exists
    user_db = db.query(User).filter(User.email == user.email).first()
    if user_db:
        raise HTTPException(400, detail='User already exists')

    # hash the password (returns bytes, which fits LargeBinary)
    hashed_pw = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())

    # create new user and save in db
    user_db = User(
        id=str(uuid.uuid4()),
        name=user.name,
        email=user.email,
        password=hashed_pw,
    )
    db.add(user_db)
    db.commit()
    db.refresh(user_db)

    return user_db
