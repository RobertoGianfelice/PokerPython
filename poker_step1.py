from random import randint

Carte=["AC","2C","3C","4C","5C","6C","7C","8C","9C","dC","JC","QC","RC",
       "AQ","2Q","3Q","4Q","5Q","6Q","7Q","8Q","9Q","dQ","JQ","QQ","RQ",
       "AF","2F","3F","4F","5F","6F","7F","8F","9F","dF","JF","QF","RF",
       "AP","2P","3P","4P","5P","6P","7P","8P","9P","dP","JP","QP","RP"]



# la funzione estraiValori riceve in input una lista con le carte assegnate
# ad un giocatore e restituisce una list con i soli valori delle carte
def estraiValori(mano):
    valori=[]
    #mano=["AC","3F","2Q",...]
    for carta in mano:
         valori.append(carta[0])

    return (valori)

# la funzione estraiSemi riceve in input una lista con le carte assegnate
# ad un giocatore e restituisce una list con i soli semi delle carte
def estraiSemi(mano):
    semi=[]
    #############################
    #inserisci qui il tuo codice#
    #############################
     #mano=["AC","3F","2Q",...]
    for carta in mano:
         semi.append(carta[1])
    return (semi)

# la funzione cercaPokerCoppieTris riceve in input una lista con i valori
# delle carte assegnate ad un giocatore e stampa se ha un poker, un tris o
# una o più coppie
def cercaPokerCoppieTris(valori):
    #############################
    #inserisci qui il tuo codice#
    #############################
     for valore in valori:
          if (valori.count(valore)==4):
               print("poker di ", valore)
          elif (valori.count(valore)==3):
               print("tris di ", valore)
          elif (valori.count(valore)==2):
               print("coppia di ", valore)
          valori.remove(valore)

          
        
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
    valoriMano=estraiValori(cartaDate[i])
    cercaPokerCoppieTris(valoriMano)
    
    #############################
    #inserisci qui il tuo codice#
    #############################
