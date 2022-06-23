# -*- coding:utf-8 -*-
__projet__ = "PROJET_CRYPTO_save"
__nom_fichier__ = "Bellaso"
__author__ = "PENOT Baptiste"
__date__ = "novembre 2021"

from classes_et_fonctions.preparation_chiffre import del_accent_char, adapt_clef, alphabet


class Bellaso:
    def __init__(self, message, clef):
        self.message_ = message
        self.clef_ = clef

        # les espaces sont gardés puisque nécessaires pour le chiffrement
        self.message_ = del_accent_char(self.message_, space=True)
        self.clef_ = del_accent_char(self.clef_)

        # Adaptation de la clef au mot à chiffrer (renvoie la bonne taille de clef)
        nombre_mots = self.message_.count(" ") + 1
        # print(nombre_mots)
        # on adapte la clef au nombre de mots
        self.clef_ = adapt_clef(self.message_[: nombre_mots], self.clef_)
        print("clef", self.clef_)
        # print("message", self.message_)

        self.table_Bellaso_ = {"A": "abcdefghijklmnopqrstuvwxyz", "B": "abcdefghijklmnopqrstuvwxyz",
                               "C": "abcdefghijklmnopqrstuvwxyz", "D": "abcdefghijklmnopqrstuvwxyz",
                               "E": "abcdefghijklmyznopqrstuvwx", "F": "abcdefghijklmyznopqrstuvwx",
                               "G": "abcdefghijklmyznopqrstuvwx", "H": "abcdefghijklmyznopqrstuvwx",
                               "I": "abcdefghijklmwxyznopqrstuv", "J": "abcdefghijklmwxyznopqrstuv",
                               "K": "abcdefghijklmwxyznopqrstuv", "L": "abcdefghijklmwxyznopqrstuv",
                               "M": "abcdefghijklmuvwxyznopqrst", "N": "abcdefghijklmuvwxyznopqrst",
                               "O": "abcdefghijklmuvwxyznopqrst", "P": "abcdefghijklmuvwxyznopqrst",
                               "Q": "abcdefghijklmstuvwxyznopqr", "R": "abcdefghijklmstuvwxyznopqr",
                               "S": "abcdefghijklmstuvwxyznopqr", "T": "abcdefghijklmstuvwxyznopqr",
                               "U": "abcdefghijklmqrstuvwxyznop", "V": "abcdefghijklmqrstuvwxyznop",
                               "W": "abcdefghijklmqrstuvwxyznop", "X": "abcdefghijklmqrstuvwxyznop",
                               "Y": "abcdefghijklmopqrstuvwxyzn", "Z": "abcdefghijklmopqrstuvwxyzn"}

    def chiffrement(self):
        """
        Méthode qui chiffre et déchiffre un mot clair ou un code grâce à une clef et une table de Bellaso comme ci-dessus
        :return: la chaine de caractères chiffrée ou bien déchiffrée
        """

        chiffreB = ''
        # séparons les différents mots dans le message (d'après la position des espaces
        mots = self.message_.split()
        print("mots", mots)

        # pour chaque lettre de la clef
        for ind in range(len(self.clef_)):

            # on récupère l'alphabet correspondant à la lettre de la clef
            alphabet = self.table_Bellaso_[self.clef_[ind]].upper()

            # pour chaque lettre du mot correspondant
            for lettre in mots[ind]:

                # selon la valeur de l'index de la lettre du message clair, on trouve la lettre associée (qui est située à 13 caractères de celle-ci)
                # afin d'éviter l'erreur out of range
                if int(alphabet.index(lettre)) >= 13:
                    chiffreB += alphabet[alphabet.index(lettre) - 13]

                else:
                    chiffreB += alphabet[alphabet.index(lettre) + 13]

            if ind < len(self.clef_)-1:
                chiffreB += " "

        return chiffreB

    def dechiffrement(self):
        return self.chiffrement()


if __name__ == '__main__':
    chiffrer = Bellaso("le matin du deux février", "valise").chiffrement()
    print(chiffrer)
    print(Bellaso(chiffrer, "valise").chiffrement())