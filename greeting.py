name = input("What is your name? ")
birth_year = input("What is your birth year? ")

print(f"Hello {name}")

from datetime import datetime 
current_year = datetime.now().year
age = current_year - int(birth_year)
print(f"You must be {age} years old")

print("Goodbye!")