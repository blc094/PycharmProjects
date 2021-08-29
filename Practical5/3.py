d = {"a":1,"b":2,"c":3,"d":4,"e":5}
print(d)
result = {key:value for (key, value) in d.items() if value <= 2}
print(result)