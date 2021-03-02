import random
square=[]       #Το τετράγωνο με τυχαίους 0,1
set_of_four=[]  #Λίστα με τετράδες από 1


"""Δημιουργία του τετραγώνου και γέμισμα των μισών θέσεων (στρογγυλοποίηση προς τα πάνω) τυχαία με άσσους και μηδενικά"""

def create_square():
    if((N*N)%2==0):
        num_of_1=N*N//2
    else:
        num_of_1=N*N//2+1
    num_of_0=N*N//2
    list_of_1=[1 for x in range(0,num_of_1)]
    list_of_0=[0 for x in range(0,num_of_0)]
    list_of_01=list_of_1+list_of_0
    for i in range(0,N):
        l=[]
        for j in range(0,N):
            size=len(list_of_01)
            number=random.randint(0,size-1)
            l.append(list_of_01[number]);
            list_of_01.pop(number)
        square.append(l)

"""Έλεγχος αν η τετράδα έχει προσμετρηθεί και καταχώρησή της διαφορετικά"""
def put_four_in_set(l):
    if l not in set_of_four:
        set_of_four.append(l)


"""Έλεγχος τετράδων με 1 για έναν υποπίνακα 4Χ4. x,y το σημείο εκκίνησης"""
def check_a_4x4(x,y):

    #Έλεγχος γραμμών για τετράδες άσσων και τοποθέτηση στη λίστα
    for i in range(x,x+4):
        s=0
        l=[]
        for j in range(y,y+4):
            s=s+square[i][j]
            l.append((i,j))
        if(s==4):
            put_four_in_set(l)

    #Έλεγχος στηλών για τετράδες άσσων και τοποθέτηση στη λίστα
    for j in range(y,y+4):
        s=0
        l=[]
        for i in range(x,x+4):
            s=s+square[i][j]
            l.append((i,j))
        if(s==4):
            put_four_in_set(l)

    #Έλεγχος διαγωνίων για τετράδες άσσων και τοποθέτηση στη λίστα        
    s=0
    l=[]
    row=-1
    for i in range(x,x+4):
        row=row+1
        col=-1
        for j in range(y,y+4):
            col=col+1
            if((row==col)and(square[i][j]==1)):
                s=s+1
                l.append((i,j))
    if(s==4):
        put_four_in_set(l)

    l=[]
    s=0
    row=-1
    for i in range(x,x+4):
        row=row+1
        col=-1
        for j in range(y,y+4):
            col=col+1
            if((row+col==3)and(square[i][j]==1)):
                s=s+1
                l.append((i,j))
    if(s==4):
        put_four_in_set(l)


"""
Έλεγχος όλων των υποπινάκων 4Χ4 που δημιουργούνται από τον αρχικό πίνακα
"""
def check_all():
    for i in range(0,N-3):
        for j in range(0,N-3):
            check_a_4x4(i,j)
    return len(set_of_four)

"""Εκτύπωση του τυχαίου πίνακα

def square_output():
    for i in range(0,N):
        print(square[i])"""

N=int(input("Δώσε τη διάσταση του τετραγώνου: "))
total=0
for i in range(0,100):
    square=[]
    set_of_four=[]
    create_square()
    #square_output()
    tetrades=check_all()
    #print("τετράδες: ------>",tetrades)
    #print(set_of_four)
    #print("______________________\n")
    total=total+tetrades
print("Το σύνολο των τετράδων από άσσους που εμφανίστηκαν συνολικά είναι: ",total)
print("Ο μέσος όρος των τετράδων από άσσους είναι: ",total/100)
