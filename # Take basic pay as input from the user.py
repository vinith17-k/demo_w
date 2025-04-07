# Take basic pay as input from the user
basic_pay = float(input("Enter the basic pay of the employee: "))
# Calculate HRA (10% of Basic Pay)
HRA = 0.10 * basic_pay
# Calculate TA (5% of Basic Pay)
TA = 0.05 * basic_pay
# Calculate Gross Salary
gross_salary = basic_pay + HRA + TA
# Calculate Professional Tax (2% of Gross Salary)
professional_tax = 0.02 * gross_salary
# Calculate Net Salary after deductions
net_salary = gross_salary - professional_tax
# Output the results
print(f"\nBasic Pay: {basic_pay}")
print(f"HRA (10% of Basic Pay): {HRA}")
print(f"TA (5% of Basic Pay): {TA}")
print(f"Gross Salary: {gross_salary}")
print(f"Professional Tax (2% of Gross Salary): {professional_tax}")
print(f"Net Salary: {net_salary}")
print("name= abhijeet ingale")
print("roll no= 1721")