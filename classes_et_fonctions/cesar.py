# -*- coding:utf-8 -*-
__projet__ = "projet"
__nom_fichier__ = "methode_cesar"
__author__ = "Benoit Cachard"
__date__ = "novembre 2021"

# script de la méthode de césar - sens codage
from classes_et_fonctions.preparation_chiffre import del_accent_char
list_lettre = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

class Cesar :
    def __init__(self, texte, cle):
        self.texte = del_accent_char(texte)
        self.cle = int(cle)

# script de la méthode de césar - sens décodage

    def chiffrement (self) :
        M = [] # on crée une liste vide qui donnera le rendu final
        for lettre in self.texte: # on balaye le mot donné par l'utilisateur
            if lettre == ' ':
                M.append(' ') # le but de cette boucle if est de prendre en compte les espaces
            else :
                nbe = list_lettre.index(lettre) + self.cle # on applique la clé de décalage à la lettre en question
                if nbe <= 25 :
                    M.append(list_lettre[nbe]) # on ajoute la nouvelle lettre au mot codé
                else :
                    M.append(list_lettre[nbe-26]) # cette bouble if / else permet de prendre en compte les cas qui dépassent les limites de l'alphabet
        result = ''.join(M) # permet que le résultat final soit sous forme de mot
        return result # on retourne le mot codé

# script de la méthode de césar - sens décodage

    def dechiffrement (self) :
        M = [] # on crée une liste vide qui donnera le rendu final
        for lettre in self.texte: # on balaye le mot donné par l'utilisateur
            if lettre == ' ':
                M.append(' ') # le but de cette boucle if est de prendre en compte les espaces
            else :
                nbe = list_lettre.index(lettre) - self.cle # on applique la clé de décalage à la lettre en question
                if nbe >= 0:
                    M.append(list_lettre[nbe]) # on ajoute la nouvelle lettre au mot décodé
                else:
                    M.append(list_lettre[26+nbe]) # cette bouble if / else permet de prendre en compte les cas qui dépassent les limites de l'alphabet
        result = ''.join(M) # permet que le résultat final soit sous forme de mot
        return result # on retourne le mot décodé


if __name__ == '__main__':
    print(Cesar("benoit", 22).chiffrement())
    print(Cesar("XAJKEP", 22).dechiffrement())