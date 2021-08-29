st = input("Enter the string : ")
new_st = " "
for i in range(len(st)):
    if i != 2:
        new_st = new_st + st[i]

print("The string after removal of ith character : " + new_st)