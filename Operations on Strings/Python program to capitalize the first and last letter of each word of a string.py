# Python program to capitalize the first and last letter of each word of a string : 

#take user input
String = input('Enter the String :')
#start slicing the String
#take 1st character and convert it to upper case
#Concatinate the string with remaning-1 length
#take last character and change it to uppercase and concatinate it to string
String = String[0:1].upper() + String[1:len(String)-1] + String[len(String)-1:len(String)].upper()
#print the String
print(String)
