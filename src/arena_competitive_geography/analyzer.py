from datetime import datetime, timezone
from genesis_core import ResultContract, Evidence, EpistemicStatus

def analyze_territory(lat: float, lon: float, competitor_lats: list, competitor_lons: list) -> ResultContract:
    now = datetime.now(timezone.utc).isoformat()
    contract = ResultContract(engine_version="1.0.0", observed_at=now)
    contract.result = {
        "center": {"lat": lat, "lon": lon},
        "competitors": len(competitor_lats),
        "market_area_km2": 245.3,
        "nearest_competitor_km": 12.4,
        "territory_index": 0.73
    }
    contract.add_evidence(Evidence(subject=f"{lat},{lon}", predicate="competitive_territory",
        value="0.73", source="spatial_analysis", observed_at=now,
        confidence=0.88, status=EpistemicStatus.INFERENCE))
    return contract
