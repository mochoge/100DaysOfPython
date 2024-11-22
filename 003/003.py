#Control Flow and Logical Operators
#if else

print("County Water Tank")
MAX_WATER_LEVEL = 100
water_level = int(input("Enter current water level in litres: "))

if water_level >= MAX_WATER_LEVEL:
    print("Closing gate valve")
else:
    print(f"{MAX_WATER_LEVEL - water_level} litres to full")


#while statement
print("\n\nWelcome to Python Petrol/Gas Station!")
fuel_gauge = 0
fuel_level = int(input("Enter amount of fuel in litres: "))
while fuel_gauge < fuel_level:
    fuel_gauge += 1
    if fuel_gauge == fuel_level:
        print(f"Fuel tank is full: {fuel_gauge} litres")
    else:
        print(f"Gate valve open, fuel flowing: {fuel_gauge} litres")


#Modolu
remainder = 4 % 2
print(f"The remainder of 4 / 2 is: {remainder}")


#Check if number is even using Modulo operator
num_input = int(input("Enter your prefered number: "))
remainder = num_input % 2

#Check if even
if remainder == 0:
    print(f"The number {num_input} is even.\n")
else:
    print(f"The number {num_input} is not even.\n")

#and not or
bool_true = True
bool_false = False

print(bool_true and bool_true)
print(not bool_false and bool_true)
print(bool_false or bool_true)
print(bool_false and not bool_true)