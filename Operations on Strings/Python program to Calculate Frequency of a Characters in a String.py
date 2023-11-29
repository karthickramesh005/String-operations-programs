# Python program to Calculate Frequency of a Characters in a String :
s= input("Enter a string : ")

for i in s :
    fri = s.count(i)
    print(str(i),":",str(fri),end = ",")
