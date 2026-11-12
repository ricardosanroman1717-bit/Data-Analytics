# Exercise 4.B Lab 1 - Department Converter Version 2

department_code = 18

match department_code:
    case 1:
        department = "Marketing"
    case 5:
        department = "Human Resources"
    case 10:
        department = "Accounting"
    case 12:
        department = "Legal"
    case 18:
        department = "IT"
    case 20:
        department = "Customer Relations"
    case _:
        department = "Unknown Department"

print(department)