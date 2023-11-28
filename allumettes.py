from Fonctions_Allumettes import choixJoueur, deroulementBotNorm, difficulteBot, menuBots,deroulement,affAll,verdict,deroulementBotImp,changeNbAll,verdictJvJ
class joueur :
    pseudo : str
    score_devinette : int
    score_allumette : int
    score_morpion : int


def allumettes(J1 : joueur, J2 : joueur):

    pseudoJ1 : str
    pseudoJ2 : str
    scoreJ1 : int    
    scoreJ2 : int    

    pseudoJ1 = J1.pseudo
    pseudoJ2 = J2.pseudo
    scoreJ1 = J1.score_allumette
    scoreJ2 = J2.score_allumette
    nbAll : int
    quelJoueurJoue : int
    modeDeJeu : int
    varTemp : str

    print("Il y a 20 allumettes de base, vous en tirerez chacun 1, 2 ou 3 a chaque tours.")
    print("Le but est de faire prendre à l'adversaire la dernière allumette.\n")


    nbAll = changeNbAll()
    print("\nNombre d'allumettes :",nbAll)
    modeDeJeu = menuBots()

    if modeDeJeu == 4:
        print("Au revoir")

    elif modeDeJeu == 1 :
        quelJoueurJoue = 0
        print()
        affAll(nbAll)
        print()
        while nbAll > 0:

            if quelJoueurJoue == 0:
                print(pseudoJ1,"commence.")
                nbAll = deroulement(nbAll)
                quelJoueurJoue = 2
                print()

            elif quelJoueurJoue == 1:
                print(pseudoJ1,"joue.")
                nbAll = deroulement(nbAll)
                quelJoueurJoue = 2
                print()
                
            elif quelJoueurJoue == 2:
                print(pseudoJ2,"joue.")
                nbAll = deroulement(nbAll)
                quelJoueurJoue = 1
                print()
                
        scoreJ1,scoreJ2 = verdictJvJ(quelJoueurJoue,pseudoJ1,pseudoJ2,scoreJ1,scoreJ2)
        return scoreJ1,scoreJ2
    elif modeDeJeu == 2 :
        quelJoueurJoue = 0


        pseudoJ1 = choixJoueur(pseudoJ1,pseudoJ2)
        pseudoJ2 = difficulteBot()
        print(pseudoJ2)
        
        if (nbAll+3)%4 != 0:
            if pseudoJ2 == "BotImp" :
                varTemp = pseudoJ1
                pseudoJ1 = pseudoJ2
                pseudoJ2 = varTemp

        print()
        affAll(nbAll)
        print()

        if pseudoJ2 == "BotImp" or pseudoJ1 =="BotImp" :
            if pseudoJ1 =="BotImp" :
                while nbAll > 0:

                    if quelJoueurJoue == 0:
                        print(pseudoJ1,"commence.")
                        nbAll = deroulementBotImp(nbAll)
                        quelJoueurJoue = 2
                        print()

                    elif quelJoueurJoue == 1:
                        print(pseudoJ1,"joue.")
                        nbAll = deroulementBotImp(nbAll)
                        quelJoueurJoue = 2
                        print()

                    elif quelJoueurJoue == 2:
                        print(pseudoJ2,"joue.")
                        nbAll = deroulement(nbAll)
                        quelJoueurJoue = 1
                        print()
            else:
                while nbAll > 0:

                    if quelJoueurJoue == 0:
                        print(pseudoJ1,"commence.")
                        nbAll = deroulement(nbAll)
                        quelJoueurJoue = 2
                        print()

                    elif quelJoueurJoue == 1:
                        print(pseudoJ1,"joue.")
                        nbAll = deroulement(nbAll)
                        quelJoueurJoue = 2
                        print()

                    elif quelJoueurJoue == 2:
                        print(pseudoJ2,"joue.")
                        nbAll = deroulementBotImp(nbAll)
                        quelJoueurJoue = 1
                        print()
        if pseudoJ2 == "BotNorm" :
            while nbAll > 0:

                if quelJoueurJoue == 0:
                    print(pseudoJ1,"commence.")
                    nbAll = deroulement(nbAll)
                    quelJoueurJoue = 2
                    print()

                elif quelJoueurJoue == 1:
                    print(pseudoJ1,"joue.")
                    nbAll = deroulement(nbAll)
                    quelJoueurJoue = 2
                    print()
                    
                elif quelJoueurJoue == 2:
                    print(pseudoJ2,"joue.")
                    nbAll = deroulementBotNorm(nbAll)
                    quelJoueurJoue = 1
                    print()

        verdict(quelJoueurJoue,pseudoJ1,pseudoJ2)
    elif modeDeJeu == 3:

        pseudoJ1 = "BotNorm1"
        pseudoJ2 = "BotNorm2"

        quelJoueurJoue = 0
        print("\nLes ordinateurs jouant seront en difficulté normale par choix du créateur.\n\n")

        print()
        affAll(nbAll)
        print()
        while nbAll > 0:
            
            if quelJoueurJoue == 0:
                print(pseudoJ1,"commence.")
                nbAll = deroulementBotNorm(nbAll)
                quelJoueurJoue = 2
                print()

            elif quelJoueurJoue == 1:
                print(pseudoJ1,"joue.")
                nbAll = deroulementBotNorm(nbAll)
                quelJoueurJoue = 2
                print()
                
            elif quelJoueurJoue == 2:
                print(pseudoJ2,"joue.")
                nbAll = deroulementBotNorm(nbAll)
                quelJoueurJoue = 1
                print()
                
        verdict(quelJoueurJoue,pseudoJ1,pseudoJ2)
    return scoreJ1,scoreJ2
    """Procédure permettant de jouer au jeu des allumettes
    Entrée : Joueur1, Joueur2
    Sortie : score_allumette du joueur 1, score_allumette du joueur 2
    """



joueur1 : joueur
joueur2 : joueur
joueur1 = joueur()
joueur2 = joueur()
joueur1.pseudo = "Aurèle"
joueur2.pseudo = "Mattéo"
joueur1.score_allumette = 0
joueur2.score_allumette = 0
joueur1.score_allumette,joueur2.score_allumette = allumettes(joueur1,joueur2)
print("Score J1 :",joueur1.score_allumette)
print("Score J2 :",joueur2.score_allumette)
