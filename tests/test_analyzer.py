# test de l'analyse d'emprise géographique Arena
from arena_competitive_geography.analyzer import analyze_territory

def test_analyze_territory():
    contract = analyze_territory(48.8566, 2.3522)
    assert contract is not None
    assert contract.result["territory_dominance_index"] > 0
    assert len(contract.evidence) >= 1
