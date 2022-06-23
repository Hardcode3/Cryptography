# -*- coding:utf-8 -*-
__projet__ = "projet"
__nom_fichier__ = "methode_atbash"
__author__ = "Benoit Cachard"
__date__ = "novembre 2021"

from classes_et_fonctions.preparation_chiffre import del_accent_char

list_lettre = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
               "V", "W", "X", "Y", "Z"]
list_lettre_reverse = ['Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N', 'M', 'L', 'K', 'J', 'I', 'H',
                       'G', 'F', 'E', 'D', 'C', 'B', 'A']


class Atbash:
    def __init__(self, texte, clef):
        self.texte = del_accent_char(texte)
        self.clef_ = clef

    # script de la méthode atbash - sens codage

    def chiffrement(self):
        Mot_code = []  # on crée une liste vide qui donnera le rendu final
        for lettre in self.texte:  # on balaye le mot donné par l'utilisateur
            if lettre == ' ':
                Mot_code.append(' ')  # le but de cette boucle if est de prendre en compte les espaces
            else:
                nbe = list_lettre.index(lettre)
                Mot_code.append(list_lettre_reverse[
                                    nbe])  # ajoute la lettre correspondante prise dans l'alphabet à l'envers au mot final
        result = ''.join(Mot_code)  # permet que le rendu final soit sous forme de mot
        return result  # on retourne le mot codé

    # script de la méthode de atbash - sens décodage

    def dechiffrement(self):
        Mot_decode = []  # on crée une liste vide qui donnera le rendu final
        for lettre in self.texte:  # on balaye le mot donné par l'utilisateur
            if lettre == ' ':
                Mot_decode.append(' ')  # le but de cette boucle if est de prendre en compte les espaces
            else:
                nbe_code = list_lettre.index(lettre)
                Mot_decode.append(list_lettre_reverse[
                                      nbe_code])  # ajoute la lettre correspondante prise dans l'alphabet à l'endroit au mot final
        result = ''.join(Mot_decode)  # permet que le rendu final soit sous forme de mot
        return result  # on retourne le mot codé


if __name__ == '__main__':
    # script général

    # entree = input("entrez le mot : ") # demande le mot à coder à l'utilisateur
    # code_decod = int(input("entrez '1' pour coder ou '2' pour décoder : ")) # demande à l'utilisateur si il souhaite coder son mot ou le décoder
    # if code_decod == 1: # boucle if permettant d'appliquer le bon code selon le souhait de l'utilisateur
    #     print(code_atbash(mot))
    # else:
    #     print(decode_atbash(mot))
    print(Atbash("Benoit").chiffrement())
    print(Atbash("YVMLRG").dechiffrement())
