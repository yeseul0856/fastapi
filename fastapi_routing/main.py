from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "hello" : "World"
    }

@app.get("/items/{item}")
def read_items(item):
    return {"item_id": item}

# 경로 파라미터
@app.get("/users/{user_id}/items/{item_id}")
def read_user_item(user_id, item_id):
    return {
        "user_id": user_id,
        "item_id": item_id
    }

 
@app.get("/items")
def read_item(skip, limit):
    return {
        "skip": skip,
        "limit": limit
    }

# 이게 왜 필요하냐? 인크루트에 프론트에서 요청한 페이지가 60번이라고 백엔드에서 받았어
# 그럼 백엔드가 60에 해당하는 값을 가져온 다음에 인쿠르트에 뿌려줘야 한다 (같은 ui에 프론트가
# 어떻게 요청하는지에 따라서 데이터만 달라진다)
# https://search.incruit.com/list/search.asp?col=job&kw=%c6%c4%c0%cc%bd%e3&startno=30
# https://search.incruit.com/list/search.asp?col=job&kw=%c6%c4%c0%cc%bd%e3&startno=60
# 마지막 숫자가 30이면 데이터가 취업정보를 30개 불러오고 (1페이지)
# 마지막 숫자가 60이면 데이터가 취업정로를 60개 불러온다 (2페이지)