# -*- coding:utf-8 -*-
__projet__ = "PROJET_CRYPTO"
__nom_fichier__ = "mise_en_forme"
__author__ = "PENOT BAPTISTE"
__date__ = "novembre 2021"


def space_every_four_chars(text, space=4, completion=False, letter="X"):
    """
    Fonction qui insère un espace par défaut tous les caractères pour une meilleure lisibilité
    :param text: chaine de caractères à regrouper en paquets de n caractères
    :param space: taille des paquets de caractères voulus
    :param completion: True si l'on veut absolument que les groupes de caractères soient complets
    :param letter: lettre qui va remplir ces groupes non complets, par défaut, la lettre X
    :return: la chaine de caractères traitée et mise en majuscule
    """

    if completion == True and len(text) not in [space * nb for nb in range(1, 20)]:
        # si l'on veut compléter les groupes de lettres
        # et si tant que la longueur de la chaine de caractères n'est pas un multiple de la variable space
        while len(text) not in [space * nb for nb in range(1, 20)]:
            # on ajoute la lettre pour compléter le groupe, ici par défaut "x"
            text += letter.upper()
    newtext = ""
    count = 0
    for char in text:
        if count in [space * nb for nb in range(1, 20)]:
            # on fait des paquets de lettres de la taille de la variable space, par défaut 4
            newtext += " "
        newtext += char
        count += 1
    return newtext.upper()


if __name__ == '__main__':
    print(space_every_four_chars("BAPTISTECODEINPYTHON"))
    print(space_every_four_chars("TROPSYMPA"))
    print(space_every_four_chars("BAPTISTECODEINPYTHON", 5, completion=1, letter="x"))
    print(space_every_four_chars("TROPSYMPA", 5, completion=1))
    print(space_every_four_chars("tr", 5, completion=1, letter="z"))
