from fastapi import APIRouter
from app.api.routes.players import router as players_router
from app.api.routes.monsters import router as monsters_router


router = APIRouter()

router.include_router(players_router, prefix="/players", tags=["players"])
router.include_router(monsters_router, prefix="/monsters", tags=["monsters"])
