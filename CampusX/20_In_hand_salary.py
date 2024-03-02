'''
Write a program that will give you the in hand salary after deduction of HRA(10%),DA(5%),PF(3%), and tax(if salary is between 5-10 lakh–10%),(11-20lakh–20%),(20< _ – 30%)(0-1lakh print k)
'''

def calculate_in_hand_salary(salary):
    hra = 0.1 * salary
    da = 0.05 * salary
    pf = 0.03 * salary

    gross_salary = salary + hra + da
    taxable_income = gross_salary - pf

    if salary <= 100000:
        tax = 0
    elif 100001 <= salary <= 500000:
        tax = 0.1 * taxable_income
    elif 500001 <= salary <= 1000000:
        tax = 0.2 * taxable_income
    else:
        tax = 0.3 * taxable_income

    in_hand_salary = gross_salary - pf - tax
    return in_hand_salary

def main():
    salary = float(input("Enter your salary: "))
    in_hand_salary = calculate_in_hand_salary(salary)
    print("Your in-hand salary after deductions is:", in_hand_salary)

if __name__ == "__main__":
    main()