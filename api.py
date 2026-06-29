from fastapi import FastAPI

app = FastAPI()
@app.get("/pages/{page_id}")
async def read(page_id:int):
    return{"pages_id":page_id} 