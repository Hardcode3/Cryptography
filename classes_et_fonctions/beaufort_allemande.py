# -*- coding:utf-8 -*-
__projet__ = "PROJET_CRYPTO"
__nom_fichier__ = "CIFFRE_Beaufort_variante_allemande"
__author__ = "PENOT BAPTISTE"
__date__ = "novembre 2021"

from classes_et_fonctions.preparation_chiffre import del_accent_char, adapt_clef, alphabet
from classes_et_fonctions.mise_en_forme import space_every_four_chars


class Beaufort_allemande:
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
        Fonction qui réalise le chiffrement par la méthode de Beaufort (variante allemande) d'une chaine de caractères imposée en entrée
        :return: message clair chiffré grâce à une clef de chiffrement choisie par l'utilisateur
        """

        chiffreV_all = ""
        for ind in range(len(self.message_)):
            chiffreV_all += alphabet[alphabet.index(self.message_[ind]) - alphabet.index(self.clef_[ind])]
        return space_every_four_chars(chiffreV_all)

    def dechiffrement(self):
        """
        Fonction qui exécute le déchiffrement d'une chaine de caractères chiffrée par la méthode de Beaufort (variante Allemande)
        :return: Le message clair associé, si la clef de chiffrement est correcte
        """

        dechiffreV_all = ""
        for ind in range(len(self.message_)):
            dechiffreV_all += alphabet[alphabet.index(self.message_[ind]) + alphabet.index(self.clef_[ind])]
        return dechiffreV_all


if __name__ == '__main__':
    print(Beaufort_allemande("baptiste", "clef").chiffrement())
    print(Beaufort_allemande("ZPLO GHPZ", "clef").dechiffrement())
