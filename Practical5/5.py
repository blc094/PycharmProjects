movies = {"War":[3,5], "Bourne":[18,5], "Gully Boy":[15,5], "Uri":[12,5]}
m_name = input("Enter the movie name : ")
age = int(input("Enter your age : "))
t = int(input("Enter the number of ticket : "))
k = 0
c = 0
for i in movies:
    if(m_name==i):
        k=1
        m_name = movies
        break
if(k==1):
    for j in m_name.values():
        if(j[0]<=age and j[1]>=t):
            c=1
        else:
            print("Movie is not available")
    if(c==1):
        print("Ticket is available")
    else:
        print("Ticket is not available")