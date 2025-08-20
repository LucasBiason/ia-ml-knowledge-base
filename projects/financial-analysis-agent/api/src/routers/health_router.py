from fastapi import APIRouter
from ..models.responses import HealthResponse, RootResponse
from ..controllers.agent_controller import AgentController

router = APIRouter(tags=["Sistema"])

agent_controller = AgentController()


@router.get("/", response_model=RootResponse)
async def root():
    """Endpoint de saúde da API"""
    return RootResponse(
        message="Financial Analysis Agent API",
        status="running",
        version="1.0.0",
        docs="/docs"
    )


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """Verificação de saúde da API"""
    try:
        status = agent_controller.get_agent_status()
        return HealthResponse(**status)
    except Exception as e:
        return HealthResponse(
            status="unhealthy",
            error=str(e)
        )
