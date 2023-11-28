from typing import List

def saisieMatInt(nLig : int ,nCol : int)-> List[List[int]]:
    from Module.saisie import saisieEntier    
    i : int 
    j : int
    val : int
    mat : List[List[int]]
    val = 0

    mat = list([])
    for i in range (nLig):
        ligne : List[int]
        ligne = list()
        for j in range (nCol):
            val = saisieEntier("Saisir la valeur : ")
            ligne.append(val)
        mat.append(ligne)
    return mat
    """
    Fonction permettant la saisie des arguments d'une matrice 2D de chiffres
    Entrée : nombre de lignes
             nombre de colones
    Sortie : Matrice
    """


def afficherMatInt(mat : List[List[int]]):
    i : int
    j : int
    for i in range (len(mat)):
        for j in range (len(mat[0])):
            if mat[i][j]<10 and mat[i][j]>-10:
                if mat[i][j]<0:
                    print (' '+"-0"+str(abs(mat[i][j])),end='')
                else:
                    print ('  '+'0'+str(mat[i][j]),end='')
            else :
                if mat[i][j]<-10:
                    print (' '+str(mat[i][j]),end='')
                else:
                    print ('  '+str(mat[i][j]),end='')
        print ()
    """
    Procédure permettant d'afficher une matrice 2D de chiffres
    Entrée : Matrice
    """

def afficherMatStr(mat : List[List[str]]):
    i : int
    j : int
    for i in range (len(mat)):
        for j in range (len(mat[0])):
            print(mat[i][j],end='')
        print ()
    """
    Procédure permettant d'afficher une matrice 2D de chaines
    Entrée : Matrice
    """


def saisieMatStr(nLig : int ,nCol : int)-> List[List[str]]:
    from Module.saisie import saisieEntier    
    i : int 
    j : int
    val : str
    mat : List[List[str]]
    val = 0

    mat = list([])
    for i in range (nLig):
        ligne : List[str]
        ligne = list()
        for j in range (nCol):
            val = input("Saisir la valeur : ")
            ligne.append(val)
        mat.append(ligne)
    return mat
    """
    Fonction permettant la saisie des arguments d'une matrice 2D de chaines
    Entrée : nombre de lignes
             nombre de colones
    Sortie : Matrice
    """