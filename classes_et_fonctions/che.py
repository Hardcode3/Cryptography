# -*- coding:utf-8 -*-
__projet__ = "code_che.py"
__nom_fichier__ = "classe_che"
__author__ = "mon_Prénom mon_Nom"
__date__ = "décembre 2021"

from classes_et_fonctions.preparation_chiffre import del_accent_char
from classes_et_fonctions.decryptage_code_che import *
from classes_et_fonctions.code_che import *

class Che:

    def __init__(self, message, cle):
        if type(message) is str:
            self.message_ = del_accent_char(message)
        else:
            self.message_ = message
        self.cle_ = str(cle)

    def chiffrement(self):
        """code le message entier avec la cle"""

        # on découpe le message
        message_code = substitution(self.message_)

        # on prépare la clé pour la suite du code (gain de calcul)
        list_cle = separer(self.cle_)
        resultat = []

        # pour chaque bloc
        for bloc in message_code:
            # on le convertit avec la clé
            bloc_separe = separer(bloc)
            resultat.append(codage_bloc(bloc_separe, list_cle))

        return resultat

    def dechiffrement(self):
        """décrypte un message codé via la méthode du che"""

        message_conv = ""
        for bloc in self.message_:
            bloc_decrypt = decryptage_bloc(bloc, self.cle_)
            bloc_conv = conversion_bloc(bloc_decrypt)
            message_conv += bloc_conv

        return message_conv

if __name__ == '__main__':

    che = Che("LILIAN", 22060)
    print(che.chiffrement())
    decode = Che(che.chiffrement(), 22060)
    print(decode.dechiffrement())

    #[[7, 4, 5, 9, 3, 2], [5, 1, 6, 3, 6]]
