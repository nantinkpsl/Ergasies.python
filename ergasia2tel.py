import random
square=[]
set_of_sos=[]

"""Δημιουργία του ορθογωνίου και γέμισμα των μισών θέσεων (στρογγυλοποίηση προς τα πάνω) τυχαία με άσσους και μηδενικά"""
def create_square():
    num_of_s=N*M//2
    num_of_o=N*M//2+N*M%2
    list_of_o=['O' for x in range(0,num_of_o)]
    list_of_s=['S' for x in range(0,num_of_s)]
    list_of_os=list_of_o+list_of_s

    for i in range(0,N):
        l=[]
        for j in range(0,M):
            size=len(list_of_os)
            number=random.randint(0,size-1)
            l.append(list_of_os[number]);
            list_of_os.pop(number)
        square.append(l)

"""Έλεγχος αν η τριάδα έχει προσμετρηθεί και καταχώρησή της διαφορετικά"""
def put_sos_in_set(l):
    if l not in set_of_sos:
        set_of_sos.append(l)

"""Έλεγχος τριάδων SOS για έναν υποπίνακα 3Χ3. x,y το σημείο εκκίνησης"""
def check_a_3x3(x,y):

    #Έλεγχος γραμμών για SOS και τοποθέτηση στη λίστα
    for i in range(x,x+3):
        s=''
        l=[]
        for j in range(y,y+3):
            s=s+square[i][j]
            l.append((i,j))
        if(s=='SOS'):
            put_sos_in_set(l)

    #Έλεγχος στηλών για SOS και τοποθέτηση στη λίστα
    for j in range(y,y+3):
        s=''
        l=[]
        for i in range(x,x+3):
            s=s+square[i][j]
            l.append((i,j))
        if(s=='SOS'):
            put_sos_in_set(l)

    #Έλεγχος διαγωνίων για SOS και τοποθέτηση στη λίστα
    fir_l=[]
    sec_l=[]
    fir_s=''
    sec_s=''
    row=-1
    for i in range(x,x+3):
        row=row+1
        col=-1
        for j in range(y,y+3):
            col=col+1
            if(row==col):
                fir_s=fir_s+square[i][j]
                fir_l.append((i,j))
            if(row+col==2):
                sec_s=sec_s+square[i][j]
                sec_l.append((i,j))

    if(fir_s=='SOS'):
        put_sos_in_set(fir_l)

    if(sec_s=='SOS'):
        put_sos_in_set(sec_l)

"""Έλεγχος όλων των υποπινάκων 3Χ3 που δημιουργούνται από τον αρχικό πίνακα"""
def check_all():
    for i in range(0,N-2):
        for j in range(0,M-2):
            check_a_3x3(i,j)
    return len(set_of_sos)

"""Εκτύπωση του τυχαίου πίνακα
def square_output():
    for i in range(0,N):
        print(square[i])"""

N=int(input("Δώσε το πλάτος του ορθογωνίου: "))
M=int(input("Δώσε το μήκος του ορθογωνίου: "))
total=0
for i in range(0,100):
    square=[]
    set_of_sos=[]
    create_square()
    #square_output()
    sos_counter=check_all()
    #print("SOS: ------>",sos_counter)
    #print(set_of_sos)
    #print("______________________\n")
    total=total+sos_counter

print("Το σύνολο των SOS που εμφανίστηκαν συνολικά είναι: ",total)
print("Ο μέσος όρος των SOS είναι: ",total/100)
