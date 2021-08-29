n = int(input("Enter the Number : "))
print("The entered number divisors are")
for i in range(1, n+1):
    if(n%i==0):
        print(i)