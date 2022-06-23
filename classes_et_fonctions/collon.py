# -*- coding:utf-8 -*-
__projet__ = "pythonProject7projetcryptopolygraph"
__nom_fichier__ = "chiffre_de_collon"
__author__ = "ACETO Lilian"
__date__ = "décembre 2021"

# Ce programme necessite des lettres majuscules pour fonctionner

# Grille support pour le codage
Grille_ordonnee = [["A", "B", "C", "D", "E"], ["F", "G", "H", "I", "K"], ["L", "M", "N", "O", "P"],
                   ["Q", "R", "S", "T", "U"], ["V", "W", "X", "Y", "Z"]]


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
            # Si la valeur se trouve dans la ligne nous récupérons l'indice de la colonne
            colonne_valeur = ligne.index(valeur)
            # La fonction s'arrête immédiatement la valeur trouvée
            return matrice.index(ligne), colonne_valeur


class Collon:
    def __init__(self, message, N):
        """
        :param message: Message codé ou décodé
        :param N: Clef représentant en combien de partie est divisé le message
        """
        self.message_ = message
        self.N_ = N

    def partition_message(self):
        """
        Cette fonction permet de découper le message en série de taille N
        :return: La liste contenant les différentes séries
        """
        n = 0  # initialisation du compteur
        nuplet = ""  # initialisation de la série
        message_decoupe = []  # initialisation de la liste
        while n <= len(self.message_) - 1:  # boucle parcourant le message
            if len(nuplet) < self.N_:  # si l série n'est pas de taille N nous rajoutons une lettre
                if self.message_[n] == "J":
                    nuplet += "I" #remplace les J par des I
                else:
                    nuplet += self.message_[n]
                n += 1
            else:  # Si la série est pleine la série est ajouté à la liste et la série est réinitialisée
                message_decoupe += [nuplet]
                nuplet = ""
        message_decoupe += [nuplet]  # rajout d'une série si elle est non complète
        return message_decoupe

    def formation_de_binome(self):
        """
        Cette fonction de décodage sert à retrouver les binomes lignes et colonnnes permettant de retrouver la lettre du message originel
        :return: Une liste de binome ligne colonne
        """
        liste_binomes = []  # initialisation de la liste des binomes
        binome = ["X", "X"]  # initialisation du binome
        liste_uplet = []  # initialisation de la liste des séries intermédiaire nécessaire à la recherche des binomes
        nombre_de_serie = len(self.message_) // (2 * self.N_)
        for i in range(0, nombre_de_serie + 1):  # parcour du message codé pour retrouvé les séries de taille 2*N
            liste_uplet += [self.message_[i * 2 * self.N_:(i + 1) * 2 * self.N_]]
        for uplet in liste_uplet:  # parcour des séries
            for j in range(len(uplet) // 2):  # reconstitution des binomes et formation de la liste
                binome = ["X", "X"]
                binome[0] = uplet[j]
                binome[1] = uplet[j + len(uplet) // 2]
                liste_binomes += [binome]
        return liste_binomes

    def chiffrement(self):
        """
        Fonction permettant de coder le massage
        :return: le message codé
        """
        message_code = ""  # initialisation du message codé
        nuplet = ""  # initialisation de la partie du message à codé, celui-ci est codé partie par partie dépendnt de la clef N
        for uplet in self.partition_message():  # Nous parcourons les séries formés en divisant les messages
            lignescode = ""  # initialisation
            colonnecode = ""
            nuplet = ""
            for lettre in uplet:  # Nous parcourons les lettres
                ligne, colonne = trouver_les_coordonnees(Grille_ordonnee,
                                                         lettre)  # Nous récupérons la position de la lettre dans la grille
                lignescode += Grille_ordonnee[ligne][0]  # première nouvelle lettre codant la lettre initiale
                colonnecode = colonnecode + Grille_ordonnee[4][
                    colonne]  # deuxième nouvelle lettre codant la lettre initiale
            nuplet += lignescode + colonnecode  # Partie du message de taille 2*N
            message_code += nuplet  # Ajout de la partie au message codé
        return message_code

    def dechiffrement(self):
        """
        Fonction permettant le decodage du message codé
        :return: le message decode
        """
        message = ""  # initialisation du message
        for binome in self.formation_de_binome():  # nous parcourons la liste des binomes
            ligne, y = trouver_les_coordonnees(Grille_ordonnee, binome[
                0])  # nous recherchons la lettre orignelle à partir des cordonnées des lettres du binome
            x, colonne = trouver_les_coordonnees(Grille_ordonnee, binome[1])
            message += Grille_ordonnee[ligne][colonne]
        return message


if __name__ == '__main__':
    # Test des diffentes fonctions
    Code = Collon("Lilian", 2)
    #print(Code.partition_message())
    print(Code.chiffrement())
    Decode = Collon(Code.chiffrement(), 3)
    print(Decode.formation_de_binome(), Decode.dechiffrement())
