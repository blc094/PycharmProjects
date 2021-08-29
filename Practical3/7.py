st = input("Enter string : ")
count1 = 0
count2 = 0
for i in st:
    if(i.islower()):
        count1 = count1 + 1
    elif(i.isupper()):
        count2 = count2 + 1

print("The number of lower case characters is : ",count1)
print("The number of upper case characters is : ",count2)
