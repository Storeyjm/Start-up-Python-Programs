#10.Words Words Words

#User inputs sentence
myString = input("Enter a sentence")

#initiate words counter
words = 0

#initiate space_flag
space_flag = True


#Reads number of words in sentence using loop
#initiate counter
counter = 0
while counter < len(myString):
    
    # check if character is a space
    if myString[counter] == " ":
        # set space_flag to true and ignore character
        space_flag = True
    else:
        # if space_flag is true then new word so add 1
        if space_flag == True:
            words = words + 1
        # set space_flag to False as it is not a spce
        space_flag = False
        # endif
    #endif
    
    #increment counter'
    counter = counter + 1
#endwhile

#Prints final value of words
print (words)

##Very good