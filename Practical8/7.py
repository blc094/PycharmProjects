class A:
    def check(self):
        print("Class A")

class B:
    pass

class D(A):
    def check(self):
        print("Class D")

class C(B):
    def check(self):
        print("Class C")

class E(B,D):
    pass

obj = E()
print("Scenario-1: ")
obj.check()

#scenario2
class A:
    def check(self):
        print("Class A")

class B(A):
    pass

class F:
    def check(self):
        print("Class F")

class C(F):
    def check(self):
        print("Class C")

class D(F):
    def check(self):
        print("Class D")

class E(B,C,D):
    pass

obj = E()
print("Scenario-2: ")
obj.check()
