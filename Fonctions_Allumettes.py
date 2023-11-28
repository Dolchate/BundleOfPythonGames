from time import sleep
from Module.saisie import saisieEntier
from random import randint

def menuBots() -> int :

    choix : int

    print("""
╔═══════════════════════════════════════════════╗
║           Choix du deroulement :              ║
║                                               ║
║                                               ║
║        1 - Joueur contre joueur               ║
║                                               ║
║        2 - Ordinateur contre joueur           ║
║                                               ║
║        3 - Ordinateur contre ordinateur       ║
║                                               ║
║        4 - Annuler                            ║
║                                               ║
╚═══════════════════════════════════════════════╝

""")
    choix = saisieEntier("Votre choix : ")
    while choix > 4 or choix < 1 :
        print ("Choix invalide.")
        choix = saisieEntier("Votre choix : ")
    return choix
    """Procédure permettant de choisir le mode de jeu
    Entrée : None
    Sortie : Choix du mode de jeu choisi
    """


def deroulement(nbAll : int) -> int:

    choixDuJoueur : int

    choixDuJoueur = saisieEntier("Votre choix : ")
    while choixDuJoueur > nbAll or choixDuJoueur > 3 or choixDuJoueur <= 0:
        print ("La valeur d'allumette à enlever n'est pas valide.")
        choixDuJoueur = saisieEntier("Votre choix : ")
    nbAll = nbAll - choixDuJoueur 
    affAll(nbAll)
    return nbAll
    """
    Fonction permettant de choisir le nombre d'allumettes que veut enlever un joueur
    Entrée : Nombre d'allumettes 
    Sortie : Nombre d'allumette, soustraite par le nombre d'allumettes choisies
    """


def affAll(nbAll : int):
    
    i : int 

    if nbAll > 0:
        print("Nombre d'allumettes :\n")
        for i in range (nbAll):
            print("\033[1;31m0 ",end='')
        print("\033[0m")
        for i in range (nbAll):
            print("\033[1m| ",end='')
        print()
        for i in range (nbAll):
            print("| ",end='')
        print("\033[0m\n")
    if nbAll == 1:
        print("Il reste",nbAll,"allumette.")
    elif nbAll == 0:
        print("Il ne reste aucune allumette.")
    else:
        print("Il reste",nbAll,"allumettes.")
    """Procédure permettant d'afficher les allumettes pour montrer combien il en reste
    Entrée : Nombre d'allumettes
    Sortie : None"""

def verdictJvJ(quelJoueur : int, J1 : str, J2 : str, scoreJ1 : int, scoreJ2 : int):
    if quelJoueur == 2 :
        print(J1,"a perdu.")
        return scoreJ1,scoreJ2+1
    elif quelJoueur == 1 :
        print(J2,"a perdu.")
        return scoreJ1+1,scoreJ2
    else:
        print("Error system.")
    """Procédure permettant de rendre le verdict de la partie 
    d'un joueur contre un autre, ajoutant au score du joueur gagnant.
    Entrée : l'id du joueur qui aurait joué après, le pseudo du joueur 1, le pseudo du joueur 2, le score du joueur 1, le score du joueur 2
    Sortie : le score du joueur 1, le score du joueur 2"""
    
def verdict(quelJoueur : int, J1 : str, J2 : str):
    """Procédure permettant de rendre le verdict de la partie dans tous les modes 
    de jeu a l'exception du mode Joueur VS Joueur
    Entrée : l'id du joueur qui aurait joué après, le pseudo du joueur 1, le pseudo du joueur 2
    Sortie : None"""
    if quelJoueur == 2 :
        print(J1,"a perdu.")
    elif quelJoueur == 1 :
        print(J2,"a perdu.")
    else:
        print("Error system.")

