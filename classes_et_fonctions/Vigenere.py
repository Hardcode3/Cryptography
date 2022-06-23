# -*- coding:utf-8 -*-
__projet__ = "PROJET_CRYPTO"
__nom_fichier__ = "CHIFFRE_Vigenere"
__author__ = "PENOT BAPTISTE"
__date__ = "novembre 2021"

from classes_et_fonctions.preparation_chiffre import del_accent_char, adapt_clef, alphabet
from classes_et_fonctions.mise_en_forme import space_every_four_chars


class Vigenere:
    def __init__(self, message, clef):
        self.message_ = message
        self.clef_ = clef

        # préparation du str : accents et espaces enlevés et message mis en majuscule
        self.message_ = del_accent_char(self.message_)
        self.clef_ = del_accent_char(self.clef_)

        # Adaptation de la clef au mot à chiffrer (renvoie la bonne taille de clef)
        self.clef_ = adapt_clef(self.message_, self.clef_)

    def chiffrement(self):
        """
        Fonction qui réalise le chiffrement par la méthode de Vigenère d'une chaine de caractères imposée en entrée
        :return: message clair chiffré grâce à une clef de chiffrement choisie par l'utilisateur
        """

        chiffreV = ""
        for ind in range(len(self.message_)):
            chiffreV += alphabet[alphabet.index(self.message_[ind]) + alphabet.index(self.clef_[ind])]
        return space_every_four_chars(chiffreV)

    def dechiffrement(self):
        """
        Fonction qui exécute le déchiffrement d'une chaine de caractères chiffrée par la méthode de Vigenère
        :return: Le message clair associé, si la clef de chiffrement est correcte
        """

        dechiffreV = ""
        for ind in range(len(self.message_)):
            dechiffreV += alphabet[alphabet.index(self.message_[ind]) - alphabet.index(self.clef_[ind])]
        return dechiffreV


if __name__ == '__main__':
    print(Vigenere("Baptiste", "clef").chiffrement())
    print(Vigenere("DLTY KDXJ", "clef").dechiffrement())
