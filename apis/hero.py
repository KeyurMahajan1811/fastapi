from fastapi import FastAPI
import json

app = FastAPI()
HERO = {}
with open('mockdata\superhero.json') as file:
    HERO = json.load(file)

print(HERO)

@app.get("/heros")
async def get_all_hero():
    return HERO