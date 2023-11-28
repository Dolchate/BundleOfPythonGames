def saisieEntier (phrase : str) -> int:

    nbr : int
    verif : bool

    verif = True
    while verif :
        try :
            nbr = input(phrase)
            nbr =  int(nbr)
            verif = False
        except ValueError:
            print ("Rentrez une valeur valide.")
    return nbr
    """
    Fonction permetant de saisir un nombre entier et de verifier sa validité.
    Entrée : phrase (Phrase demandant le nombre)
    Sortie : nbr (Nombre entier comfirné)
    
    """
