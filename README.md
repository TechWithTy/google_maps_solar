# Google Maps Solar SDK (skeleton)

Minimal placeholder; add usage examples after full implementation.

## Quick start

```python
from backend.app.core.third_party_integrations.google_maps_solar.client import GoogleMapsSolarClient

client = GoogleMapsSolarClient(api_key="YOUR_API_KEY")
assert client.health() is True
```

Note: This is a stub client intended to be expanded with real API calls as per Google Maps Solar API docs.

## Environment

- GOOGLE_MAPS_API_KEY
- SOLAR_BASE_URL (default: https://solar.googleapis.com)
- SOLAR_TIMEOUT (default: 15)

## References

- Google Maps Solar API: https://developers.google.com/maps/documentation/solar/overview
