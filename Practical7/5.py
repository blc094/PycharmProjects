import csv
fields = ["Name", "Enrollment No", "Branch", "Batch", "Sem"]

student = 1
all_rows = []

def get_data(student):
    rows = []
    print("Student ",student)
    rows.append(input("Name : "))
    rows.append(input("Enrollment No : "))
    rows.append(input("Branch : "))
    rows.append(input("Batch : "))
    rows.append(input("Sem : "))
    all_rows.append(rows)

    print("Do you want to still Enter data : ")
    print("Press 1 to Continue else Press 0")
    choose = int(input("choose : "))
    if choose == 1:
        get_data(student)
    else:
        return


get_data(student)
print(all_rows)
with open("student.csv", "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(all_rows)

with open("student.csv", "r") as csvfile:
    read_csv = csv.reader(csvfile)
    for i in read_csv:
        print(i)