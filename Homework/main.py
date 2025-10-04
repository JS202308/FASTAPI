from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import uvicorn
import json

app = FastAPI()


users = []


@app.post("/users")
def add_user(name: str):
    if name in users:
        raise HTTPException(status_code=400, detail="Це ім'я вже існує!")
    users.append(name)
    return {"message": f"Ім'я '{name}' додано успішно."}



@app.get("/users")
def get_users():
    return JSONResponse(content={"users": users})


@app.delete("/users/{name}")
def delete_user(name: str):
    if name not in users:
        raise HTTPException(status_code=404, detail="Такого імені немає!")
    users.remove(name)
    return {"message": f"Ім'я '{name}' успішно видалено."}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

