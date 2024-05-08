#Jeffrey Linney
#April 6,2024
#P4HWK2
#Branching - Salary Homework

num_employee = 0
total_reg_pay = 0
total_ot_pay = 0


employee_name = input("Enter employee's name: ")


while employee_name != "Done":

    num_employee = num_employee + 1
    hours = float(input('Enter number of hours worked: '))
    pay_rate = float(input('Enter employee rate of pay: '))

    if hours <= 40:
        regular_hours = hours
        overtime_hours = 0

    else: # Hours is greater than 40
        regular_hours = 40
        overtime_hours = hours - 40
        print()
    reg_pay = regular_hours * pay_rate 
    ot_pay = overtime_hours * pay_rate * 1.5
    total_reg_pay +=reg_pay
    total_ot_pay +=ot_pay
    total_grosspay = total_reg_pay + total_ot_pay
    
    print("Employee Name:", employee_name )
    print()
    print(f"{'Hours Worked':<20}{'Pay Rate':<14}{'OverTime':<15}{'OverTime Pay':<17}{'RegHour Pay':<23}{'Gross Pay':<16}")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    print(f"{hours:<20}{pay_rate:<14}{overtime_hours:<15}{ot_pay:<17}${reg_pay:<23}${reg_pay + ot_pay:<16}")      
    employee_name = input("Enter employee's name: ")

print(f"Total number of employees entered: {num_employee}")
print(f"Total amount paid for overtime: {ot_pay}")
print(f"Total amount paid for regular hours: {reg_pay}")
print(f"Total amount paid in gross: {total_grosspay}")

