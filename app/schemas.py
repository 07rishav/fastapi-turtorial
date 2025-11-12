from pydantic import BaseModel, EmailStr, conint
from typing import Optional, Annotated
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
     
class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True  # ✅ Updated


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        from_attributes = True  # ✅ Updated

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token : str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None

from pydantic import BaseModel, conint

class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, conint(ge=0, le=1)]  

    class Config:
        from_attributes = True

class PostVote(BaseModel):
    Post: Post
    total_vote: int

    class Config:
        from_attributes = True
