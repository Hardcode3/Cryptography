# -*- coding:utf-8 -*-
__projet__ = "classe_che.py"
__nom_fichier__ = "class_hill"
__author__ = "mon_Prénom mon_Nom"
__date__ = "décembre 2021"

from classes_et_fonctions.code_hill import *
from classes_et_fonctions.decryptage_code_hill import *
from classes_et_fonctions.preparation_chiffre import del_accent_char

class Hill:

    def __init__(self, mot, param, p=2):
        self.mot_ = del_accent_char(mot)
        self.a_ = param[0]
        self.b_ = param[1]
        self.c_ = param[2]

    def chiffrement(self):
        """chiffre un message via le chiffrement de Hill"""

        return chiffrement(self.mot_, self.a_, self.b_, self.c_)

    def dechiffrement(self):
        """déchiffre un message préalablement codé via le chiffrement de Hill"""

        return dechiffrement(self.mot_, self.a_, self.b_, self.c_)


if __name__ == '__main__':
    message = Hill("ESSAIS", [7, 5, 9])
    print(message.chiffrement())
    message_code = Hill("KASALJ", [7, 5, 9])
    print(message_code.dechiffrement())
