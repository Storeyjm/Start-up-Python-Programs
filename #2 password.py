#2 password

#user inputs password
psw = input("Type in your password")

#password detection
num = len(psw)
 
if num > 6:
    print ("Password is valid")
else:
    print ("Password is invalid")

#end if