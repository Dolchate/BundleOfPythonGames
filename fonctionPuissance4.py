from random import randint
from typing import List
from Module.saisie import saisieEntier
from time import sleep

def affGrille(tab : List[List[str]]):
    """
    Procedure permettant d'afficher la grille du morpion
    Entrée : Grille
    Sortie : None
    """
    print("\n\033[1;34m╔════╦════╦════╦════╦════╦════╦════╗")
    print("║",tab[0][0]," ║",tab[0][1]," ║",tab[0][2]," ║",tab[0][3]," ║",tab[0][4]," ║",tab[0][5]," ║",tab[0][6]," ║")
    print("╠════╬════╬════╬════╬════╬════╬════╣")
    print("║",tab[1][0]," ║",tab[1][1]," ║",tab[1][2]," ║",tab[1][3]," ║",tab[1][4]," ║",tab[1][5]," ║",tab[1][6]," ║")
    print("╠════╬════╬════╬════╬════╬════╬════╣")
    print("║",tab[2][0]," ║",tab[2][1]," ║",tab[2][2]," ║",tab[2][3]," ║",tab[2][4]," ║",tab[2][5]," ║",tab[2][6]," ║")
    print("╠════╬════╬════╬════╬════╬════╬════╣")
    print("║",tab[3][0]," ║",tab[3][1]," ║",tab[3][2]," ║",tab[3][3]," ║",tab[3][4]," ║",tab[3][5]," ║",tab[3][6]," ║")
    print("╠════╬════╬════╬════╬════╬════╬════╣")
    print("║",tab[4][0]," ║",tab[4][1]," ║",tab[4][2]," ║",tab[4][3]," ║",tab[4][4]," ║",tab[4][5]," ║",tab[4][6]," ║")
    print("╠════╬════╬════╬════╬════╬════╬════╣")
    print("║",tab[5][0]," ║",tab[5][1]," ║",tab[5][2]," ║",tab[5][3]," ║",tab[5][4]," ║",tab[5][5]," ║",tab[5][6]," ║")
    print("╚════╩════╩════╩════╩════╩════╩════╝"+"\033[0m")

def verifCase(colonne : int, ligne : int, grille : List[List[str]]) -> bool:
    """Fonction permettant de savoir si la case suivante est disponible pour faire 'tomber' le jeton une case plus bas 
    Entrée : colonne choisie, ligne choisie, grille du puissance 4
    Sortie : 
            Booléen :
                Vrai -> La prochaine case est disponible
                Faux -> La prochaine case n'est pas disponible"""
    caseOk : bool

    caseOk = False

    if grille[ligne+1][colonne] == ' ':
        caseOk = True
    if grille[ligne+1][colonne] != ' ':
        if ligne == 0 and grille[ligne][colonne] == ' ':
            caseOk = True
    
    if ligne > 5 or ligne < 0:
        caseOk = False
    if grille[0][colonne] != ' ':
        caseOk = False

    return caseOk

def choixColonne()-> int:
    """
    Fonction permettant au joueur de rentrer la colonne dans laquel il veut placer son jeton
    Entrée : None
    Sortie : Numéro de la colonne"""
    numero : int
    numero = saisieEntier("Choisisez la colonne : ")
    while numero > 7 or numero < 1:
        print("Choix invalide, case non comforme.")
        numero = saisieEntier("Choisisez la colonne : ")
    return numero-1

def mettreDansCase(grille : List[List[str]],quiJoue : int) -> List[List[str]]:
    """
    Fonction permettant de mettre le jeton dans la colonne choisie au bon emplacement
    Entrée : Grille du morpion, quel joueur joue
    Sortie : Grille du morpion modifiée"""
    colonne : int
    caseOK : bool
    case : str
    ligne : int
    
    if quiJoue == 1 or quiJoue == 3:
        case = "\033[1;31m◯\033[1m"+"\033[1;34m"
    elif quiJoue == 2:
        case = "\033[1;33m◯\033[1m"+"\033[1;34m"
    else :
        print("AAAAAAAA PAS PREVU OSCOUR \nLa case n'est pas définie car le joueur jouant est invalide.")

    ligne = 0
    colonne = choixColonne()
    caseOK = verifCase(colonne,ligne,grille)
  
    while caseOK == False:
        print("Colonne choisie invalide. \nVeuillez en choisir une autre.")
        colonne = choixColonne()
        caseOK = verifCase(colonne,ligne,grille)
          
    while caseOK:
        if grille[ligne+1][colonne] == ' ':
            grille[ligne][colonne] = ' '
            ligne = ligne +1
            grille[ligne][colonne] = case
        elif ligne == 0:
            grille[ligne][colonne] = case

        if ligne < 5:
            caseOK = verifCase(colonne,ligne,grille)
        else:
            caseOK = False

    return grille

