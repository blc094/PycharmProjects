class OperatorOverload:
    def __init__(self, r):
        self.m = r

    def __str__(self):
        return "({0})".format(self.m)

    def __pow__(self, other):
            result = self.m**other
            return result


o1 = OperatorOverload(3)
o2 = OperatorOverload(4)
print("Answer of", o1, "power", o2, "is:{}".format(o1**o2))
