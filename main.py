########################
###[POKER SIMULATION]###
########################
## De la simulation des probabilités des combinaisons de poker
## Martin MAUTOUCHET Tle 1

## Importations
import itertools
from collections import Counter
from tqdm import tqdm
#import numpy as np

## Constantes : 
CARDS_VALUES = ["1","2","3","4","5","6","7","8","9","10","V","D","R"]
CARDS_COLORS = ["pi","co","tr","ca"]
DECK = [x + ";" + y for x in CARDS_VALUES for y in CARDS_COLORS]
ALL_POSSIBLES_HAND = list(itertools.combinations(DECK,5))
nt = 2598960
## Définitions de fonctions
def getValueOfACard(card) : 
  card_value_dict = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,
  "V":11,"D":12,"R":13}
  return card_value_dict[card.split(";")[0]]

def getColorOfACard(card) : 
  return card.split(";")[1]

def isOnePair(hand) :
    """Teste si hand contient strictement 1 paire"""
    values = [getValueOfACard(card) for card in hand]
    counts = Counter(values).values()
    return sorted(counts, reverse=True) == [2,1,1,1]

def isTwoPair(hand) :
    """teste si hand contient strictement 2 paires"""
    values = [getValueOfACard(card) for card in hand]
    counts = Counter(values).values()
    return sorted(counts, reverse=True) == [2,2,1]

def isThreeOfAKind(hand) :
    """Teste si hand contient strictement 1 brelan"""
    values = [getValueOfACard(card) for card in hand]
    counts = Counter(values).values()
    return sorted(counts, reverse=True) == [3,1,1]

def isStraight(hand) :
    """Teste si hand contient une quinte"""
    values = sorted([getValueOfACard(card) for card in hand])
    colors = [getColorOfACard(card) for card in hand]
    if len(set(values)) != 5:
        return False
    if len(set(colors)) == 1:
        return False  # exclut straight flush
    if max(values) - min(values) == 4:
        return True
    if set(values) == {1,2,3,4,5}:
        return True
    if set(values) == {1,10,11,12,13}:
        return True
    return False

def isFlush(hand) : 
    """Teste si hand contient une couleur, quinte flush et quinte flush royales exclues"""
    colors = [getColorOfACard(card) for card in hand]

    # Vérifie que toutes les cartes ont la même couleur
    if len(set(colors)) != 1:
        return False

    values = sorted([getValueOfACard(card) for card in hand])
    values_set = set(values)

    # Cas straight flush classique : 5 valeurs consécutives
    if len(values_set) == 5 and (values[-1] - values[0] == 4 or \
    values_set == {1,2,3,4,5} or values_set == {10,11,12,13,1}):
        return False

    return True

def isFullHouse(hand) : 
    """Teste si hand contient un full"""
    values = [getValueOfACard(card) for card in hand]
    counts = Counter(values).values()
    return sorted(counts, reverse=True) == [3,2]

def isFourOfAKind(hand) : 
    """Teste si hand contient un carré"""
    values = [getValueOfACard(card) for card in hand]
    counts = Counter(values).values()
    return sorted(counts, reverse=True) == [4,1]

def isStraightFlush(hand) :
    """Teste si hand contient une quinte"""
    values = sorted([getValueOfACard(card) for card in hand])
    colors = [getColorOfACard(card) for card in hand]
    if len(set(values)) != 5:
        return False
    if len(set(colors)) != 1:
        return False  # exclut straight flush
    if max(values) - min(values) == 4:
        return True
    if set(values) == {1,2,3,4,5}:
        return True
    if set(values) == {1,10,11,12,13}:
        return False
    return False

def isRoyalFlush(hand) : 
    """Teste si hand contient une quinte flush royale"""
    colors = [getColorOfACard(card) for card in hand]

    # Vérifie que toutes les cartes ont la même couleur
    if len(set(colors)) != 1:
        return False

    values = sorted([getValueOfACard(card) for card in hand])
    values_set = set(values)

    # Cas straight flush classique : 5 valeurs consécutives
    if values_set == {10,11,12,13,1}:
        return True

    return False

