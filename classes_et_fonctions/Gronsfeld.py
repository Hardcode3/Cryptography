# -*- coding:utf-8 -*-
__projet__ = "PROJET_CRYPTO"
__nom_fichier__ = "Gronsfeld"
__author__ = "PENOT BAPTISTE"
__date__ = "novembre 2021"

from classes_et_fonctions.preparation_chiffre import del_accent_char, adapt_clef, alphabet
from classes_et_fonctions.mise_en_forme import space_every_four_chars


class Gronsfeld:
    def __init__(self, message, clef):
        self.message_ = message
        self.clef_ = clef

        # préparation du str : accents et espaces enlevés et message mis en majuscule
        self.message_ = del_accent_char(self.message_)

        # Adaptation de la clef au mot à chiffrer (renvoie la bonne taille de clef)
        self.clef_ = adapt_clef(self.message_, self.clef_)

    def chiffrement(self):
        """
        Fonction qui exécute le déchiffrement d'une chaine de caractères chiffrée par la méthode de Gronsfeld
        :return: Le message chiffré grâce à une clef de chiffrement numérique
        """

        chiffreG = ""
        for ind in range(len(self.message_)):
            chiffreG += alphabet[alphabet.index(self.message_[ind]) + int(self.clef_[ind])]
        return space_every_four_chars(chiffreG)

    def dechiffrement(self):
        """
        Fonction qui déchiffre un message chiffré par la méthode de Gronsfeld
        :return: Le message clair associé, si la clef de chiffrement numérique est correcte
        """

        message = ""
        for ind in range(len(self.message_)):
            message += alphabet[alphabet.index(self.message_[ind]) - int(self.clef_[ind])]
        return message


if __name__ == '__main__':
    print(Gronsfeld("baptiste", "758").chiffrement())
    print(Gronsfeld("IFXA NAAJ", "758").dechiffrement())
