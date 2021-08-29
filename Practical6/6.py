a = int(input("Enter a number : "))

def pow(n):
    print(1)
    print(a)
    b = a
    for i in range(3):
        temp = b
        b = temp * a
        print(b)

pow(a)