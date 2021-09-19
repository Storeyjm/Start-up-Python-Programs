#14.Reverse

#User inputs word
myWord = input("Enter a word:")

#intitiate counter
counter = len(myWord) - 1

reversestring = ""

#words put in reverse order
while counter > -1:
    reversestring = reversestring + myWord[counter]
    counter = counter - 1
#endwhile

#print
print(reversestring)