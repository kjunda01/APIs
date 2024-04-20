from fastapi import FastAPI

app = FastAPI()

@app.get("/api/usuarios")
async def ObterUsuarios():
    return "Este são os usuários"

