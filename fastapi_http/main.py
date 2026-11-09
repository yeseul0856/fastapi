from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_home():
    return {
        "1위": "파이썬"
    }

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {
        "item_id": item_id
    }

@app.get("/items")
def read_items(item:dict):
    # DB에서 데이터를 가져오는 로직
    return {"item":item}

@app.post("/items")
def create_item(item:dict):
    # DB에 글을 작성하는 로직
    return {"item":item}

@app.put("/items/{item_id}")
def update_item(item_id:int, item:dict):
    return {
        "item_id": item_id,
        "updated_item": item
    }

@app.delete("/items/{item_id}")
def delete_item(item_id:int):
    return {
        "message": f"{item_id}는 삭제되었습니다."
    }