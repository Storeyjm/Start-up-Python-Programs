#12.Factors

#User inputs
myNumber = int(input(("Enter an integer: ")))

#Initiate counter
counter = 1

#While loop
while counter < (myNumber /2) +1 :
    if myNumber % counter == 0:
        print(counter)
    counter = counter + 1
#endwhile
print (myNumber)