from arena_competitive_geography.analyzer import analyze_territory

def test_analyze_territory():
    c = analyze_territory(43.6047, 1.4442, [43.7, 43.5], [1.5, 1.3])
    assert "market_influence_area_km2" in c.result
    assert c.confidence > 0.8
