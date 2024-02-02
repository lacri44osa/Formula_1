from pydantic import BaseModel

class Violators(BaseModel):
    id: int
    visiotr_id: int

class New_violator(BaseModel):
    id: int
    visiotr_id: int



