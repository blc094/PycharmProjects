tuplex = "w", 3, "s", "o", "u", "r", "c", "e"
print(tuplex)
tuplex = tuplex[:2] + tuplex[3:]
print(tuplex)
listx = list(tuplex)
listx.remove("o")
tuplex = tuple(listx)
print(tuplex)