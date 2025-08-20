from pydantic import BaseModel
from typing import Optional, Dict, Any

class AnalysisResponse(BaseModel):
    """Modelo para resposta de análise"""
    success: bool
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    message: str

class HealthResponse(BaseModel):
    """Modelo para resposta de saúde da API"""
    status: str
    agent: Optional[str] = None
    error: Optional[str] = None

class RootResponse(BaseModel):
    """Modelo para resposta da raiz da API"""
    message: str
    status: str
    version: str
    docs: str

class ToolsResponse(BaseModel):
    """Modelo para resposta de ferramentas disponíveis"""
    tools: list