def choixMenu() -> int :
    """Procédure permettant de choisir le mode de jeu
    Entrée : None
    Sortie : Choix du mode de jeu choisi
    """

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

def verifPlaceGrille(grille : List[List[str]]) -> int:
    """Fonction verifiant que la grille n'est pas remplie
    Entrée : Grille du puissance 4
    Sortie : 
            id en fonction des tests :
                1 -> il reste de la place
                2 -> il ne reste pas de place"""
    i : int
    j : int
    for i in range(0,6):
        for j in range(0,7):
            if ( grille[i][j] == " " ):
                return 1
    return 0

def regarderhaut(grille : List[List[str]], ligne : int, colonne : int)->bool:
    """Fonction permettant de regarder au dessus d'un jeton donné et voir si la disposition 
    des jetons permet à l'un des participants de gangner.
    Entrée : grille du puissance 4, numéro de la ligne de la case, numéro de la colonne de la case
    Sortie :
            Booléen :
                False -> Aucun participants n'a gagné à ce tour
                True -> Un participant à gagné à ce tour
    """
    win : bool
    win = False
    if grille[ligne][colonne] == grille[ligne-1][colonne] == grille[ligne-2][colonne] == grille[ligne-3][colonne]:
        win = True
    return win

def regarderdroite(grille : List[List[str]], ligne : int, colonne : int)->bool:
    """Fonction permettant de regarder à droite d'un jeton donné et voir si la disposition 
    des jetons permet à l'un des participants de gangner.
    Entrée : grille du puissance 4, numéro de la ligne de la case, numéro de la colonne de la case
    Sortie :
            Booléen :
                False -> Aucun participants n'a gagné à ce tour
                True -> Un participant à gagné à ce tour
    """

    win : bool
    win = False
    if grille[ligne][colonne] == grille[ligne][colonne+1] == grille[ligne][colonne+2] == grille[ligne][colonne+3]:

        win = True
    return win

def regarderhautdroite(grille : List[List[str]], ligne : int, colonne : int)->bool:
    """Fonction permettant de regarder au dessus à droite (diagonale) d'un jeton donné et voir si la disposition 
    des jetons permet à l'un des participants de gangner.
    Entrée : grille du puissance 4, numéro de la ligne de la case, numéro de la colonne de la case
    Sortie :
            Booléen :
                False -> Aucun participants n'a gagné à ce tour
                True -> Un participant à gagné à ce tour
    """
    
    win : bool
    win = False
    if grille[ligne][colonne] == grille[ligne-1][colonne+1] == grille[ligne-2][colonne+2] == grille[ligne-3][colonne+3]:
        win = True
    return win

def regarderhautgauche(grille : List[List[str]], ligne : int, colonne : int)->bool:
    """Fonction permettant de regarder au dessus à gauche (diagonale) d'un jeton donné et voir si la disposition 
    des jetons permet à l'un des participants de gangner.
    Entrée : grille du puissance 4, numéro de la ligne de la case, numéro de la colonne de la case
    Sortie :
            Booléen :
                False -> Aucun participants n'a gagné à ce tour
                True -> Un participant à gagné à ce tour
    """
    win : bool
    win = False
    if grille[ligne][colonne] == grille[ligne-1][colonne-1] == grille[ligne-2][colonne-2] == grille[ligne-3][colonne-3]:
        win = True
    return win

def verifVictoire(grille : List[List[str]])-> int:
    """Fonction permettant de savoir si un participant à gagné en fonction de différentes autres fonctions
    Entrée : Grille du puissance 4
    Sortie : 
            id en fonction des résultats :
                1 -> Aucun participants n'a gagné
                2 -> Un participants n'a gagné"""
    win : bool
    win = False
    i : int
    j : int
    for i in range(5,-1,-1):
        for j in range(7):
            if ( grille[i][j] != " " ):
                if i>2:
                    win = regarderhaut(grille, i, j)
                if win == False and j<4:
                    win = regarderdroite(grille, i, j)
                if win == False and i>2 and j<4:
                    win = regarderhautdroite(grille, i, j)
                if win == False and i>2 and j>2:
                    win = regarderhautgauche(grille, i, j)
                if win == True:
                    return 0
    return 1

