# -*- coding:utf-8 -*-
__projet__ = "interface graphique.py"
__nom_fichier__ = "methode_polybe"
__author__ = "Benoit Cachard"
__date__ = "novembre 2021"

from classes_et_fonctions.preparation_chiffre import del_accent_char

matrice_lettre = [['A', 'B', 'C', 'D', 'E'], ['F', 'G', 'H', 'I', 'K'], ['L', 'M', 'N', 'O', 'P'],
                  ['Q', 'R', 'S', 'T', 'U'], ['V', 'W', 'X', 'Y', 'Z']]


class Polybe:
    def __init__(self, texte, clef):
        self.texte = del_accent_char(texte)
        self.clef_ = clef

    # script de la méthode de polybe - sens codage

    def chiffrement(self):
        Mot_code = []  # on crée une liste vide qui sera le mot codé
        coord_1 = 0
        coord_2 = 0
        for lettre in self.texte:  # on balaye le mot donnée par l'utilisateur
            if lettre == ' ':
                Mot_code.append(' ')  # le but de cette boucle if est de prendre en compte les espaces
            else:
                if lettre == 'j':  # couvre le cas spécifique de la lettre j qui occupe la même case que i dans la matrice, de coordonnée (1, 3)
                    coord_1 = 1
                    coord_2 = 3
                else:
                    for L in matrice_lettre:  # on balaye les sous-listes de la matrice alphabet
                        if lettre in L:  # on balaye les éléments de chaque sous-liste
                            coord_1 = matrice_lettre.index(
                                L)  # la première coordonnée de la lettre en question est la coordonnée de la sous liste dans la matrice
                            coord_2 = L.index(
                                lettre)  # la deuxième coordonnée de la lettre en question est la coordonnée de la lettre dans la sous-liste en question
                Mot_code.append(coord_1)  # on ajoute la coordonnée 1 de la lettre en question au mot codé
                Mot_code.append(coord_2)  # on ajoute la coordonnée 2 de la lettre en question au mot codé
        result = ""
        for elt in Mot_code:  # on modifie l'apparence du resultat pour qu'il soit de la forme "2341 3413324213 243422"
            result += str(elt)  # pour cela on doit transformer les entiers en str pour que python puisse les concaténer
        return result  # on retourne le mot codé

    # script de la méthode de polybe - sens décodage

    def dechiffrement(self):
        result = ""  # on crée une chaine de caractère vide
        i = 0  # on initialise la valeur de i, notre compteur
        while i < len(self.texte):  # on parcourt le code rentré par l'utilisateur
            if self.texte[i] == " ":  # cette boucle if premet de prendre en compte les espaces
                result += " "
                i = i + 1  # on passe au caractère suivant
            else:  # cette boucle lit les deux valeurs (coordonnées) et les associent à une lettre de la matrice de polybe qu'elle ajoute au résultat
                result += matrice_lettre[int(self.texte[int(i)])][int(self.texte[int(i + 1)])]
                i = i + 2  # on saute le caractère d'après car on l'a déjà étudié avec le i+1
        return result  # on renvoie le résultat


# script général


# code_decod = int(input(
#     "entrez 1 pour coder ou 2 pour décoder : "))  # on demande à l'utilisateur si il souhaite coder ou décoder son mot
# if code_decod == 1:  # cette boucle permet d'appliquer le bon programme en fonction du souhait de l'utilisateur
#     mot = input("entrez le mot : ")  # on demande à l'utilisateur le mot d'entrée
#     print("votre mot codé selon la méthode de polybe donne :", code_polybe(mot))
#
# else:
#     cle = input(
#         "entrez la clé de coordonnées (exemple présentation : 12354565 75468864) : ")  # on demande à l'utilisateur la cle des coordonnées qu'il souhaite décoder
#     print("votre mot décodé selon la méthode de polybe est :", decode_polybe(cle))
if __name__ == '__main__':
    print(Polybe("test").chiffrement())
    print(Polybe("33043233").dechiffrement())
