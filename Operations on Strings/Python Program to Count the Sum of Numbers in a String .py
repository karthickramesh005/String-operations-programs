# Python Program to Count the Sum of Numbers in a String : 

#take user input
String = input("Enter a string : ")
#initialize integer variable
sum1 = 0
for i in String:
    #check if values lies between range of numbers or not
    #according to ascii tale
    if ord(i) >= 48 and ord(i) <= 57:
        #convert it to integer and add
        sum1 = sum1 + int(i)
print('Sum is :' + str(sum1))
