f = open("two_cities_ascii.txt", "r")#Άνοιγμα αρχείου για διάβασμα
text=f.read()#Εκχώρηση του περιεχόμενου του αρχείου στηνν μεταβλητή text ως string
f.close()#Κλείσιμο του αρχείου

L = []#Δημιουργία κενής λίστας με σκοπό να βάλουμε ΄όλες τις λέξεις χωρίς τα σύμβολα

"""Καθάρισμα του κειμένου από όλους τους χαρακτήρες που δεν είναι γράμματα"""
text=text.replace(',',' ')
text=text.replace('.',' ')
text=text.replace('!',' ')
text=text.replace('"',' ')
text=text.replace('#',' ')
text=text.replace('$',' ')
text=text.replace('%',' ')
text=text.replace('^',' ')
text=text.replace('&',' ')
text=text.replace('(',' ')
text=text.replace(')',' ')
text=text.replace('*',' ')
text=text.replace('+',' ')
text=text.replace('-',' ')
text=text.replace('/',' ')
text=text.replace('0',' ')
text=text.replace('1',' ')
text=text.replace('2',' ')
text=text.replace('3',' ')
text=text.replace('4',' ')
text=text.replace('5',' ')
text=text.replace('6',' ')
text=text.replace('7',' ')
text=text.replace('8',' ')
text=text.replace('9',' ')
text=text.replace(':',' ')
text=text.replace(';',' ')
text=text.replace('<',' ')
text=text.replace('=',' ')
text=text.replace('>',' ')
text=text.replace('?',' ')
text=text.replace('@',' ')
text=text.replace('[',' ')
text=text.replace('\ ',' ')
text=text.replace(']',' ')
text=text.replace('_',' ')
text=text.replace('}',' ')
text=text.replace('|',' ')
text=text.replace('{',' ')
text=text.replace('~',' ')
text=text.replace('`',' ')


L = text.split()#Διαχωρισμός των λέξεων με βάση τον κενό χαρακτήρα και εκχώρηση αυτών στην λίστα

#Έλεγχος και εμφάνιση των ζευγαριών των λέξεων της λίστας των οποίων το μήκος χαρακτήρων είναι στο σύνολο ακριβώς 20
i=0
while(i<len(L)-1):
    removeitems=L[i]
    j=i+1
    while(j<len(L)-2):
        n=len(L[i]+L[j])
        if n==20:
            print('Ζευγάρι λέξεων: ',L[i],'-',L[j])
            if(i<j):
                L.pop(i)
                L.pop(j+1)
            else:
                L.pop(i)
                L.pop(j)
        j=j+1
    i=i+1

#Δημιουργία λιστών για την τοποθέτηση των λέξεων που απέμειναν με βάση το μήκος τους
ls1=[]
ls2=[]
ls3=[]
ls4=[]
ls5=[]
ls6=[]
ls7=[]
ls8=[]
ls9=[]
ls10=[]
ls11=[]
ls12=[]
ls13=[]
ls14=[]
ls15=[]
ls16=[]
ls17=[]
ls18=[]
ls19=[]
for i in range(len(L)):
    if len(L[i])==1:
        ls1.append(L[i])
    elif len(L[i])==2:
        ls2.append(L[i])
    elif len(L[i])==3:
        ls3.append(L[i])
    elif len(L[i])==4:
        ls4.append(L[i])
    elif len(L[i])==5:
        ls5.append(L[i])
    elif len(L[i])==6:
        ls6.append(L[i])
    elif len(L[i])==7:
        ls7.append(L[i])
    elif len(L[i])==8:
        ls8.append(L[i])
    elif len(L[i])==9:
        ls9.append(L[i])
    elif len(L[i])==10:
        ls10.append(L[i])
    elif len(L[i])==11:
        ls11.append(L[i])
    elif len(L[i])==12:
        ls12.append(L[i])
    elif len(L[i])==13:
        ls13.append(L[i])
    elif len(L[i])==14:
        ls14.append(L[i])
    elif len(L[i])==15:
        ls15.append(L[i])
    elif len(L[i])==16:
        ls16.append(L[i])
    elif len(L[i])==17:
        ls17.append(L[i])
    elif len(L[i])==18:
        ls18.append(L[i])
    elif len(L[i])==19:
        ls19.append(L[i])

#Εμφάνιση των ζευγαριών που απέμειναν στην λίστα με βάση το μήκος τους
print("*******************Λέξεις που απομένουν*****************")
print(" 1",ls1,"\n","2",ls2,"\n","3",ls3,"\n","4",ls4,"\n","5",ls5,"\n","6",ls6,"\n","7",ls7,"\n","8",ls8,"\n","9",ls9,"\n","10",ls10,"\n","11",ls11,"\n","12",ls12,"\n","13",ls13,"\n","14",ls14,"\n","15",ls15,"\n","16",ls16,"\n","17",ls17,"\n","18",ls18,"\n","19",ls19)
