import tax
def test_5(): # 1 ~ 560000 = Annual_income * 0.05
    val = 560000
    result = tax.calc_tax(val)
    assert result == 21800
def test_12(): # 560,001 ~ 1,260,000 = (Annual_income - 560000) * 0.12 + 28000
    val = 700000
    result = tax.calc_tax(val)
    assert result == 29920
def test_20(): # 1,260,001 ~ 2,520,000 = (Annual_income - 1260000) * 0.20 + 179200
    val = 2560000
    result = tax.calc_tax(val)
    assert result == 414400
def test_30(): # 2,520,001 ~ 4,720,000 = (Annual_income - 2520000) * 0.30 + 229600
    val = 560000
    result = tax.calc_tax(val)
    assert result == 21800
def test_40(): # > 4,720,001 = (Annual_income - 4720000) * 0.40 + 1645600
    val = 5000000
    result = tax.calc_tax(val)
    assert result == 1708000