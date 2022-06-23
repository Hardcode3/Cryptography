# -*- coding:utf-8 -*-
__projet__ = "classe_che.py"
__nom_fichier__ = "code_hill"
__author__ = "mon_Prénom mon_Nom"
__date__ = "décembre 2021"

from random import randrange
from math import *
import numpy as np

list_lettre = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
               "V", "W", "X", "Y", "Z", " "]


def code_caracteres(message):
    """code un message en assignant à chaque lettre son rang dans l'alphabet - 1, l'espace est placé à la fin de l'alphabet (code 26)"""

    # On crée une liste vide
    list_mess_code = []

    # On remplit la liste par le rang des lettres dans l'alphabet - 1
    for lettre in message:
        for i in range(len(list_lettre)):
            if lettre == list_lettre[i]:
                list_mess_code.append(i)

    return list_mess_code


def regroupement(liste, p):
    """regroupe les codes d'une liste en blocs de p codes. Si le dernier bloc n'est pas complet, il est complété aléatoirement"""

    list_bloc = []
    k = 0
    bloc = []
    for code in liste:
        # si le bloc n'est pas de longueur p, on ajoute un code au bloc
        if len(bloc) < p:
            bloc.append(code)
            k += 1

        # si le bloc est de longueur p, on ajoute le bloc à la list_bloc, et on crée un nouveau bloc
        else:
            list_bloc.append(np.array(bloc))
            bloc = []
            bloc.append(code)
            k = 0

    # si le dernier bloc n'est pas complet, on le complète avec des 0
    if len(bloc) != p:
        for i in range(p - len(bloc)):
            bloc.append(0)

    # on ajoute le dernier bloc à la list_bloc
    list_bloc.append(np.array(bloc))

    return list_bloc


def pgcd(a, b):
    """retourne le pgcd de a et b"""
    # Cette fonction est utile pour la méthode matrice

    if b == 0:
        return a
    else:
        r = a % b
        return pgcd(b, r)


def matrice(a, b, c, p=2):
    """crée une matrice carrée de taille p=2 (cas simplifié) à partir de 3 coefficients donnés telle que son déterminant soit premier avec la longueur de la liste de lettres"""

    n = len(list_lettre)

    # a doit être premier avec la longueur de la liste, sinon on retourne une erreur
    for nbre in range(2, int(min(a, n))):
        # Si a et n sont premiers entre eux
        if a % nbre == 0 and n % nbre == 0:
            # On renvoie une matrice nulle
            return np.array([[0, 0], [0, 0]])

    # on prend un d = 0
    d = 0

    # tant que le déterminant n'est pas premier avec n, on augmente d de 1 (d est donc toujours le même pour a, b et c connus,
    # ce qui est plus pratique pour le decryptage, car il n'est pas nécessaire de connaître d pour décrypter)
    while pgcd(a * d - b * c, n) != 1:
        d += 1

    return np.array([[a, b], [c, d]])


def new_regroupement(matA, list_bloc):
    """réalise le produit de la matrice A avec chacun des vecteurs de la liste des blocs"""

    new_list_bloc = []
    for bloc in list_bloc:
        new_list_bloc.append(np.dot(matA, bloc))

    return new_list_bloc


def chiffrement(message, a, b, c, p=2):
    """code le message via le chiffrement de Hill"""

    caracteres_codes = code_caracteres(message)
    list_bloc = regroupement(caracteres_codes, p)
    matA = matrice(a, b, c, p)

    # Si la matA est nulle
    if not matA.any():
        # On renvoie à l'utilisateur que la valeur de a n'est pas compatible avec ce chiffrement
        return str(a) + " est une valeur impossible"

    else:
        # new_list_bloc est la matrice des vecteurs codés (vecteurs intiaux multipliés par la matrice)
        new_list_bloc = new_regroupement(matA, list_bloc)
        # On crée un bloc qui permet de tester si le dernier bloc en sensé être rempli ou non en fonction de la longueur du message initial
        last_bloc = None
        k = len(message)

        # Si le dernier bloc n'est pas sensé être rempli
        if k != p * len(new_list_bloc):
            # last_bloc prend la valeur du premier élément du dernier bloc (puisque le bloc est de longueur 2,
            # le code serait différent dans le cas général de blocs de longueur p)
            last_bloc = new_list_bloc[-1]
            del new_list_bloc[-1]
            last_bloc = last_bloc[0]

        # On crée un str vide
        message_code = ""

        # Pour chaque bloc
        for bloc in new_list_bloc:

            # Et pour chaque code du bloc
            for code in list(bloc):
                # On ajoute la lettre codée au message
                message_code += list_lettre[code % len(list_lettre)]

        # On vérifie que le dernier bloc ait été traité
        if last_bloc != None:
            # Sinon on le traite
            message_code += list_lettre[last_bloc % len(list_lettre)]

        return message_code


if __name__ == '__main__':
    print(chiffrement("BAPTISTE", 7, 5, 6))
