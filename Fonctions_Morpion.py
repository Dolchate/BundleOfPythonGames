from typing import List
from random import randint
from Module.saisie import saisieEntier

def choixMenu() -> int :

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


def saisieMorpion(table : List[List[str]], signe : str)-> List[List[str]]:
    """
    Fonction permettant la saisie d'un signe dans une grille de Morpion
    Entrée : Matrice, signe
    Sortie : Matrice
    """
    ligne : int
    colonne : int
    ligne = saisieEntier("Choix de la ligne : ")-1
    colonne = saisieEntier("Choix de la colonne : ")-1
    caseVide : bool
    caseVide = False
    while caseVide != True:

        if int(ligne) >= 0 and int(ligne) <= 2 and int(colonne) >= 0 and int(colonne) <= 2 and table[int(ligne)][int(colonne)] == ' ' :
            table[int(ligne)][int(colonne)] = signe
            caseVide = True
        else:
            print("Cette case est invalide.\nVeuillez en choisir une autre.")                       
            ligne = saisieEntier("Choix de la ligne : ")-1
            colonne = saisieEntier("Choix de la colonne : ")-1
        
    return table

def affMorpion(tab : List[List[str]]):
    print("╔═══╦═══╦═══╗")
    print("║",tab[0][0],"║",tab[0][1],"║",tab[0][2],"║")
    print("╠═══╬═══╬═══╣")
    print("║",tab[1][0],"║",tab[1][1],"║",tab[1][2],"║")
    print("╠═══╬═══╬═══╣")
    print("║",tab[2][0],"║",tab[2][1],"║",tab[2][2],"║")
    print("╚═══╩═══╩═══╝")
    """Procédure permettant d'afficher la grille du morpion
    Entrée : La grille du morpion
    Sortie : None
    """

def verif(table : List[List[str]])-> int:
    i : int
    j : int

    for i in range (0,3):
        if( table[i][0] == table[i][1] == table[i][2] != " " ):
            return 0

    for i in range (0,3):
        if( table[0][i] == table[1][i] == table[2][i] != " " ):
            return 0

    if( table[0][0] == table[1][1] == table[2][2] != " " ):
        return 0

    if( table[0][2] == table[1][1] == table[2][0] != " " ):
        return 0

    for i in range (0,3):
        for j in range(0,3):
            if ( table[i][j] == " " ):
                return 1
    
    return 2
    """Fonction permettant de vérifier que la grille du morpion n'a pas de vainqueur.
    Elle vérifie aussi que la grill n'est pas pleine. Renvoie un id en fonction du résultat de ses tests.
    Entrée : Grille du morpion
    Sortie : id en fonction du resultat des tests
    """

def verdict(quelJoueur : int, scoreJ1 : int, scoreJ2 : int, pseudoJ1 : str, pseudoJ2 : str, check : int):

    if check == 0 and quelJoueur == 2:
        print("Bien joué à",pseudoJ1+", c'est une victoire !")
        return scoreJ1+1,scoreJ2
    elif check == 0 and quelJoueur == 3:
        print("Bien joué à",pseudoJ2+", c'est une victoire !")
        return scoreJ1,scoreJ2+1
    else:
        print("Aucun vainqueur, bien joué à tous !")
        return scoreJ1,scoreJ2
    """Procédure permettant de rendre le verdict de la partie 
    d'un joueur contre un autre, ajoutant au score du joueur gagnant.
    Entrée : l'id du joueur qui aurait joué après, le pseudo du joueur 1, le pseudo du joueur 2, le score du joueur 1, le score du joueur 2
    Sortie : le score du joueur 1, le score du joueur 2"""

