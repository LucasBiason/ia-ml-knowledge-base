from fastapi import APIRouter, HTTPException
from ..models.requests import StockAnalysisRequest
from ..models.responses import AnalysisResponse
from ..controllers.analysis_controller import AnalysisController

router = APIRouter(prefix="/analyze", tags=["Análise Financeira"])

analysis_controller = AnalysisController()


@router.post("/fundamental", response_model=AnalysisResponse)
async def analyze_fundamental(request: StockAnalysisRequest):
    """Análise fundamentalista de uma ação"""
    try:
        result = analysis_controller.analyze_fundamental(
            request.ticker,
            request.analysis_type
        )

        if result["status"] == "success":
            return AnalysisResponse(
                success=True,
                data=result,
                message="Análise fundamentalista concluída com sucesso"
            )
        else:
            return AnalysisResponse(
                success=False,
                error=result.get("error", "Erro desconhecido"),
                message="Falha na análise fundamentalista"
            )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/technical", response_model=AnalysisResponse)
async def analyze_technical(request: StockAnalysisRequest):
    """Análise técnica de uma ação"""
    try:
        result = analysis_controller.analyze_technical(request.ticker)

        if result["status"] == "success":
            return AnalysisResponse(
                success=True,
                data=result,
                message="Análise técnica concluída com sucesso"
            )
        else:
            return AnalysisResponse(
                success=False,
                error=result.get("error", "Erro desconhecido"),
                message="Falha na análise técnica"
            )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/risk", response_model=AnalysisResponse)
async def analyze_risk(request: StockAnalysisRequest):
    """Análise de risco de uma ação"""
    try:
        result = analysis_controller.analyze_risk(
            request.ticker,
            request.company_info or ""
        )

        if result["status"] == "success":
            return AnalysisResponse(
                success=True,
                data=result,
                message="Análise de risco concluída com sucesso"
            )
        else:
            return AnalysisResponse(
                success=False,
                error=result.get("error", "Erro desconhecido"),
                message="Falha na análise de risco"
            )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/comprehensive", response_model=AnalysisResponse)
async def analyze_comprehensive(request: StockAnalysisRequest):
    """Análise completa de uma ação"""
    try:
        result = analysis_controller.analyze_comprehensive(request.ticker)

        if result["status"] == "success":
            return AnalysisResponse(
                success=True,
                data=result,
                message="Análise completa concluída com sucesso"
            )
        else:
            return AnalysisResponse(
                success=False,
                error=result.get("error", "Erro desconhecido"),
                message="Falha na análise completa"
            )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
