class Student:
    cnt = 0
    def __init__(self):
        Student.cnt = Student.cnt+1

    def get_value(self, en, name, branch):
        self.en = en
        self.name = name
        self.branch = branch

    def print_value(self):
        print("Enrollment No: {}\nName: {}\nBranch: {}\n".format(self.en, self.name, self.branch))

    def show(self):
        print("Number of instances created : {}".format(Student.cnt))

s1 = Student()
s1.get_value(19012011094, "BHANWAR LAL CHOUDHARY", "CE")
s1.print_value()
s1.show()
s2 = Student()
s2.show()
s3 = Student()
s3.show()