from backend.app.core.third_party_integrations.google_maps_solar.client import GoogleMapsSolarClient

def test_health():
    client = GoogleMapsSolarClient(api_key="test")
    assert client.health() is True
