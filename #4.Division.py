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
print (a,"remainder", b)

## Your print statemeent needs commas .. In have put them in
## Also I don't think there is any need to covert to float as the results are integers. 
## Convert inputs to int I would think