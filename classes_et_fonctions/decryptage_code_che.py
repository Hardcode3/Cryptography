# -*- coding:utf-8 -*-
__projet__ = "Code Che.py"
__nom_fichier__ = "decryptage_code_che"
__author__ = "mon_Prénom mon_Nom"
__date__ = "décembre 2021"

from classes_et_fonctions.code_che import *

def decryptage_bloc(bloc, cle):
    """décrypte un bloc codé"""

    list_cle = separer(str(cle))

    if len(bloc) > len(list_cle):
        # si le bloc est de longueur 6, on rajoute un 0 devant la cle pour que les 2 listes aient la meme longueur
        cle_copy = list_cle
        list_cle = [0]
        list_cle += cle_copy

    else :
        list_cle = list_cle

    bloc_decode = []

    for i in range(len(bloc)):

        x = bloc[i] - list_cle[i]

        # si la soustraction est négative
        if x < 0:
            # on ajoute 10
            x += 10

        bloc_decode.append(x)

    return bloc_decode

def conversion_bloc(bloc):
    """convertit un bloc en lettres"""

    new_bloc = ""
    for elt in bloc:
        new_bloc += str(elt)
    bloc_deco = []
    k = 0
    while k < len(bloc):
        cte = k
        for i in range(len(list_code)):

            # si le dernier chiffre est un 3
            if bloc[k] == 3 and k == len(bloc) - 1:
                # alors le message est décodé
                bloc_final = ""
                for lettre in bloc_deco:
                    bloc_final += lettre
                return bloc_final

            if bloc[k] == list_code[i-1]:
                bloc_deco.append(list_lettre[i-1])
                k += 1
                break

        # si le code d'une lettre n'existe pas
        if k == cte:
            # on le transforme en code à 2 chiffres
            code = str(new_bloc[k]) + str(new_bloc[k+1])

            if code == '33':
                bloc_final = ""
                for lettre in bloc_deco:
                    bloc_final += lettre

                return bloc_final

            for i in range(len(list_code)):
                if int(code) == list_code[i]:
                    bloc_deco.append(list_lettre[i])
                    k += 2
                    break

    bloc_final = ""
    for lettre in bloc_deco:
        bloc_final += lettre

    return bloc_final


#if __name__ == '__main__':

    # x = decryptage_code_che([[8, 4, 9, 9, 0], [3, 7, 0, 2, 7, 7], [3, 5, 5, 2, 1, 5], [4, 1, 1, 9, 0], [4, 4, 8, 9, 3], [2, 1, 7, 8, 1, 7], [0, 9, 9, 7, 1]], 12345)
    # print(x)