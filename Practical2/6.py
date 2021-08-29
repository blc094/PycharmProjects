n = int(input("Enter the number of days late : "))

if n <= 5:
    print('fine is',0.40*n)

elif n <= 10 :
    print('fine is', 0.65 * n)

else:
    print('fine is', 0.80 * n)
