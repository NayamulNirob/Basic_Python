import math

course = "Python for Beginners"
print(course[0:6])
print(course[7:10])
print(len(course))

first_name = "John"
last_name = "Doe"
full_name = f"{first_name} {last_name}"
print(full_name)

abs(-2.9)
print(abs(-2.9))
print(round(2.9))

print("*" * 6+"Math Operations"+"*" * 6)
print(math.ceil(2.9))
print(math.floor(2.9))
print(math.pi)
print(math.e)
print(math.inf)
print(math.nan)
print(math.factorial(5))
print(math.pow(2, 3))
print(math.sqrt(16))
print(math.sin(math.pi / 2))
print(math.cos(math.pi))
print(math.tan(math.pi / 4))
print(math.log(100, 10))

print("*" * 6+"Type  Casting"+"*" * 6)

x=input("Enter a number: ")
y=int(x)+1
print(type(x))
print(f"Value of x: {x}"+f" Value of y: {y}")


print(bool(None))
print(bool(0))
print(bool(""))
print(bool([]))
print(bool({}))
print(bool(1))