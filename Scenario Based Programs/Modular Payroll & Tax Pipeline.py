"""Modular Payroll & Tax Pipeline
Task: Build calc_gross, calc_deductions, and generate_payslip"""


def calc_gross(basic, allowance_list):
    gross = basic + sum(allowance_list)
    return gross


def calc_deductions(basic, pf_percentage, flat_prof_tax=200):
    deductions = (basic * pf_percentage) + flat_prof_tax
    return deductions


def generate_payslip(emp_name, basic, allowance_list, pf_percentage):
    gross = calc_gross(basic, allowance_list)
    deductions = calc_deductions(basic, pf_percentage)
    final_sal = gross - deductions
    return f"Employee: {emp_name} | Gross: Rs.{gross} | Deductions: Rs.{deductions} | Salary: Rs.{final_sal}"


entry = True
while entry:
    emp_name = input("Enter name of employee: ")
    basic = float(input("Enter basic salary: "))
    allowance = list(
        map(float, input("Enter Allowances seperated by spaces: ").split())
    )
    pf_percentage = float(input("Enter provident fund percentage: "))
    print(f"\t{generate_payslip(emp_name, basic, allowance, pf_percentage)}")
    ch = input("\nDo you want to continue [y/n]: ")
    if ch == "n":
        entry = False
