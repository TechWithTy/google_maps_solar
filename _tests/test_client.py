from backend.app.core.third_party_integrations.google_maps_solar.client import GoogleMapsSolarClient


class _Resp:
    def __init__(self, status=200, json_data=None):
        self.status_code = status
        self._json = json_data if json_data is not None else {"ok": True}

    def raise_for_status(self):
        if self.status_code >= 400:
            raise Exception(f"HTTP {self.status_code}")

    def json(self):
        return self._json


def test_building_insights_find_closest(monkeypatch):
    client = GoogleMapsSolarClient(api_key="k")

    def fake_post(url, json=None, params=None, timeout=None):
        assert url == "https://solar.googleapis.com/v1/buildingInsights:findClosest"
        assert params and params.get("key") == "k"
        assert isinstance(json, dict) and "location" in json
        return _Resp(json_data={"buildingInsights": {"status": "OK"}})

    monkeypatch.setattr(
        "backend.app.core.third_party_integrations.google_maps_solar.client.requests.post",
        fake_post,
    )

    out = client.building_insights_find_closest(body={"location": {"latitude": 1.0, "longitude": 2.0}})
    assert out["buildingInsights"]["status"] == "OK"
