def leftshift(l,n):
    list = []
    for i in range(1,len(l)):
        list.append(l[i])
    for i in range(0,1):
        list.append(l[i])
    return list
rotate_num = 1
L= [1,2,3,4]
print(leftshift(L, rotate_num))