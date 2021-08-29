def max_min(a):
    b = tuple([max(a)])
    c = tuple([min(a)])
    print("Maximum Element : ", b)
    print("Minimum Element : ", c)

n = int(input("Enter size of list : "))
a = []
print("Enter list of size ",n, ":")
for i in range(n):
    a.append(int(input()))
print("List : ")
print(a)
max_min(a)