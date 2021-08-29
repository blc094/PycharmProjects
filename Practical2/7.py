counter = 0
odd = []

while counter < 3:
    x = int(input("Enter numbers : "))
    if abs(x)%2 != 0:
        odd.append(x)
    counter += 1

if len(odd) ==0:
    print("Entered number is not odd")
else:
    print("The maximum odd number is : ", max(odd))