def isHighCard(hand) : 
    """Teste si la main a une hauteur (aucune combinaison)"""
    if not isOnePair(hand) and not isTwoPair(hand) and not isThreeOfAKind(hand)\
     and not isStraight(hand) and not isFlush(hand) and not isFourOfAKind(hand) \
     and not isStraightFlush(hand) and not isRoyalFlush(hand) and not isFullHouse(hand) : return True
    return False





## Programme principal
print("###[Simulation poker]###")
while 1 : 
    print("#"*20)
    menu_text = """Menu : 
    1 - Calcul de la probabilté d'une paire
    2 - Calcul de la probabilité d'une double paire
    3 - Calcul de la probabilité d'un brelan
    4 - Calcul de la probabilité d'une quinte, quinte flush et quinte flush royales exclues
    5 - Calcul de la probabilité d'une couleur
    6 - Calcul de la probabilité d'un full
    7 - Calcul de la probabilité d'un carré
    8 - Calcul de la probabilité d'une quinte flush
    9 - Calcul de la probabilité d'une quinte flush royale
    10 - Calcul de la probabilité d'une hauteur (rien)
    11 - Tout calculer en une seule fois
    99) Quitter
    Saisissez un choix > """

    func_dict = [isOnePair,isTwoPair,isThreeOfAKind,isStraight,isFlush,isFullHouse,
                isFourOfAKind,isStraightFlush,isRoyalFlush,isHighCard]
    choice = int(input(menu_text))
    
    if choice == 99 : break
    
    elif choice == 11 : 
        n_onepair = 0
        n_twopair = 0
        n_threeofakind = 0
        n_straight = 0
        n_flush = 0
        n_fullhouse = 0
        n_fourofakind = 0
        n_straightflush = 0
        n_royaleflush = 0
        n_highcard = 0
        
        print("Calculs en cours...")   
         #1:33 sans opti
        for hand in tqdm(ALL_POSSIBLES_HAND) : 
            if isOnePair(hand) : n_onepair += 1
            elif isTwoPair(hand) : n_twopair += 1
            elif isThreeOfAKind(hand) : n_threeofakind += 1
            elif isStraight(hand) : n_straight += 1
            elif isFlush(hand) : n_flush += 1
            elif isFullHouse(hand) : n_fullhouse += 1
            elif isFourOfAKind(hand) : n_fourofakind += 1
            elif isStraightFlush(hand) : n_straightflush += 1
            elif isRoyalFlush(hand) : n_royaleflush += 1
            else : n_highcard += 1

        print("## Résultats ##")
        print(f"Parmi les {nt} mains possibles : ")
        print(f"- {n_highcard} sont des simples paires, soit {n_highcard/nt*100} %")
        print(f"- {n_onepair} sont des simples paires, soit {n_onepair/nt*100} %")
        print(f"- {n_twopair} sont des doubles paires, soit {n_twopair/nt*100} %")
        print(f"- {n_threeofakind} sont des brelans, soit {n_threeofakind/nt*100} %")
        print(f"- {n_straight} sont des quintes, soit {n_straight/nt*100} %")
        print(f"- {n_flush} sont des couleurs, soit {n_flush/nt*100} %")
        print(f"- {n_fullhouse} sont des full, soit {n_fullhouse/nt*100} %")
        print(f"- {n_fourofakind} sont des carrés, soit {n_fourofakind/nt*100} %")
        print(f"- {n_straightflush} sont des quintes flush, soit {n_straightflush/nt*100} %")
        print(f"- {n_royaleflush} sont des quintes flush royales, soit {n_royaleflush/nt*100} %")
        print(f"Somme de vérification : {n_highcard+n_onepair+n_twopair+n_threeofakind+n_straight+n_flush+n_fullhouse+n_fourofakind+n_straightflush+n_royaleflush}={nt}")
        print("Plus la combinaison est rare, plus elle est forte.")

    else : 
      validating_func = func_dict[choice-1]

      ## Calculs
      print("Calculs en cours...")
      print(validating_func.__doc__)
      n = 0
      for hand in tqdm(ALL_POSSIBLES_HAND) : 
        if validating_func(hand) : 
          n+=1
      print("## Résultats ##")
      print(f"Nombre de mains valides parmi {nt} : {n}")
      print(f"Soit une probabilité de : {n/nt*100} % ")
    input("Appuyez sur entrée pour passer à l'itération suivante...")
print("Programme terminé, bonne journée :)")


