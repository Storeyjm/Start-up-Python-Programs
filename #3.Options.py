#3.Options

#User enters number
Input = input("Enter a number between 1 & 3")

#Converts input into integer
num = int(Input)

while num < 1 or num > 3:
    Input = input("Enter a number between 1 & 3")
    num = int(Input)
print(num)

## ACS - Very good work