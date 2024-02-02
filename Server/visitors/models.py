from pydantic import BaseModel


class Visitors(BaseModel):
    id: int
    name: str
    surname: str
    middle_name: str
    ticket_number: int
    ticket_price: int
    seat_number: int

class New_visitor(BaseModel):
    name: str
    surname: str
    middle_name: str
    ticket_number: int
    ticket_price: int
    seat_number: int

class Certain_visitor(BaseModel):
    id: int
    name: str
    surname: str
    seat_number: int


class Update_visitor(BaseModel):
    name: str
    surnane: str
    middle_name: str


