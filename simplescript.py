#Program to find the average expenditure

food = input("How much was spent on food?")
travel = input("How much was spent on travel?")
accessories = input("How much was spent on accessories?")
clothing = input("How much was spent on clothing?")
education = input("How much was spent on education?")
health = input("How much was spent on health?")

number = 6
total = float(food) + float(travel) + float(accessories) + float(clothing) + float(education) + float(health)
average = total / number

print (average)


