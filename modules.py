from pydantic import BaseModel
class story_books(BaseModel):
    id : int
    name : str
    copies : int
