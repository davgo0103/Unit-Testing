import tax
def test_5(): # 1 ~ 560000 = Annual_income * 0.05
    val = 560000
    result = tax.calc_tax(val)
    assert result == 21800
def test_12(): # 1 ~ 560000 = (Annual_income - 560000) * 0.12 + 28000
    val = 560000
    result = tax.calc_tax(val)
    assert result == 21800
def test_20(): # 1 ~ 560000 = (Annual_income - 1260000) * 0.20 + 179200
    val = 560000
    result = tax.calc_tax(val)
    assert result == 21800
def test_30(): # 1 ~ 560000 = (Annual_income - 2520000) * 0.30 + 229600
    val = 560000
    result = tax.calc_tax(val)
    assert result == 21800
def test_40(): # 1 ~ 560000 = (nnual_income - 4720000) * 0.40 + 1645600
    val = 560000
    result = tax.calc_tax(val)
    assert result == 21800
