print('"=============================================================================="')
class Student:
    def personal_details():
        name = input("Enter your name : ")
        en_roll = input("Enter your enrollment number : ")
        branch = input("Enter your branch : ")
        age = input("Enter your age : ")
        email = input("Enter your email : ")
        mob_no = input("Enter your mobile number : ")

        print("Name : {}\nEnrollement : \nBranch : \nAge : \nEmail : \nMobile : ".format(name,en_roll,branch,age,email,mob_no
                                                                                         ))

    personal_details()
print('"=============================================================================="')