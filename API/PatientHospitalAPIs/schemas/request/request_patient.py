from typing import Optional
from pydantic import BaseModel, Field

class AddPatient(BaseModel):
    patient_name:str=Field(...)
    age:int=Field(...)
    blood_group:Optional[str]=None


class UpdatePatient(BaseModel):  
    patient_name: Optional[str] = Field(None)
    age: Optional[int] = Field(None)
    blood_group: Optional[str] = Field(None)