#5.Hundreds, tens and units

#User inputs number
num = int(input("Enter a number between 100 and 999"))

#Splits numbers up
a = num // 100
b = (num - (a * 100)) // 10
c = num - (a * 100) - (b * 10)

#Prints output
print(a, "hundreds", b, "tens", c, "units.")

## ACS - Excellent work.  Maybe a few more comments.