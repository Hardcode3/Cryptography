# -*- coding:utf-8 -*-
__projet__ = "projet crypto"
__nom_fichier__ = "Code Che"
__author__ = "mon_Prénom mon_Nom"
__date__ = "novembre 2021"

from classes_et_fonctions.decryptage_code_che import *

list_code = [6, 38, 32, 4, 8, 30, 36, 34, 39, 31, 78, 72, 70, 76, 9, 79, 71, 58, 2, 0, 52, 50, 56, 54, 1, 59, 55]
list_lettre = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
               "V", "W", "X", "Y", "Z", " "]
# on rajoute le code 55 pour l'espace, puisque ni le 5 ni le 55 n'est utilisé pour coder une lettre


def substitution(message):
    """transforme les lettres en nombres et découpe le code en blocs de 5 chiffres"""

    message_code = []
    # on traduit les lettres en nombres
    for lettre in message:
        for i in range(len(list_lettre)):
            if lettre == list_lettre[i]:
                message_code.append(list_code[i])


    # on découpe le message en blocs de 5 chiffres, ou 6 pour ne pas couper une lettre codée par un nombre de 2 chiffres
    code_decoupe = []
    bloc = ""
    k = 0
    for code in message_code:
        # tant que le bloc contient moins de 5 chiffres
        if k < 5:
            # on rajoute le code suivant
            bloc += str(code)
            k += len(str(code))

        # si le bloc contient au moins 5 chiffres
        if k >= 5:
            # on le rajoute et on commence le nouveau bloc
            code_decoupe.append(bloc)
            bloc = ""
            k = 0

    # si le dernier bloc n'est pas vide
    if bloc != "":
        # on le transforme en bloc à 5 chiffres en rajoutant des 3 derrière (utile pour le décodage, car le code 3 ou 33 n'existe pas)
        x = len(bloc)
        bloc += (5-x) * '3'
        # new_bloc += bloc
        code_decoupe.append(bloc)

    return code_decoupe


def separer(bloc):
    """sépare un bloc en une liste de chacun des chiffres composant le bloc"""

    list_bloc = []
    for elt in bloc:
        list_bloc.append(int(elt))
    return list_bloc


def codage_bloc(bloc, cle):
    """code un bloc en l'additionnant avec un cle modulo 10"""

    list_bloc = separer(bloc)
    list_bloc_code = []

    if len(list_bloc) > len(cle):
        # si le bloc est de longueur 6, on rajoute un 0 devant la cle pour que les 2 listes aient la meme longueur
        cle_copy = cle
        cle = [0]
        cle += cle_copy

    for i in range(0, len(list_bloc)):

        x = list_bloc[i] + cle[i]

        # si la somme est supérieure à 10, on soustrait 10 pour ne garder que le chiffre des unités
        if len(str(x)) > 1:
            x -= 10

        list_bloc_code.append(x)

    return list_bloc_code



if __name__ == '__main__':
    print(substitution("BAPTISTE"))
    # print(separer('383230'))
    # print(codage_bloc('127456', '56853'))
    #print(codage('LA GEOCHIMIE C EST LONG', '12345'))
