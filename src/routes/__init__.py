from fastapi import APIRouter

from models.models import IntersectionCalcRequest, IntersectionCalcResponse

main_router = APIRouter(prefix="/nodal", tags=["NodalAnalysis"])


@main_router.post("/calc", response_model=IntersectionCalcResponse)
async def my_profile(data: IntersectionCalcRequest):
    """
    Эндпоинт для выполнения Узлового Анализа
    """
    # Функция для выполнения узлового анализа
    from calculations.nodal import calc_nodal

    return calc_nodal(data.vlp.dict(), data.ipr.dict())
