import datetime as dt
import pydantic as _pydantic
from pydantic import Field
from uuid import UUID
from typing import List, Optional



class _UserBase(_pydantic.BaseModel):
    email: str

class UserUpdate(_UserBase):
    first_name: str
    last_name: str
    phone_number: str


class UserPasswordUpdate(_pydantic.BaseModel):
    password: str


class UserCreate(_UserBase):
    password: str
    first_name: Optional[str]
    last_name: Optional[str]
    phone_number: Optional[str]
    country_code: Optional[str] 
    image: Optional[str] 
    device_id: Optional[str] 
    country: Optional[str]
    state: Optional[str]
    google_id: Optional[str]
    google_image: Optional[str] 

    class Config:
        orm_mode = True
    

class UserLogin(_UserBase):
    password: str



class Token(_UserBase):
    access_token: str
    token_type: str


class TokenData(_UserBase):
    id: Optional[str] = None


class User(_UserBase):
    id: str
    first_name: Optional[str]
    last_name: Optional[str]
    phone_number: str
    is_active: bool
    is_verified: bool
    is_superuser: bool
    country_code: Optional[str]
    image: Optional[str] 
    is_deleted: bool
    device_id: Optional[str] 
    country: Optional[str]
    state: Optional[str]
    google_id: Optional[str]
    google_image: Optional[str] 
    date_created: dt.datetime
    last_updated: dt.datetime 

    class Config:
        orm_mode = True

