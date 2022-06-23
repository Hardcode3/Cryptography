# -*- coding:utf-8 -*-
__projet__ = "class_hill.py"
__nom_fichier__ = "decryptage_code_hill"
__author__ = "mon_Prénom mon_Nom"
__date__ = "décembre 2021"

from classes_et_fonctions.code_hill import *


def invmatrice(a, b, c):
    """inverse la matrice ayant codé un message avec le chiffre de Hill et la transforme en la matrice nécessaire au décodage du message"""

    # Pour inverser la matrice ayant servi au cryptage, on la recrée, la création étant unique puisque le dernier paramètre (d) est déterminé par itération
    matA = matrice(a, b, c)

    # Si la matA est nulle
    if not matA.any():
        # On la renvoie directement, ce qui renverra un message à l'utilisateur sur les paramètres à choisir (dans la méthode déchiffrement)
        return matA

    d = matA[1][1]
    # On calcule le déterminant de la matrice
    det = a * d - b * c

    n = len(list_lettre)
    # On cherche l'inverse modulaire du déterminant (il est unique)
    inv_mod = 1

    # Tant que l'inverse modulaire n'est pas trouvé, on itère
    while (inv_mod * det) % n != 1:
        inv_mod += 1

    # On définit l'inverse de la matA
    inv_matA = [[d, -b], [-c, a]]

    # Et on crée la matrice solution qui décryptera le message
    mat_sol = []

    for ligne in inv_matA:
        ligne_sol = []
        for valeur in ligne:
            # Chaque coefficient de l'inverse de matA est multiplié par l'inverse modulaire modulo la longueur de l'alphabet
            ligne_sol.append((valeur * inv_mod) % len(list_lettre))
        mat_sol.append(ligne_sol)

    # La matrice permettant de décrypter le message est crée
    return np.array(mat_sol)


def dechiffrement(message, a, b, c, p=2):
    """déchiffre un message codé avec le chiffre de Hill"""

    carac_message = code_caracteres(message)
    liste_message = regroupement(carac_message, p)
    print(liste_message)
    matrice = invmatrice(a, b, c)

    # Si la matA est nulle
    if not matrice.any():
        # On renvoie à l'utilisateur que la valeur de a n'est pas compatible avec ce chiffrement
        return str(a) + " est une valeur impossible"

    liste_decrypt = new_regroupement(matrice, liste_message)

    # On crée un bloc qui permet de tester si le dernier bloc en sensé être rempli ou non en fonction de la longueur du message initial
    last_bloc = None
    k = len(message)

    # Si le dernier bloc n'est pas sensé être rempli
    if k != p * len(liste_decrypt):
        # last_bloc prend la valeur du premier élément du dernier bloc (puisque le bloc est de longueur 2,
        # le code serait différent dans le cas général de blocs de longueur p)
        last_bloc = liste_decrypt[-1]
        del liste_decrypt[-1]
        last_bloc = last_bloc[0]

    # On crée un str vide
    message_decode = ""

    # Pour chaque bloc
    for bloc in liste_decrypt:

        # Et pour chaque code du bloc
        for code in list(bloc):
            # On ajoute la lettre décodée au message
            message_decode += list_lettre[code % len(list_lettre)]

    # On vérifie que le dernier bloc ait été traité
    if last_bloc != None:
        # Sinon on le traite :
        # Puisque le message est de longueur impaire, le code de la dernière lettre (y) est a * valeur de la lettre (x)
        # On peut donc remonter à la lettre d'origine, il s'agit de x = (y + len(alphabet) * i) / a, il faut donc trouver i
        i = 0
        # Une fois qu on sait que la division sera entière ie pgcd(y + len(alphabet) * i, a) != 1
        while pgcd(liste_message[-1][0] + len(list_lettre) * i, a) == 1:
            i += 1
        # On peut ajouter la lettre correspondante au message décodé
        message_decode += list_lettre[int((liste_message[-1][0] + len(list_lettre)) * i / a)]

    return message_decode


if __name__ == '__main__':
    print(chiffrement("L INFO C EST TOP", 7, 2, 13))
    print(dechiffrement("VIBXJLYOBOCSEOUU", 6, 2, 13))
