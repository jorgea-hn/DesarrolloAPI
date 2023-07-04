from typing import Any

from pydantic import BaseModel
from pydantic import validator
from pydantic.utils import GetterDict

from peewee import ModelSelect

class PeeweeGetterDict(GetterDict):
    def get(self,key:Any,default:Any=None):
        res = getattr(self._obj, key,default)
        if isinstance(res,ModelSelect):
            return list(res)
        return res


class UserRequestModel(BaseModel):
    username:str
    password:str


    @validator("username")
    def username_validator(cls,username):
        if len(username) < 3 or len(username) >50:
            raise ValueError("La longitud debe encontrarse entre 3 y 50 caracteres.")
        
        return username
    

class UserResponseModel(BaseModel):
    id:int
    username:str

    class Config:
        orm_mode = True
        getter_dict=PeeweeGetterDict