def choixJoueur(J1 : str, J2 : str) -> str:

    choix : int

    print("Quel joueur va participer contre l'ordinateur ?\n")
    print("1 -",J1,"\n")
    print("2 -",J2,"\n")
    choix = saisieEntier("Votre choix : ")
    while choix != 1 and choix != 2 :
        print("Choix non valide.")
        choix = saisieEntier("Votre choix : ")
    if choix == 1:
        return J1
    if choix == 2:
        return J2
    """Fonction permettant de choisir quel joueur va participé au mode de jeu contre l'ordinateur
    Entrée : le pseudo du joueur 1, le pseudo du joueur 2
    Sortie : le pseudo du joueur choisi"""



def difficulteBot() -> str:
    choix : int
    print("""
╔═══════════════════════════════════════╗
║      Difficulté de l'ordinateur:      ║
║                                       ║
║           1 - Normale                 ║
║                                       ║
║                                       ║
║           2 - Impossible              ║
║                                       ║
╚═══════════════════════════════════════╝

""")
    choix = saisieEntier("Votre choix : ")
    while choix != 1 and choix != 2 :
        print("Choix non valide.")
        choix = saisieEntier("Votre choix : ")
    if choix == 1:
        return "BotNorm"
    if choix == 2:
        return "BotImp"
    """Fonction permettant de choisir la difficulté de l'ordinateur
    Entrée : None
    Sortie : nom de l'ordinateur choisi"""

def deroulementBotImp(nbAll : int) -> int :
    """Fonction permettant a l'ordinateur en mode 'Impossible' de jouer
    Entrée : Nombre d'allumettes 
    Sortie : Nombre d'allumettes, soustraite par le nombre d'allumettes choisies
    """

    choixDuBot : int

    if (nbAll+2)%4 == 0:
        choixDuBot = 1
    elif (nbAll+1)%4 == 0:
        choixDuBot = 2
    elif nbAll%4 == 0:
        choixDuBot = 3
    else:
        print("ERREUR, pas prévue par le programme")
        choixDuBot = 0

    nbAll = nbAll - choixDuBot 
    print("Choix de l'ordinateur :",choixDuBot)
    sleep(3)
    affAll(nbAll)
    
    return nbAll

def deroulementBotNorm(nbAll : int) -> int :
    """Fonction permettant a l'ordinateur en mode 'Normal' de jouer
    Entrée : Nombre d'allumettes 
    Sortie : Nombre d'allumettes, soustraite par le nombre d'allumettes choisies
    """
    
    choixDuBot : int

    choixDuBot = randint(1,3)
    while choixDuBot > nbAll:
        choixDuBot = randint(1,3)

    nbAll = nbAll - choixDuBot 
    print("Choix de l'ordinateur :",choixDuBot)
    sleep(3)
    affAll(nbAll)
    
    return nbAll

def choixNbAll() -> int:

    nbAll : int

    nbAll = saisieEntier("Choix du nombre d'allumettes : ")
    while nbAll<1:
        print("Choix non valide.")
        nbAll = saisieEntier("Choix du nombre d'allumettes : ")
    return nbAll
    """Fonction permettant de changer le nombre d'allumettes au départ
    Entrée : None
    Sortie : Nombre d'allumettes choisi
    """

def changeNbAll() -> int:
    """
    Fonction permettant de demander au joueurs si ils veulent changer le nombre d'allumettes au départ
    Entrée : None
    Sortie : Nombre d'allumettes"""
    choix : str

    choix = input("Voulez-vous changer le nombre d'allumettes ? o/N : ")
    choix = choix.lower()

    while choix != 'o' and choix != '' and choix != 'n' and choix != 'non' and choix !='oui' :
        print("Rentrez une valeur valide.(oui ; non ; o ; n ;  )")
        choix = input("Voulez-vous changer le nombre d'allumettes ? o/N : ")
        choix = choix.lower()

    if choix == 'o' or choix =='oui' :
        nbAll = choixNbAll()
    elif choix == 'n' or choix == 'non' or choix == '' :
        nbAll = 20
    
    return nbAll