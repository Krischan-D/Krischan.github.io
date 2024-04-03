from GrossSalary import gross_salary
from SalaryDeductions import deduction
from NetSalary import net

def info():

    print("Payslip App")
    name = input("Enter Name: ")
    hour = int(input("Enter Hour: "))
    loan = int(input("Enter Loan: "))
    insurance = int(input("Enter Insurance: "))

    return name, hour, loan, insurance

def display_info(name, hour):
    print("\nEmployee Paylsip Detials")
    print("Name: " , name)
    print("Hour: " , hour)

#returned values from the info() function
employee_name, employee_hour, employee_loan, employee_insurance = info()

#invoked display function with 2 args 
display_info(employee_name, employee_hour)

#assigned variable for the return value of the gross_salary function 
gross_amount = gross_salary(employee_hour)
print("\nGross Salary: Php {:.2f}" .format(gross_amount))

#assigned variable for the return value of the deduction function 
deducted_amount = deduction(gross_amount, employee_loan, employee_insurance)

#assigned variable for the return value of the net function 
net_amount = net(gross_amount, deducted_amount)
print("Net Salary: Php", net_amount )


