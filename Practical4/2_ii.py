list = []
n = int(input("Enter the numbers you want to print : "))
for i in range(1, n + 1):
    element = int(input("Enter elements : "))
    list.append(element)
print("Maximum element is : ", max(list))
print("Minimum element is : ", min(list))