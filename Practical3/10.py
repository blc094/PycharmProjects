st = input("Enter the String : ")
sub_st = input("Enter the word : ")
if(st.find(sub_st) == -1):
    print("SubString not found in String!")
else:
    print("SubString found in String!")