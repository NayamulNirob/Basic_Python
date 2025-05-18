# temperature = int(input('Enter the temperature: '))
# print("Temperature is:", temperature)
# if temperature > 30:
#     print("It's hot")
#     print("Stay hydrated")
# elif temperature < 20:
#     print("It's cold")
#     print("Wear a jacket")
# elif temperature == 30:
#     print("It's a warm day")
#     print("Perfect for a walk")
# print("Have a great day!")
from pyexpat.errors import messages

age=int(input("Enter your age:"))
if age < 18:
    messages = "You are a minor."
elif 18 <= age < 65:
    messages = "You are an adult."
else:
    messages = "You are a senior citizen."
print("Thank you."+messages)

# age = int(input("Enter your age: "))

