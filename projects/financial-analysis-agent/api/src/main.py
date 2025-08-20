"""
Aplicação principal da API Financial Analysis Agent.

Este módulo configura e inicializa a aplicação FastAPI,
incluindo middlewares, routers e configurações de CORS.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import analysis_router, agent_router, health_router

# Configuração da aplicação FastAPI
app = FastAPI(
    title="Financial Analysis Agent API",
    description="API para análise financeira de ações usando IA",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configuração de CORS para permitir requisições do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, especificar origens permitidas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusão dos routers da aplicação
app.include_router(health_router)
app.include_router(analysis_router)
app.include_router(agent_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
