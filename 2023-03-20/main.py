def leave(tax):
    print(tax)
    exit()

def calc_tax(annual_income):
    annual_income -= 124000
    if(annual_income <= 92000):
        tax = 0
        leave(tax)
    

    elif(annual_income > 0 and annual_income <= 560000): # 5%
        tax = annual_income * 0.05
        leave(tax)
    elif(annual_income >= 560001 and annual_income <= 1260000): #12%
        tax = (annual_income - 560000) * 0.12 + 28000
        leave(tax)
    elif(annual_income >= 1260001 and annual_income <= 2520000): #20%
        tax = (annual_income - 1260000) * 0.12 + 179200
        leave(tax)
    elif(annual_income >= 2520001 and annual_income <= 4720000): #30%
        tax = (annual_income - 2520000) * 0.2 + 229600
        leave(tax)
    elif(annual_income >= 4720001): # 40%
        tax = (annual_income - 4720000) * 0.4 + 1645600
        leave(tax)

calc_tax()