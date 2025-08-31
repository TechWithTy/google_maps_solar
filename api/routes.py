import logging
from typing import Dict, Any, Optional

from fastapi import APIRouter
from app.core.third_party_integrations.google_maps_solar.api.building_insights import router as building_insights_router

logger = logging.getLogger(__name__)
router = APIRouter()

# Aggregate sub-routers
router.include_router(building_insights_router)