def verdictBot(quelJoueur : int, pseudoJ1 : str, pseudoJ2 : str, check : int):

    if check == 0 and quelJoueur == 2:
        print("Bien joué à",pseudoJ1+", c'est une victoire !")

    elif check == 0 and quelJoueur == 3:
        print("Bien joué à",pseudoJ2+", c'est une victoire !")

    else:
        print("Aucun vainqueur, bien joué à tous !")
    """Procédure permettant de rendre le verdict de la partie dans tous les modes 
    de jeu a l'exception du mode Joueur VS Joueur
    Entrée : l'id du joueur qui aurait joué après, le pseudo du joueur 1, le pseudo du joueur 2
    Sortie : None"""

def botNorm(table : List[List[str]],signe : str)-> List[List[str]]:
    caseVide : bool
    ligne = randint(0,2)
    colonne = randint(0,2)
    caseVide = False
    while caseVide != True:

        if int(ligne) >= 0 and int(ligne) <= 2 and int(colonne) >= 0 and int(colonne) <= 2 and table[int(ligne)][int(colonne)] == ' ' :
            table[int(ligne)][int(colonne)] = signe
            caseVide = True
        else:                       
            ligne = randint(0,2)
            colonne = randint(0,2)  
    return table
    """Fonction permettant a l'ordinateur en mode 'Normal' de jouer
    Entrée : Grille du morpion, signe à utiliser
    Sortie : Grille du morpion modifiée par le choix de l'ordinateur
    """


