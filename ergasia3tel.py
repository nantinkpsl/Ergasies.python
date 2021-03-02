import json
import urllib.request

fp=open('file.txt','r')#Άνοιγμα αρχείου με σκοπό να το διαβάσω
f=fp.read() #Ανάθεση του περιεχόμενου του αρχείου στην μεταβλητή f
f=f[1:-1] #Αφαίρεση των {}

#Δημιουργία λίστας με μεμονωμένα τα στοιχεία του λεξικού που διαβάσαμε σε λίστες με ένα στοιχειο
s=[]
d=f.split(',') #Χωρίζω τα στοιχεία με βάση το κόμμα
for i in range(len(d)):
  d[i]=d[i].split(':')#Χωρίζω τα στοιχεία με βάση την :
  d[i][0]=d[i][0].split("'")
  d[i][1]=d[i][1].split("'")
  s.append(d[i][0][0][1:-1].split("'"))
  s.append(d[i][1][0].split("'"))


#Δημιουργία λίστας που θα περιέχει τα ονόματα και το πλήθος των κρυπτονομισμάτων που διαθέτει ο χρήστης από το καθένα ως ξεχωριστά στοιχεία
j=[]
for i in range(len(s)):
   j.append(s[i][0])

for i in range(len(j)):
    if i%2==1:#Έλεγχος έτσι ώστε να μετατραπεί μόνο το πλήθος των κρυπτονομισμάτων που διαθέτει ο χρήστης απο string σε float.
        e=j[i]
        j[i]=float(e) #Αλλαγή του τύπου του πλήθους των κρυπτονομισμάτων που διαθέτει ο χρήστης απο string σε float.

dict={}#Δημιουργία κενού λεξικού
for i in range(len(j)):
    if i%2==0:
        dict[j[i]]=j[i+1]

#Κάνουμε την σύνδεση με το url από το οποίο θα πάρουμε τις τιμές των κρυπτονομισμάτων.
def get_coin_data(coin):
    url="https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,LTC&tsyms=EUR&e=CCCAGG"
    r=urllib.request.urlopen(url)
    html=r.read()
    html=html.decode()
    d=json.loads(html)
    return d[coin]["EUR"]

#Εμφάνιση του ποσού σε ευρώ που αντιστοιχεί το πλήθος που διαθέτει ο χρήστης απο το το κάθε κρυπτονόμισμα.
for i in range (len(j)):
    if i%2==0:
       print("Το ποσό σε ευρώ που αντιστοιχεί το πλήθος που διαθέτετε από το κρυπτονόμισμα",j[i],"είναι:",get_coin_data(j[i])*j[i+1])



fp.close() #Κλείσιμο του αρχείου.