def verdict(quiJoue : int, scoreJ1 : int, scoreJ2 : int, pseudoJ1 : str, pseudoJ2 : str, check : int):
    """Procédure permettant de rendre le verdict de la partie 
    d'un joueur contre un autre, ajoutant au score du joueur gagnant.
    Entrée : l'id du joueur qui aurait joué après, le pseudo du joueur 1, le pseudo du joueur 2, le score du joueur 1, le score du joueur 2,
             un check qui permet de savoir si la grille est remplie
    Sortie : le score du joueur 1, le score du joueur 2"""

    if check == 0 and quiJoue == 2:
        print("Bien joué à",pseudoJ1+", c'est une victoire !")
        return scoreJ1+1,scoreJ2
    elif check == 0 and quiJoue == 3:
        print("Bien joué à",pseudoJ2+", c'est une victoire !")
        return scoreJ1,scoreJ2+1
    else:
        print("Aucun vainqueur, bien joué à tous !")
        return scoreJ1,scoreJ2

def verdictBot(quiJoue : int, pseudoJ1 : str, pseudoJ2 : str, check : int):
    """Procédure permettant de rendre le verdict de la partie dans tous les modes 
    de jeu a l'exception du mode Joueur VS Joueur
    Entrée : l'id du joueur qui aurait joué après, le pseudo du joueur 1, le pseudo du joueur 2,
             un check qui permet de savoir si la grille est remplie
    Sortie : None"""

    if check == 0 and quiJoue == 2:
        print("Bien joué à",pseudoJ1+", c'est une victoire !")

    elif check == 0 and quiJoue == 3:
        print("Bien joué à",pseudoJ2+", c'est une victoire !")

    else:
        print("Aucun vainqueur, bien joué à tous !")

def botNorm(grille : List[List[str]], quiJoue : int) -> List[List[str]]:
    """Fonction permettant à l'ordinateur en mode 'Normal' de jouer
    Entrée : Grille du puissance 4, l'id du joueur qui aurait joué après 
    Sortie : Grille du morpion modifiée"""
    colonne : int
    caseOK : bool
    case : str
    ligne : int


    if quiJoue == 1 or quiJoue == 3:
        case = "\033[1;31m◯\033[1m"+"\033[1;34m"
    elif quiJoue == 2:
        case = "\033[1;33m◯\033[1m"+"\033[1;34m"
    else :
        print("AAAAAAAA PAS PREVU OSCOUR \nLa case n'est pas définie car le joueur jouant est invalide.")

    ligne = 0
    colonne = randint(0,6)
    caseOK = verifCase(colonne,ligne,grille)
  
    while caseOK == False:
        colonne = randint(0,6)
        caseOK = verifCase(colonne,ligne,grille)
    print("Choix de l'ordinateur :",colonne)
    while caseOK:
        if grille[ligne+1][colonne] == ' ':
            grille[ligne][colonne] = ' '
            ligne = ligne +1
            grille[ligne][colonne] = case
        elif ligne == 0:
            grille[ligne][colonne] = case

        if ligne < 5:
            caseOK = verifCase(colonne,ligne,grille)
        else:
            caseOK = False
    sleep(0.5)
    return grille

