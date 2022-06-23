# -*- coding:utf-8 -*-
__projet__ = "PROJET_CRYPTO"
__nom_fichier__ = "CHIFFRE_Beaufort"
__author__ = "PENOT BAPTISTE"
__date__ = "novembre 2021"

from classes_et_fonctions.preparation_chiffre import alphabet, del_accent_char, adapt_clef
from classes_et_fonctions.mise_en_forme import space_every_four_chars


class Beaufort:
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
        Fonction qui réalise le chiffrement par la méthode de Beaufort d'une chaine de caractères imposée en entrée
        :return: message clair chiffré grâce à une clef de chiffrement choisie par l'utilisateur
        """

        chiffreB = ""
        for ind in range(len(self.message_)):
            chiffreB += alphabet[alphabet.index(self.clef_[ind]) - alphabet.index(self.message_[ind])]
        return space_every_four_chars(chiffreB)

    def dechiffrement(self):
        """
        Fonction qui exécute le déchiffrement d'une chaine de caractères chiffrée par la méthode de Beaufort
        :return: Le message clair associé, si la clef de chiffrement est correcte
        """

        dechiffreB = ""
        for ind in range(len(self.message_)):
            dechiffreB += alphabet[alphabet.index(self.clef_[ind]) - alphabet.index(self.message_[ind])]
        return dechiffreB


if __name__ == '__main__':
    print(Beaufort("baptiste","clef").chiffrement())
    print(Beaufort("BLPM UTLB","clef").dechiffrement())