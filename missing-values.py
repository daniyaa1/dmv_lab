name = input("Enter your name: ")

if name == "":
    name = "Guest"

age = input("Enter your age: ")

if age == "":
    age = 18
else:
    age = int(age)

city = input("Enter your city: ")

if city == "":
    city = "Unknown"

print("Name:", name)
print("Age:", age)
print("City:", city)