def botDif(table : List[List[str]],signe : str)-> List[List[str]]:
    i : int
    j : int
    compte = int
    a_joue : bool
    a_joue = False
    compte = 0

    for i in range (0,3):
        for j in range(0,3):
            if ( table[i][j] != " " ):
                compte = compte + 1
    if compte == 0:
        table[0][0] = signe
    elif compte == 1: 
        if table[0][0] == ' ':
            table[0][0] = signe
        else:
            table[1][1] = signe

    else:

        for i in range (0,3):
            if (table[0][i] == table[1][i] == signe and  table[2][i] == ' '):
                table[2][i] = signe
                a_joue = True
                return table
            elif (table[0][i] == ' ' and table[1][i] == table[2][i] == signe):
                table[0][i] = signe
                a_joue = True
                return table
            elif (table[0][i] == table[2][i] == signe and table[1][i] == ' '):
                table[1][i] = signe
                a_joue = True
                return table
        
        for i in range (0,3):
            if (table[i][0] == table[i][1] == signe and  table[i][2] == ' '):
                table[i][2] = signe
                a_joue = True
                return table
            elif (table[i][0] == ' ' and table[i][1] == table[i][2] == signe):
                table[i][0] = signe
                a_joue = True
                return table
            elif (table[i][0] ==  table[i][2] == signe and table[i][1]== ' '):
                table[i][1] = signe
                a_joue = True
                return table
        if (table[0][0] == table[1][1] == signe and  table[2][2] == ' '):
            table[2][2] = signe
            a_joue = True
            return table
        elif (table[0][0] == table[2][2] == signe and  table[1][1] == ' '):
            table[1][1] = signe
            a_joue = True
            return table
        elif (table[0][0] == ' ' and table[1][1] == table[2][2] == signe):
            table[0][0] = signe
            a_joue = True
            return table
        
        elif (table[0][2] == table[1][1] == signe and  table[2][0] == ' '):
            table[2][0] = signe
            a_joue = True
            return table
        elif (table[2][0] == table[1][1] == signe and  table[0][2] == ' '):
            table[0][2] = signe
            a_joue = True
            return table
        elif (table[0][2] == table[2][0] == signe and  table[1][1] == ' '):
            table[1][1] = signe
            a_joue = True
            return table

        while a_joue == False:
            for i in range (0,3):
                if (table[0][i] == table[1][i] != ' ' and  table[2][i] == ' '):
                    table[2][i] = signe
                    a_joue = True
                    return table
                elif (table[0][i] == ' ' and table[1][i] == table[2][i] != ' '):
                    table[0][i] = signe
                    a_joue = True
                    return table
                elif (table[0][i] == table[2][i] != ' ' and table[1][i] == ' '):
                    table[1][i] = signe
                    a_joue = True
                    return table
            
            for i in range (0,3):
                if (table[i][0] == table[i][1] != ' ' and  table[i][2] == ' '):
                    table[i][2] = signe
                    a_joue = True
                    return table
                elif (table[i][0] == ' ' and table[i][1] == table[i][2] != ' '):
                    table[i][0] = signe
                    a_joue = True
                    return table
                elif (table[i][0] ==  table[i][2] != ' ' and table[i][1]== ' '):
                    table[i][1] = signe
                    a_joue = True
                    return table
            if (table[0][0] == table[1][1] != ' ' and  table[2][2] == ' '):
                table[2][2] = signe
                a_joue = True
                return table
            elif (table[0][0] == table[2][2] != ' ' and  table[1][1] == ' '):
                table[1][1] = signe
                a_joue = True
                return table
            elif (table[0][0] == ' ' and table[1][1] == table[2][2] != ' '):
                table[0][0] = signe
                a_joue = True
                return table
            
            elif (table[0][2] == table[1][1] != ' ' and  table[2][0] == ' '):
                table[2][0] = signe
                a_joue = True
                return table
            elif (table[2][0] == table[1][1] != ' ' and  table[0][2] == ' '):
                table[0][2] = signe
                a_joue = True
                return table
            elif (table[0][2] == table[2][0] != ' ' and  table[1][1] == ' '):
                table[1][1] = signe
                a_joue = True
                return table
        
            else:
                for i in range (0,3):
                    if (table[0][i] == signe and table[1][i] == ' ' and  table[2][i] == ' '):
                        if table[2][i] == ' ':
                            table[2][i] = signe
                            a_joue = True
                            return table
                        else:
                            table[1][i] = signe
                            a_joue = True
                            return table
                            
                    elif (table[0][i] == ' ' and table[2][i] == ' ' and table[1][i] == signe):
                        if table [0][i] == ' ':
                            table[0][i] = signe
                            a_joue = True
                            return table
                        else:
                            table[2][i] = signe
                            a_joue = True
                            return table

                    elif (table[2][i] == signe and table[0][i] == ' ' and table[1][i] == ' '):
                        if table[1][i] == ' ':
                            table[1][i] = signe
                            a_joue = True
                            return table
                        else:
                            table[0][i] = signe
                            a_joue = True
                            return table
                if table[0][2] == ' ':
                    table[0][2] = signe
                    a_joue = True
                    return table
                elif table[2][0] == ' ':
                    table[2][0] = signe
                    a_joue = True
                    return table
                elif table [2][2] == ' ':
                    table[2][2] = signe
                    a_joue = True
                    return table
                else :
                    for i in range (0,3):
                        for j in range (0,3):
                            if ( table[i][j] == " " ):
                                table[i][j] = signe
                                a_joue = True

    return table
    """Fonction permettant a l'ordinateur en mode 'Difficile' de jouer
    Entrée : Grille du morpion, signe à utiliser
    Sortie : Grille du morpion modifiée par le choix de l'ordinateur
    """

def difficulteBot() -> str:
    choix : int
    print("""
╔═══════════════════════════════════════╗
║      Difficulté de l'ordinateur:      ║
║                                       ║
║           1 - Facile                  ║
║                                       ║
║                                       ║
║           2 - Difficile               ║
║                                       ║
╚═══════════════════════════════════════╝

""")
    choix = saisieEntier("Votre choix : ")
    while choix != 1 and choix != 2 :
        print("Choix non valide.")
        choix = saisieEntier("Votre choix : ")
    if choix == 1:
        return "BotFac"
    if choix == 2:
        return "BotDif"
    """Fonction permettant de choisir la difficulté de l'ordinateur
    Entrée : None
    Sortie : nom de l'ordinateur choisi"""