st = 'I love doing python programming in spyder'
words = list(st.split(' '))
print("st : ",st)
print("list converted string : ",words)
print("Even length word : ")
for w in words:
    if(len(w)%2==0):
        print(w)