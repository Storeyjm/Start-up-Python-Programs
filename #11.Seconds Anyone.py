#11.Seconds Anyone?

#User input
myTime = input("Input a time in the form: h:m:s")

#split input
splitVal = myTime.split(":")

#conversion into seconds
hour = int(splitVal[0])* 3600 + int(splitVal[1]) * 60 + int(splitVal[2])

#print output
print(hour)

## A good solution