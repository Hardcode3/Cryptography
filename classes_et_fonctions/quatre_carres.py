# -*- coding:utf-8 -*-
__projet__ = "pythonProject7projetcryptopolygraph"
__nom_fichier__ = "chiffre_des_four_carres"
__author__ = "ACETO Lilian"
__date__ = "novembre 2021"

# Ce programme necessite des lettres majuscules pour fonctionner

import random

# Grille ordonnee
Grille_ordonnee = [["A", "B", "C", "D", "E"], ["F", "G", "H", "I", "K"], ["L", "M", "N", "O", "P"],
                   ["Q", "R", "S", "T", "U"], ["V", "W", "X", "Y", "Z"]]
# liste alphabetique
Liste_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                  "U", "V", "W", "X", "Y", "Z"]

def creation_grille_aleatoire():
    """
    Creation d'une grille aleatoire 5*5
    :return: une grille aleatoire
    """
    grille_desordonnee = []  # initialisation
    alphabet = Liste_alphabet.copy()  # creation d'une copie de la liste alphabet
    for i in range(0, 5):
        ligne = []
        for j in range(0, 5):
            lettre = random.choice(alphabet)  # choix aleatoire d'une lettre
            ligne.append(lettre)
            del alphabet[alphabet.index(lettre)]
        grille_desordonnee.append(ligne)
    return grille_desordonnee


def trouver_les_coordonnees(matrice, valeur):
    """
    Fonction permettant de trouver les coordonnées d'une valeur dans une matrice:
    :param matrice: Matrice dans laquelle se trouve la valeur
    :param valeur: valeur pour laquelle nous cherchons les coordonnées
    :return: un couple avec le numéros de la ligne et colonne de la valeur dans la matrice
    """
    for ligne in matrice:
        # Nous parcourons les lignes de la matrice
        if valeur in ligne:
            # Si la valeur se trouve dans la ligne nous recuperons l'indice de la colonne
            colonne_valeur = ligne.index(valeur)
            # La fonction s'arrete immediatement la valeur trouvee
            return matrice.index(ligne), colonne_valeur

grille1 = creation_grille_aleatoire()
grille2 = creation_grille_aleatoire()

class Quatre_carres:
    def __init__(self, message, grille_haut_droit=None, grille_bas_gauche=None):
        """
        :param message: Message code ou a code
        :param grille_haut_droit: grille aleatoire situe en haut a droite
        :param grille_bas_gauche: grille aleatoire situe en bas a gauche
        """
        self.message_ = message
        if grille_haut_droit is None:
            self.grille_haut_droit_ = grille1
        else:
            self.grille_haut_droit_ = grille_haut_droit
        if grille_bas_gauche is None:
            self.grille_bas_gauche_ = grille2
        else:
            self.grille_bas_gauche_ = grille_bas_gauche

    def analyse_message(self):
        """
        Fonction permettant de savoir si le message comporte un nombre paire ou impaire de lettres
        :return: 1 si le nombre de lettre est paire 0 sinon
        """
        if len(self.message_) % 2 == 0:
            return 1
        else:
            return 0

    def message_modifie(self):
        """
        Modifie le message partitionne pour que celui-ci ne comporte plus de J, et des I a la place
        :return: Un message partitionne avec des I a la place des J
        """
        message_modifie1 = self.partition_message()
        for binome in message_modifie1:  # parcour la liste des binomes
            if "J" in binome:
                indice = binome.index("J")
                binome[indice] = "I"
            return message_modifie1

    def partition_message(self):
        """
        Fonction decoupant le message en binomes et en rajoutant un A par defaut si le dernier est incomplet (message impaire en nombre de lettre)
        :return: le message deoupe en binomes sous forme de liste
        """
        liste_binome = []  # intialisation de la liste des binomes
        binome = []  # initialisation du binome
        for lettre in self.message_:  # parcour du message
            if len(binome) == 2:  # si le binome est forme, il est ajoute a la liste et reinitialisation  de celui-ci
                liste_binome.append(binome)
                binome = []
            binome.append(lettre)  # sinon le binome est complete
        if len(binome) != 2:  # rajout d un A pour completer si le message est impaire en nombre de lettre
            binome.append('A')
        liste_binome.append(binome)

        return liste_binome

    def chiffrement(self):
        """
        Fonction permettant de coder le message
        :return: le message code
        """
        liste_binome = self.partition_message()  # recuperation de la liste de binome
        liste_binome = self.message_modifie()  # modification de celle-ci
        message_code = ""  # initialisation du message code
        for binome in liste_binome:  # parcour de la liste des binomes
            ligne_i, colonne_i = trouver_les_coordonnees(Grille_ordonnee, binome[
                0])  # recuperation des coordonnees de la lettre 1 du binome dans la grille
            ligne_j, colonne_j = trouver_les_coordonnees(Grille_ordonnee, binome[1])  # idem pour la lettre 2
            message_code += self.grille_haut_droit_[ligne_i][colonne_j] + self.grille_bas_gauche_[ligne_j][
                colonne_i]  # ajout des nouvelles lettres au message code
        return message_code

    def dechiffrement(self):
        """
        Fonction permettant de decoder le message code elle fonctionne comme codage avec des grilles différentes,  les grilles aleatoires
        :return: le message decode
        """
        liste_binome = self.partition_message()
        liste_binome = self.message_modifie()
        message = ""
        for i, j in liste_binome:
            ligne_i, colonne_i = trouver_les_coordonnees(self.grille_haut_droit_,
                                                         i)  # recherche de la position de la 1 ere lettre dans la grille aleatoire du haut
            ligne_j, colonne_j = trouver_les_coordonnees(self.grille_bas_gauche_,
                                                         j)  # recherche de la position de la 2 eme lettre dans la grille aleatoire du bas
            message += Grille_ordonnee[ligne_i][colonne_j] + Grille_ordonnee[ligne_j][
                colonne_i]  # ajout des lettres trouvees au message
        return message


if __name__ == '__main__':
    # test des differentes fonctions
    Grille1 = creation_grille_aleatoire()
    Grille2 = creation_grille_aleatoire()
    Code1 = Quatre_carres("ANDREA")
    #print(Code1.chiffrement())
    #print(creation_grille_aleatoire())
    #print(Code1.analyse_message(), Code1.message_modifie(), Code1.partition_message())
    Code2 = Code1.chiffrement()
    Fichier2 = Quatre_carres(Code2)
    #print(Fichier2.dechiffrement())
    #print(Code2, Fichier2.partition_message(), Fichier2.decodage())

    print(Quatre_carres("test").chiffrement())
    print(Quatre_carres(Quatre_carres("test").chiffrement()).dechiffrement())