def verif3Cases(grille : List[List[str]], colonne : int)->int:
    """Fonction permettant de gérer le comportement de l'ordinateur en difficulté 'Difficile'
    en fontion des jetons placés dans la grille.
    Entrée : Grille du puissance 4, colonne choisie aléatoirement dans le cas où il n'y à pas de changement
    Sortie : Colonne choisie """
    i : int
    j : int
    rangee : bool
    rangee = False
    for i in range(5,-1,-1):
        for j in range(0,7):
            if ( grille[i][j] != " " ):
                if i>2 and grille[i][j] == grille[i-1][j] == grille[i-2][j] and grille[i-3][j] == ' ':
                    colonne = j
                    rangee = True

                if rangee == False and j<4 and grille[i][j] == grille[i][j+1] == grille[i][j+2] and grille[i][j+3] == ' ':
                    if i == 5 :
                        colonne = j+3
                        rangee = True
                    elif i < 5 and grille[i+1][j+3] != ' ':
                        colonne = j+3
                        rangee = True

                if rangee == False and j<5 and j>0 and grille[i][j] == grille[i][j+1] == grille[i][j+2] and grille[i][j-1] == ' ':
                    if i == 5 :
                        colonne = j-1
                        rangee = True
                    elif i < 5 and grille[i+1][j-1] != ' ':
                        colonne = j-1
                        rangee = True

                if rangee == False and j<4 and grille[i][j] == grille[i][j+3] == grille[i][j+2] and grille[i][j+1] == ' ':
                    if i == 5 :
                        colonne = j+1
                        rangee = True
                    elif i < 5 and grille[i+1][j+1] != ' ':
                        colonne = j+1
                        rangee = True

                if rangee == False and j<4 and grille[i][j] == grille[i][j+3] == grille[i][j+1] and grille[i][j+2] == ' ':
                    if i == 5 :
                        colonne = j+2
                        rangee = True
                    elif i < 5 and grille[i+1][j+2] != ' ':
                        colonne = j+2
                        rangee = True

                if rangee == False and i>2 and j<4 and grille[i][j] == grille[i-1][j+1] == grille[i-2][j+2] and grille[i-2][j+3] != ' ' and grille[i-3][j+3] == ' ':
                    colonne = j+3
                    rangee = True

                if rangee == False and i>1 and i<5 and j<5 and j>0 and grille[i][j] == grille[i-1][j+1] == grille[i-2][j+2] and grille[i-2][j-1] != ' ' :
                    if i+1 < 5 and grille[i+1][j-1] == ' ':
                        colonne = j-1
                        rangee = True
                    elif i+1 == 5 :
                        colonne = j-1
                        rangee = True

                if rangee == False and i>2 and j<4 and grille[i][j] == grille[i-1][j+1] == grille[i-3][j+3] and grille[i-1][j+2] != ' ' and grille[i-2][j+2] == ' ':
                    colonne = j+2
                    rangee = True

                if rangee == False and i>2 and j<4 and grille[i][j] == grille[i-2][j+2] == grille[i-3][j+3] and grille[i][j+1] != ' ' and grille[i-1][j+1] == ' ':
                    colonne = j+1
                    rangee = True

                if rangee == False and i>2 and j>2 and grille[i][j] == grille[i-1][j-1] == grille[i-2][j-2] and grille[i-2][j-3] != ' ' and grille[i-3][j-3] == ' ':
                    colonne = j-3
                    rangee = True

                if rangee == False and i>1 and i<5 and j>1 and j<6 and grille[i][j] == grille[i-1][j-1] == grille[i-2][j-2] and grille[i-2][j+1] != ' ' :
                    if i+1 < 5 and grille[i+1][j+1] == ' ':
                        colonne = j+1
                        rangee = True
                    elif i+1 == 5 :
                        colonne = j+1
                        rangee = True

                if rangee == False and i>2 and j>2 and grille[i][j] == grille[i-1][j-1] == grille[i-3][j-3] and grille[i-1][j-2] != ' ' and grille[i-2][j-2] == ' ':
                    colonne = j-2
                    rangee = True

                if rangee == False and i>2 and j>2 and grille[i][j] == grille[i-2][j-2] == grille[i-3][j-3] and grille[i][j-1] != ' ' and grille[i-1][j-1] == ' ':
                    colonne = j-1
                    rangee = True

                if rangee :
                    return colonne
    return colonne

def botDif(grille : List[List[str]], quiJoue : int) -> List[List[str]]:
    """Fonction permettant à l'ordinateur en mode 'Difficile' de jouer
    Entrée : Grille du puissance 4, l'id du joueur qui aurait joué après 
    Sortie : Grille du morpion modifiée"""
    colonne : int
    caseOK : bool
    case : str
    ligne : int


    if quiJoue == 1 or quiJoue == 3:
        case = "\033[1;31m◯\033[1m"+"\033[1;34m"
    elif quiJoue == 2:
        case = "\033[1;33m◯\033[1m"+"\033[1;34m"
    else :
        print("La case n'est pas définie car le joueur jouant est invalide.")

    ligne = 0
    colonne = randint(0,6)
    caseOK = verifCase(colonne,ligne,grille)
    print("Choix de l'ordinateur (avant verif):",colonne+1)


    while caseOK == False:
        colonne = randint(0,6)
        caseOK = verifCase(colonne,ligne,grille)

    colonne = verif3Cases(grille,colonne)

    print("Choix de l'ordinateur (apres verif):",colonne+1)


    while caseOK:
        if grille[ligne+1][colonne] == ' ':
            grille[ligne][colonne] = ' '
            ligne = ligne +1
            grille[ligne][colonne] = case
        elif ligne == 0:
            grille[ligne][colonne] = case

        if ligne < 5:
            caseOK = verifCase(colonne,ligne,grille)
        else:
            caseOK = False

    sleep(0.5)
    return grille


def difficulteBot() -> str:
    """Fonction permettant de choisir la difficulté de l'ordinateur
    Entrée : None
    Sortie : nom de l'ordinateur choisi"""
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