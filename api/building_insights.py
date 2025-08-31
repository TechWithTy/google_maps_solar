import logging
from typing import Dict, Any, Optional

from fastapi import APIRouter

from app.core.third_party_integrations.google_maps_solar.client import (
    GoogleMapsSolarClient,
)

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/solar", tags=["google_maps_solar-building_insights"])


# Utility

def find_closest_util(body: Dict[str, Any], key: Optional[str]) -> Dict:
    client = GoogleMapsSolarClient(api_key=key)
    return client.building_insights_find_closest(body=body)


# Routes
@router.post("/building-insights/find-closest")
async def building_insights_find_closest(body: Dict[str, Any], key: Optional[str] = None) -> Dict:
    return find_closest_util(body, key)
