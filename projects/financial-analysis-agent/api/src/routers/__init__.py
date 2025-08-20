from .health_router import router as health_router
from .analysis_router import router as analysis_router
from .agent_router import router as agent_router

__all__ = [
    "health_router",
    "analysis_router", 
    "agent_router"
]
