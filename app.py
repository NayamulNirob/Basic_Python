temprature = int(input("Enter the temperature: "))
print("Temperature is:", temprature)
if temprature > 30:
    print("It's hot")
    print("Stay hydrated")
elif temprature < 20:
    print("It's cold")
    print("Wear a jacket")
elif temprature == 30:
    print("It's a warm day")
    print("Perfect for a walk")