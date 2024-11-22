#Data Types
#Integers
#large numbers
large_int = 1_000_000_000

#float
floating_number = 100.02

#Boolean
bool_data_type = True

#string
string_data_type = "Hello"

#Print out the data types using F-String
print(f"This is a string: {string_data_type}\nThis is a large integer: {large_int}\nThis is a float: {floating_number}\nThis is a boolean: {bool_data_type}")


print("Data types")
print(f"{type(large_int)}\n{type(floating_number)}\n{type(bool_data_type)}\n{type(string_data_type)}")

#Mathematical Operations
print(1+2) #Addition
print(3-1) #Subtraction
print(3*2) #Multiplication
print(4/3) #Division
print(5//4) #converts the result to an integer
print(4**2) #Exponent

#Order of Operation
#PEDMAS - LEFT2RIGHT
#()
#Exponent
#Division
#Multiplication
#Addition
#Subtraction

#Calculate BMI
print("BMI Calculator")
weight = float(input("Enter your weight im Kilograms: "))
height = float(input("Your height in meters: "))
bmi = round((weight/(height ** 2)),2) #rounds up to the nearest 2 deciml points
print(f"your bmi is: {bmi}")


#Assignments
score = 0
score += 1 # same as score = score + 1
print(score)
