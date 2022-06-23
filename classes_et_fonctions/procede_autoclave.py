# -*- coding:utf-8 -*-
__projet__ = "PROJET_CRYPTO"
__nom_fichier__ = "Procede_autoclave"
__author__ = "PENOT BAPTISTE"
__date__ = "novembre 2021"

# IL S'AGIT DU CHIFFREMENT DE VIGENÈRE POUR LEQUEL LA CLEF EST LE MESSAGE CLAIR PRÉCÉDÉ D'UNE LETTRE CHOISIE

from classes_et_fonctions.preparation_chiffre import del_accent_char, adapt_clef, alphabet
from classes_et_fonctions.mise_en_forme import space_every_four_chars


# C'EST LA METHODE DE VIGENERE POOUR UNE CLEF LEGEREMENT DIFFERENTE (on choisit un lettre que l'on place en premier dans le mot, qui devient la clef, une fois coupé à la bonne taille)
class Procede_autoclave:
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
        Fonction qui réalise le chiffrement par la méthode de Vigenère (procédé autoclave) d'une chaine de caractères imposée en entrée
        :return: message clair chiffré grâce à une clef de chiffrement choisie par l'utilisateur
        """

        chiffreVa = ""
        for ind in range(len(self.message_)):
            chiffreVa += alphabet[alphabet.index(self.message_[ind]) + alphabet.index(self.clef_[ind])]
        return space_every_four_chars(chiffreVa)

    def dechiffrement(self):
        """
        Fonction qui exécute le déchiffrement d'une chaine de caractères chiffrée par la méthode de Vigenère (procédé autoclave)
        :return: Le message clair associé, si la clef de chiffrement est correcte
        """

        dechiffreVa = ""
        for ind in range(len(self.message_)):
            dechiffreVa += alphabet[alphabet.index(self.message_[ind]) - alphabet.index(self.clef_[ind])]
        return dechiffreVa


if __name__ == '__main__':
    print(Procede_autoclave("Baptiste", "xbaptiste", ).chiffrement())
    print(Procede_autoclave("YBPI BALX", "xbaptiste").dechiffrement())
