from typing import List
from fonctionPuissance4 import affGrille,mettreDansCase,choixMenu,verifPlaceGrille,verifVictoire,verdict,verdictBot,botNorm,botDif,difficulteBot
class joueur :
    pseudo : str
    score_devinette : int
    score_allumette : int
    score_morpion : int
    score_puissance4 : int

def puissance4 (joueur1 : joueur, joueur2 : joueur):
    """Procédure permettant de jouer au jeu du puissance 4
    Entrée : Joueur1, Joueur2
    Sortie : score_puissance4 du joueur 1, score_puissance4 du joueur 2
    """
    fin : bool
    fin = False
    check : int
    check = 1
    pseudoJ1 : str
    pseudoJ1 = joueur1.pseudo
    pseudoJ2 : str
    pseudoJ2 = joueur2.pseudo
    scoreJ1 : int
    scoreJ1 = joueur1.score_puissance4
    scoreJ2 : int
    scoreJ2 = joueur2.score_puissance4
    choixDeroulement : int
    quiJoue : int
    quiJoue = 1
    grille : List[List[str]]
    grille = [[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']]
    choixDeroulement = choixMenu()

    while (choixDeroulement !=1 or choixDeroulement !=2 or choixDeroulement !=3 or choixDeroulement !=4) and fin == False:
        if choixDeroulement == 1:
            affGrille(grille)
            quiJoue = 1
            while check == 1 :
                if quiJoue == 1:
                    print(pseudoJ1,"commence.")
                    grille = mettreDansCase(grille,quiJoue)
                    affGrille(grille)
                    quiJoue = 2
                    check = verifPlaceGrille(grille)
                elif quiJoue == 2:
                    print(pseudoJ2,"joue.")
                    grille = mettreDansCase(grille,quiJoue)
                    quiJoue = 3
                    check = verifPlaceGrille(grille)
                    affGrille(grille)
                    if check == 1:
                        check = verifVictoire(grille)
                elif quiJoue == 3:
                    print(pseudoJ1,"joue.")
                    grille = mettreDansCase(grille,quiJoue)
                    quiJoue = 2
                    check = verifPlaceGrille(grille)
                    affGrille(grille)
                    if check == 1:
                        check = verifVictoire(grille)

            scoreJ1,scoreJ2 = verdict(quiJoue,scoreJ1,scoreJ2,pseudoJ1,pseudoJ2,check)
            choixDeroulement = 4

        if choixDeroulement == 2:
            pseudoJ1 = "Joueur"
            pseudoJ2 = difficulteBot()
            if pseudoJ2 == "BotFac":
                affGrille(grille)
                quiJoue = 1
                while check == 1 :
                    if quiJoue == 1:
                        print(pseudoJ1,"commence.")
                        grille = mettreDansCase(grille,quiJoue)
                        affGrille(grille)
                        quiJoue = 2
                        check = verifPlaceGrille(grille)
                    elif quiJoue == 2:
                        print(pseudoJ2,"joue.")
                        grille = botNorm(grille,quiJoue)
                        quiJoue = 3
                        check = verifPlaceGrille(grille)
                        affGrille(grille)
                        if check == 1:
                            check = verifVictoire(grille)
                    elif quiJoue == 3:
                        print(pseudoJ1,"joue.")
                        grille = mettreDansCase(grille,quiJoue)
                        quiJoue = 2
                        check = verifPlaceGrille(grille)
                        affGrille(grille)
                        if check == 1:
                            check = verifVictoire(grille)
                verdictBot(quiJoue,pseudoJ1,pseudoJ2,check)
                
            if pseudoJ2 == "BotDif":
                affGrille(grille)
                quiJoue = 1
                while check == 1 :
                    if quiJoue == 1:
                        print(pseudoJ1,"commence.")
                        grille = mettreDansCase(grille,quiJoue)
                        affGrille(grille)
                        quiJoue = 2
                        check = verifPlaceGrille(grille)
                    elif quiJoue == 2:
                        print(pseudoJ2,"joue.")
                        grille = botDif(grille,quiJoue)
                        quiJoue = 3
                        check = verifPlaceGrille(grille)
                        affGrille(grille)
                        if check == 1:
                            check = verifVictoire(grille)
                    elif quiJoue == 3:
                        print(pseudoJ1,"joue.")
                        grille = mettreDansCase(grille,quiJoue)
                        quiJoue = 2
                        check = verifPlaceGrille(grille)
                        affGrille(grille)
                        if check == 1:
                            check = verifVictoire(grille)
                verdictBot(quiJoue,pseudoJ1,pseudoJ2,check)
            choixDeroulement = 4

        if choixDeroulement == 3 :
            pseudoJ1 = "Bot1"
            pseudoJ2 = "Bot2"
            print("\nLes ordinateurs jouant seront en difficulté 'Difficile' par choix du créateur.\n\n")
            affGrille(grille)
            quiJoue = 1
            while check == 1 :
                if quiJoue == 1:
                    print(pseudoJ1,"commence.")
                    grille = botDif(grille,quiJoue)
                    affGrille(grille)
                    quiJoue = 2
                    check = verifPlaceGrille(grille)
                elif quiJoue == 2:
                    print(pseudoJ2,"joue.")
                    grille = botDif(grille,quiJoue)
                    quiJoue = 3
                    check = verifPlaceGrille(grille)
                    affGrille(grille)
                    if check == 1:
                        check = verifVictoire(grille)
                elif quiJoue == 3:
                    print(pseudoJ1,"joue.")
                    grille = botDif(grille,quiJoue)
                    quiJoue = 2
                    check = verifPlaceGrille(grille)
                    affGrille(grille)
                    if check == 1:
                        check = verifVictoire(grille)

            verdictBot(quiJoue,pseudoJ1,pseudoJ2,check)
            choixDeroulement = 4

        elif choixDeroulement == 4:
            print("Au revoir !")
            fin = True

        else:
            print("Choix non conforme.\nRéessayez s'il vous plaît.")
            choixDeroulement = choixMenu()

    return scoreJ1,scoreJ2

joueur1 : joueur
joueur2 : joueur
joueur1 = joueur()
joueur2 = joueur()
joueur1.pseudo = "Quelqu'un"
joueur2.pseudo = "Quelqu'deux"
joueur1.score_puissance4 = 0
joueur2.score_puissance4 = 0
joueur1.score_puissance4,joueur2.score_puissance4 = puissance4(joueur1,joueur2)
print("Score J1 :",joueur1.score_puissance4)
print("Score J2 :",joueur2.score_puissance4)