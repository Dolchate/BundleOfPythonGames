from typing import List
from Fonctions_Morpion import *
from time import sleep
class joueur :
    pseudo : str
    score_devinette : int
    score_allumette : int
    score_morpion : int


def morpion(joueur1 : joueur, joueur2 : joueur):
    """Procédure permettant de jouer au jeu du morpion
    Entrée : Joueur1, Joueur2
    Sortie : score_morpion du joueur 1, score_morpion du joueur 2
    """
    
    choix : int
    quelJoueurJoue : int
    pseudoJ1 : str
    pseudoJ1 = joueur1.pseudo
    pseudoJ2 : str
    pseudoJ2 = joueur2.pseudo
    scoreJ1 : int
    scoreJ1 = joueur1.score_morpion
    scoreJ2 : int
    scoreJ2 = joueur2.score_morpion
    check : int
    check = 1
    print("Le jeux du morpion consiste à aligner 3 symboles \"O\" ou \"X\" sur une grille de 3 lignes et trois colonnes.")
    table : List[list[str]]
    table = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    choix = choixMenu()
    
    if choix == 1:
        affMorpion(table)
        quelJoueurJoue = 1
        while check == 1 :
            if quelJoueurJoue == 1:
                print(pseudoJ1,"commence.")
                signe = "\033[1;31mX\033[0m"
                table = saisieMorpion(table,signe)
                affMorpion(table)
                quelJoueurJoue = 2
                check = verif(table)
            elif quelJoueurJoue == 2:
                signe = "\033[1;34mO\033[0m"
                print(pseudoJ2,"joue.")
                table = saisieMorpion(table,signe)
                affMorpion(table)
                quelJoueurJoue = 3
                check = verif(table)
            elif quelJoueurJoue == 3:
                print(pseudoJ1,"joue.")
                signe = "\033[1;31mX\033[0m"
                table = saisieMorpion(table,signe)
                affMorpion(table)
                quelJoueurJoue = 2
                check = verif(table)

        scoreJ1,scoreJ2 = verdict(quelJoueurJoue,scoreJ1,scoreJ2,pseudoJ1,pseudoJ2,check)

    elif choix == 2 :
        quelJoueurJoue = 1
        pseudoJ1 = "Le joueur"
        pseudoJ2 = difficulteBot()
        affMorpion(table)
        if pseudoJ2 == "BotFac":
            while check == 1 :
                if quelJoueurJoue == 1:
                    print(pseudoJ1,"commence.")
                    signe = "\033[1;31mX\033[0m"
                    table = saisieMorpion(table,signe)
                    affMorpion(table)
                    quelJoueurJoue = 2
                    check = verif(table)
                elif quelJoueurJoue == 2:
                    signe = "\033[1;34mO\033[0m"
                    print(pseudoJ2,"joue.")
                    sleep(1)
                    table = botNorm(table,signe)
                    affMorpion(table)
                    quelJoueurJoue = 3
                    check = verif(table)
                elif quelJoueurJoue == 3:
                    print(pseudoJ1,"joue.")
                    signe = "\033[1;31mX\033[0m"
                    table = saisieMorpion(table,signe)
                    affMorpion(table)
                    quelJoueurJoue = 2
                    check = verif(table)
        else:
            while check == 1 :
                if quelJoueurJoue == 1:
                    print(pseudoJ1,"commence.")
                    signe = "\033[1;31mX\033[0m"
                    table = saisieMorpion(table,signe)
                    affMorpion(table)
                    quelJoueurJoue = 2
                    check = verif(table)
                elif quelJoueurJoue == 2:
                    signe = "\033[1;34mO\033[0m"
                    print(pseudoJ2,"joue.")
                    sleep(1)
                    table = botDif(table,signe)
                    affMorpion(table)
                    quelJoueurJoue = 3
                    check = verif(table)
                elif quelJoueurJoue == 3:
                    print(pseudoJ1,"joue.")
                    signe = "\033[1;31mX\033[0m"
                    table = saisieMorpion(table,signe)
                    affMorpion(table)
                    quelJoueurJoue = 2
                    check = verif(table)
        verdictBot(quelJoueurJoue,pseudoJ1,pseudoJ2,check)

    elif choix == 3 :
        quelJoueurJoue = 1
        pseudoJ1 = difficulteBot()
        pseudoJ2 = pseudoJ1+"2"
        pseudoJ1 = pseudoJ1+"1"
        affMorpion(table)
        if pseudoJ1 == "BotFac1":
            while check == 1 :
                if quelJoueurJoue == 1:
                    signe = "\033[1;31mX\033[0m"
                    print(pseudoJ1,"commence.")
                    sleep(1)
                    table = botNorm(table,signe)
                    affMorpion(table)
                    quelJoueurJoue = 2
                    check = verif(table)
                elif quelJoueurJoue == 2:
                    signe = "\033[1;34mO\033[0m"
                    print(pseudoJ2,"joue.")
                    sleep(1)
                    table = botNorm(table,signe)
                    affMorpion(table)
                    quelJoueurJoue = 3
                    check = verif(table)
                elif quelJoueurJoue == 3:
                    print(pseudoJ1,"joue.")
                    signe = "\033[1;31mX\033[0m"
                    sleep(1)
                    table = botNorm(table,signe)
                    affMorpion(table)
                    quelJoueurJoue = 2
                    check = verif(table)
        else:
            while check == 1 :
                if quelJoueurJoue == 1:
                    signe = "\033[1;31mX\033[0m"
                    print(pseudoJ1,"commence.")
                    sleep(1)
                    table = botDif(table,signe)
                    affMorpion(table)
                    quelJoueurJoue = 2
                    check = verif(table)
                elif quelJoueurJoue == 2:
                    signe = "\033[1;34mO\033[0m"
                    print(pseudoJ2,"joue.")
                    sleep(1)
                    table = botDif(table,signe)
                    affMorpion(table)
                    quelJoueurJoue = 3
                    check = verif(table)
                elif quelJoueurJoue == 3:
                    print(pseudoJ1,"joue.")
                    signe = "\033[1;31mX\033[0m"
                    sleep(1)
                    table = botDif(table,signe)
                    affMorpion(table)
                    quelJoueurJoue = 2
                    check = verif(table)
                
        verdictBot(quelJoueurJoue,pseudoJ1,pseudoJ2,check)
    elif choix == 4:
        print("Au plaisir de vous revoir !")
    return scoreJ1,scoreJ2

joueur1 : joueur
joueur2 : joueur
joueur1 = joueur()
joueur2 = joueur()
joueur1.pseudo = "Quelqu'un"
joueur2.pseudo = "Quelqu'deux"
joueur1.score_morpion = 0
joueur2.score_morpion = 0
joueur1.score_morpion,joueur2.score_morpion = morpion(joueur1,joueur2)
print("Score J1 :",joueur1.score_morpion)
print("Score J2 :",joueur2.score_morpion)