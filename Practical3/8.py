st = input("Enter the string : ")
st = st.casefold()

rev_st = reversed(st)

if list(st) == list(rev_st):
    print("The string is a Palindrome.")
else:
    print("The string is not a Palindrome.")