# Python program to find non repeating characters in a string :
s= input("Enter a string : ")

for i in s :
    c = 0
    for j in s :
        if i == j :
            c += 1

        if c > 1 :
            break
    if c == 1:
        print(i,end ="")
    
