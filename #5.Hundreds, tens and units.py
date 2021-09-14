#5.Hundreds, tens and units

#User inputs number
num = int(input("Enter a number between 100 and 999"))

#Hundreds
a = num // 100
#Tens
b = (num - (a * 100)) // 10
#Units
c = num - (a * 100) - (b * 10)

#Prints output
print(a, "hundreds", b, "tens", c, "units.")