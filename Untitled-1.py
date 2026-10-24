




# Employee Payroll with Overtime

# Get employee information
employee_name = input("Enter employee name: ")
hours_worked = float(input("Enter hours worked this week: "))
hourly_rate = float(input("Enter hourly pay rate ($): "))

# Overtime settings
regular_hours = 40
overtime_multiplier = 1.5
tax_rate = 0.15  # Example tax rate of 15%

# Calculate regular and overtime pay
if hours_worked > regular_hours:
    regular_pay = regular_hours * hourly_rate
    overtime_hours = hours_worked - regular_hours
    overtime_pay = overtime_hours * hourly_rate * overtime_multiplier
else:
    regular_pay = hours_worked * hourly_rate
    overtime_hours = 0
    overtime_pay = 0

# Calculate gross pay, taxes, and net pay
gross_pay = regular_pay + overtime_pay
taxes = gross_pay * tax_rate
net_pay = gross_pay - taxes

# Display payroll report
print("\n===== EMPLOYEE PAYROLL =====")
print("Employee Name:", employee_name)
print("Regular Hours:", min(hours_worked, regular_hours))
print("Overtime Hours:", overtime_hours)
print(f"Hourly Rate: ${hourly_rate:.2f}")
print(f"Regular Pay: ${regular_pay:.2f}")
print(f"Overtime Pay: ${overtime_pay:.2f}")
print(f"Gross Pay: ${gross_pay:.2f}")
print(f"Estimated Taxes: ${taxes:.2f}")
print(f"Net Pay: ${net_pay:.2f}")





























