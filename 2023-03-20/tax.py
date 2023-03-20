def calc_tax(annual_income):
    annual_income -= (124000 + 92000)
    if(annual_income < 0):
        return 0
    

    elif(annual_income > 0 and annual_income <= 560000): # 5%
        tax = annual_income * 0.05
        return tax
    elif(annual_income >= 560001 and annual_income <= 1260000): #12%
        tax = (annual_income - 560000) * 0.12 + 28000
        return tax
    elif(annual_income >= 1260001 and annual_income <= 2520000): #20%
        tax = (annual_income - 1260000) * 0.20 + 179200
        return tax
    elif(annual_income >= 2520001 and annual_income <= 4720000): #30%
        tax = (annual_income - 2520000) * 0.30 + 229600
        return tax
    elif(annual_income >= 4720001): # 40%
        tax = (annual_income - 4720000) * 0.40 + 1645600
        return tax
