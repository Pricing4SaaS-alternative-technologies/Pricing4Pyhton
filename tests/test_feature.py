from app.models.feature import Feature

def test_feature():
    f = Feature("color", "red")
    assert f.name == "color"
    assert f.value == "red"
