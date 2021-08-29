myDict = {"male": ["Tom", "Charlie", "Harry", "Frank"], "female": ["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"]}
male = myDict["male"]
female = myDict["female"]
print("Names containing a are")
for i in range(len(male)):
    if("a" in male[i]):
      print(male[i])

for i in range(len(female)):
    if("a" in female[i]):
        print(female[i])