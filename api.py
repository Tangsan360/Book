from fastapi import FastAPI
from modules import story_books

app = FastAPI()

story_book =[
    story_books(id=1,name="Beauty and the beast",copies=11),
    story_books(id=2,name="Romeo and Julliet",copies=12)
]
@app.get("/story_books")
async def read():
    return story_book