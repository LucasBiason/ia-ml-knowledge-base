from fastapi import APIRouter, HTTPException
from ..models.requests import QuestionRequest
from ..models.responses import AnalysisResponse, ToolsResponse
from ..controllers.agent_controller import AgentController

router = APIRouter(prefix="/agent", tags=["Agente"])

agent_controller = AgentController()


@router.post("/ask", response_model=AnalysisResponse)
async def analyze_question(request: QuestionRequest):
    """Faz uma pergunta geral para o agente"""
    try:
        result = agent_controller.ask_question(request.question)

        return AnalysisResponse(
            success=True,
            data={"answer": result},
            message="Pergunta respondida com sucesso"
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/tools", response_model=ToolsResponse)
async def get_available_tools():
    """Retorna as ferramentas disponíveis"""
    try:
        tools = agent_controller.get_available_tools()
        return ToolsResponse(tools=tools)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
