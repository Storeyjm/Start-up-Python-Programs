#13.Ceaser Cypher

#Uer inputs string
myString = input("Enter a string:")
myString = myString.upper()

counter = 0
newWord = ""

while counter < len(myString):
    newWord = newWord + chr(((ord(myString[counter]) -64 + 3) % 26) + 64)
    counter = counter + 1
#endwhile

#print
print(newWord)