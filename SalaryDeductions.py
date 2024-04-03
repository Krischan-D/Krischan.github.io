
def deduction(gross, loan, insurance):
    tax = 0.12 
    tax_amount = tax * gross
    total_deduction = (tax_amount + loan + insurance) 
    print("\nTax: Php", tax_amount)
    print("Loan: Php {:.2f}".format(loan))
    print("Insurance: Php {:.2f}".format(insurance))
    print("\nTotal Deductions: Php", total_deduction)
    return total_deduction

