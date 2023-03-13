from pydantic import BaseModel


class PetitionBase(BaseModel):
    function: str
    a: float
    b: float
    error: float