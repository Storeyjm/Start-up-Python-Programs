#4.Division

#User inputs number
Input1 = input("Enter an integer")
Input2 = input("Enter a divisor")

#Converts into a float
Integer = float(Input1)
Divisor = float(Input2)

#Divides integer by dividor
a = (Integer // Divisor)
b = (Integer % Divisor)

#Prints output
print (a "remainder" b)