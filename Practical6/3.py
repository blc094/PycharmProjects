def sorting(a,n):
    for i in range(0, n-1):
        for j in range(i, n):
            if(a[i] > a[j]):
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
n = int(input("Enter size of list : "))
a = []
print("Enter List of Size ", n, ":")
for i in range(n):
    a.append(int(input()))
print(" ")
print("Un-Sorted List : ")
print(a)
sorting(a, n)
print(" ")
print("Sorted List : ")
print(a)