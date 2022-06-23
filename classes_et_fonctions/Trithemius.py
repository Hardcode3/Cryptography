# -*- coding:utf-8 -*-
__projet__ = "PROJET_CRYPTO"
__nom_fichier__ = "CHIFFRE_Trithemius"
__author__ = "PENOT BAPTISTE"
__date__ = "novembre 2021"

from classes_et_fonctions.preparation_chiffre import del_accent_char, alphabet
from classes_et_fonctions.mise_en_forme import space_every_four_chars


# Ce programme réalise la méthode du chiffre de trithémius par le décalage de César
# C'est une méthode polyalphabétique

## PRINCIPE
# La première lettre ne change pas (pas de décalage)
# La seconde lettre est décalée d’un cran dans l’alphabet
# La troisième l’est de 2 etc
# Donc la n ème lettre est décalée de n-1 crans dans l’alphabet
# Au bout de 24 lettres, on recommence à décaler, donc la 25 ème est la même
# La 26 ème est décalée d’un cran etc….

class Trithemius:
    def __init__(self, message, clef=None):
        self.message_ = message

        # préparation du str : accents et espaces enlevés et message mis en majuscule
        self.message_ = del_accent_char(self.message_)

    def chiffrement(self):
        """
        Fonction qui réalise le chiffrement par la méthode de Trithémius d'une chaine de caractères imposée en entrée
        :return: message clair chiffré sans clef de chiffrement
        """

        # le chiffrage est réalisé selon le tableau de trithème
        # pour chaque caractère
        chiffre = self.message_[0]
        for i in range(1, len(self.message_)):
            # on remplit la liste avec la méthode de César (décalage de 1)
            chiffre += alphabet[alphabet.index(self.message_[i]) + i]
        return space_every_four_chars(chiffre)

    def dechiffrement(self):
        """
        Fonction qui exécute le déchiffrement d'une chaine de caractères chiffrée par la méthode de Trithémius
        :return: Le message clair associé sans clef de chiffrement
        """
        dechiffre = self.message_[0]
        for i in range(1, len(self.message_)):
            dechiffre += alphabet[alphabet.index(self.message_[i]) - i]

        return dechiffre


if __name__ == '__main__':
    print(Trithemius("baptiste").chiffrement())
    print(Trithemius("BBRW MXZL").dechiffrement())
