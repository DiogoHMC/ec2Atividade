# Importa o FastAPI, a classe Request e a classe HTTPException
from fastapi import FastAPI, Request, HTTPException

# Cria a instância da aplicação FastAPI
app = FastAPI()

# Define o endpoint para a rota /auth/me
@app.post("/auth/me")
async def auth_me(request: Request):
    """
    Endpoint para autenticação.
    
    Recebe um POST request.
    Verifica se o header 'x-user' está presente para obter o nome do usuário.
    Retorna um JSON com o nome do usuário e um ping/pong.
    """
    # Tenta obter o nome de usuário do header 'x-user'
    # Esta é uma forma simples de simular um usuário, o correto seria usar tokens de autenticação
    user_header = request.headers.get("x-user")
    
    if not user_header:
        # Se o header 'x-user' não for enviado, retorna um erro 400 Bad Request
        raise HTTPException(
            status_code=400, 
            detail="Header 'x-user' não encontrado na requisição. Por favor, inclua seu nome de usuário no header."
        )

    # Retorna o JSON com o nome do usuário e a mensagem de ping/pong
    return {"user": user_header, "ping": "pong"}
