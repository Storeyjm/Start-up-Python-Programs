#9.Comparison of Three

#User inputs numbers
Num1 = int(input("Enter a number"))
Num2 = int(input("Enter a different number"))
Num3 = int(input("Enter a final number"))

#If statement and print
if Num1 > Num2 > Num3:
    print(Num1, Num2, Num3)
elif Num2 > Num1 > Num3:
    print(Num2, Num1, Num3)
elif Num2 > Num3 > Num1:
    print(Num2, Num3, Num1)
elif Num3 > Num1 > Num2:
    print(Num3, Num1, Num2)
else:
    print(Num3, Num2, Num1)
#end if