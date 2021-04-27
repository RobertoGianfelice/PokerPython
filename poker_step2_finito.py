from random import randint

Carte=["AC","2C","3C","4C","5C","6C","7C","8C","9C","dC","JC","QC","RC",
       "AQ","2Q","3Q","4Q","5Q","6Q","7Q","8Q","9Q","dQ","JQ","QQ","RQ",
       "AF","2F","3F","4F","5F","6F","7F","8F","9F","dF","JF","QF","RF",
       "AP","2P","3P","4P","5P","6P","7P","8P","9P","dP","JP","QP","RP"]
Scale=[["2","3","4","5","A"],
       ["3","4","5","6","7"],
       ["4","5","6","7","8"],
       ["5","6","7","8","9"],
       ["6","7","8","9","d"],
       ["7","8","9","d","J"],
       ["8","9","d","J","Q"],
       ["9","d","J","Q","R"],
       ["d","A","J","Q","R"]]



def estraiValori(mano):
    valori=[]
    for carta in mano:
        valori.append(carta[0])
    return (valori)

def estraiSemi(mano):
    semi=[]
    for carta in mano:
        semi.append(carta[1])
    return (semi)

def cercaPokerCoppieTrisFull(valori):
    coppia=False
    tris=False
    for i in valori:
        if (valori.count(i)==4):
            print("poker di ", i)
            for j in range(4):
                valori.remove(i)
        elif (valori.count(i)==3):
            print("tris di ", i)
            for j in range(3):
                valori.remove(i)
            tris=True
        elif (valori.count(i)==2):
            print("coppia di ", i)
            for j in range(2):
                valori.remove(i)
            coppia=True

    if ( coppia and tris ):
        print("FULL!!!!")

def cercaColore(mano):
    for seme in mano:
        if mano.count(seme)==5:
            print("Colore di ", seme)
            return

def cercaScala(mano):
    mano.sort()

    # print("Cerco scala in ", mano)
    if mano in Scale:
        print("SCALA!!!", mano)
    return

giocatori=int(input("quanti giocatori siete?"))
carteDate=[]
for i in range(giocatori):
    print("Carte del giocatore", i+1)
    carteDate.append([])
    for j in range(5):
        cartascelta=Carte[randint(0,len(Carte)-1)]
        print("Carta numero",cartascelta)
        carteDate[i].append(cartascelta)
        Carte.remove(cartascelta)
    print (carteDate[i])
print(carteDate)

for i in range(giocatori):
    print("esamino carte del giocatore ", i+1, " che ha queste carte: ", carteDate[i])
    valori=estraiValori(carteDate[i])
    cercaPokerCoppieTrisFull(valori)
    semi=estraiValori(carteDate[i])

    cercaColore(semi)
    cercaScala(valori)

    # Test:
    # print("ecco la mano ordinata------>>>>", valori)
    # cercaPokerCoppieTris(["A","A","A","2","2"])
    # cercaColore(["Q","Q","Q","Q","Q"])
    # cercaScala(["2","2","4","5","6"])
    # cercaScala(["A","2","3","4","5"])
