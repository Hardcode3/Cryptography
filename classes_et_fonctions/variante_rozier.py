# -*- coding:utf-8 -*-
__projet__ = "PROJET_CRYPTO"
__nom_fichier__ = "Variante_Rozier"
__author__ = "PENOT BAPTISTE"
__date__ = "novembre 2021"

from classes_et_fonctions.preparation_chiffre import del_accent_char, adapt_clef, alphabet
from classes_et_fonctions.mise_en_forme import space_every_four_chars


class Vigenere_rozier:
    def __init__(self, message, clef):
        self.message_ = message
        self.clef_ = clef

        self.message_ = del_accent_char(self.message_)
        self.clef_ = del_accent_char(self.clef_)

        clef_originelle = self.clef_  # sauvegarde de la clef originelle

        # chiffrer en Rozier, c'est chiffrer en vigenère avec une clef légèrement différente
        self.clef_ = self.clef_[1:len(self.clef_)] + self.clef_[0]

        # création de la nouvelle clef
        nvelle_clef = ""
        for ind in range(len(self.clef_)):
            nvelle_clef += alphabet[alphabet.index(self.clef_[ind]) - alphabet.index(clef_originelle[ind])]

        # Adaptation de la clef au mot à chiffrer (renvoie la bonne taille de clef)
        self.nvelle_clef_ = adapt_clef(self.message_, nvelle_clef)

    def chiffrement(self):
        """
        Fonction qui réalise le chiffrement par la méthode de Rozier d'une chaine de caractères imposée en entrée
        :return: message clair chiffré grâce à une clef de chiffrement choisie par l'utilisateur
        """

        chiffreVr = ""
        for ind in range(len(self.message_)):
            chiffreVr += alphabet[alphabet.index(self.message_[ind]) + alphabet.index(self.nvelle_clef_[ind])]
        return space_every_four_chars(chiffreVr)

    def dechiffrement(self):
        """
        Fonction qui exécute le déchiffrement d'une chaine de caractères chiffrée par la méthode de Rozier
        :return: Le message clair associé, si la clef de chiffrement est correcte
        """

        dechiffreVr = ""
        for ind in range(len(self.message_)):
            dechiffreVr += alphabet[alphabet.index(self.message_[ind]) - alphabet.index(self.nvelle_clef_[ind])]
        return dechiffreVr


if __name__ == '__main__':
    print(Vigenere_rozier("Baptiste", "clef").chiffrement())
    print(Vigenere_rozier("KTQQ RLUB", "clef").dechiffrement())
