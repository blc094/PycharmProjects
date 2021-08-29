n = int(input("Enter the number to check Special Number: "))
sum = 0
for i in range(1, n):
    if(n % i == 0):
        sum = sum + i

if(sum == n):
    print("Entered Number is Special Number")
else:
    print("Entered Number is Not a Special Number")