def list_add(*args):
    return list(map(sum, zip(*args)))
a = [1, 2, 3]
b = [1, 2, 3]
print("a = ", a)
print("b = ", b)
print("\nSum of List is : ", list_add(a, b))