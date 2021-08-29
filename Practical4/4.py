print("\n\t\t BHANWAR LAL CHOUDHARY \t\t 19012011094\n\t\t\tCE-B\t\t\tAB-3\n")
a = [3,6,12,-6,8,0]
a.sort()
print(a)
b = []
b.insert(0,a[0])
for i in range(1, len(a)):
    temp = 0
    for j in range(0, len(b)):
        if b[j]<a[i]:
            continue
        else:
            temp = 1
            b.insert(j, a[i])
            break
        if temp == 0:
            b.insert(j+1, a[i])
print(b)