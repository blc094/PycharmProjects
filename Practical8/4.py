class Hospital:
    def __init__(self, patient_no, patient_name, disease_name):
        self.p_no = patient_no
        self.p_name = patient_name
        self.d_name = disease_name

    def display(self):
        print("Patient No: {}\nPatient Name: {}\nDisease: {}\n".format(p1.p_no, p1.p_name, p1.d_name))


p1 = Hospital(1, "Payal", "Cold")
p1.display()
print("Name by get attributed: ", getattr(p1, "d_name"))

setattr(p1, "d_name", "Corona")
print("Disease by set attribute: ", getattr(p1, "p_name"))

print("Has attributed: ", hasattr(p1, "p1_no"), "\n")

print("Values of attributes __dict, __doc, __name, __module, __bases_ :\n")
print(Hospital.__dict__)
print("\n", Hospital.__doc__)
print("\n", Hospital.__name__)
print("\n", Hospital.__module__)
print("\n", Hospital.__bases__)
