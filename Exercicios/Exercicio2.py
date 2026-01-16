#Given a user's year of birth, calculate their age
#Ask their birth year in the terminal

from datetime import datetime

birth_year = int(input("What year were you born?"))
anniversary = bool(int(input("Have you had a birthday this year? 0 - NO 1 - YES ")))
#print(anniversary)

current_year = datetime.now().year

age = current_year - birth_year

if not anniversary:
    age -= 1

solution = f"You have {age} years old."

print(solution)
