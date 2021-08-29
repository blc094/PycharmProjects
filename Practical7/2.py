data = data2 = ""
with open("file1.txt") as f1:
    data = f1.read()

with open("file2.txt") as f2:
    data2 = f2.read()

data += "\n"
data += data2

with open("file3.txt", "w") as f3:
    f3.write(data)