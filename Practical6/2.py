def prime(a, b):
    for num in range(a, b):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
num1 = int(input("Enter the lower range : "))
num2 = int(input("Enter the upper range : "))
print("The prime numbers are : ")
prime(num1, num2)
