import os
from typing import Any, Dict, Optional

import requests


class GoogleMapsSolarClient:
    """
    Google Maps Solar API client.
    Docs: https://developers.google.com/maps/documentation/solar

    Service endpoint: https://solar.googleapis.com

    Key methods (examples):
      - buildingInsights.findClosest
    """

    def __init__(self, api_key: Optional[str] = None, timeout: int = 30):
        self.api_key = api_key or os.getenv("GOOGLE_MAPS_API_KEY")
        self.base_url = "https://solar.googleapis.com"
        self.timeout = timeout

    def _inject_key(self, params: Optional[Dict[str, Any]]) -> Dict[str, Any]:
        q: Dict[str, Any] = dict(params or {})
        if self.api_key and "key" not in q:
            q["key"] = self.api_key
        return q

    def building_insights_find_closest(self, *, body: Dict[str, Any], params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        POST {base}/v1/buildingInsights:findClosest
        Body per docs, e.g. location { latitude, longitude }
        """
        url = f"{self.base_url}/v1/buildingInsights:findClosest"
        resp = requests.post(url, json=body, params=self._inject_key(params), timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()

    def health(self) -> bool:
        return bool(self.api_key)
