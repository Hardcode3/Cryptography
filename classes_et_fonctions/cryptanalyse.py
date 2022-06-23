# -*- coding:utf-8 -*-
__projet__ = "CRYPTO"
__nom_fichier__ = "cryptanalyse"
__author__ = "PENOT Baptiste"
__date__ = "décembre 2021"

from matplotlib import pyplot
from classes_et_fonctions.preparation_chiffre import del_accent_char, alphabet

def ordonner_lettres(list_histo):
    list_histo_ordonnee = []
    for lettre_alphabet in alphabet[:26]:
        for lettre_histo in list_histo:
            if lettre_histo == lettre_alphabet:
                list_histo_ordonnee.append(lettre_alphabet)
    return list_histo_ordonnee


def donnees_histo_defaut(text):
    file = open(text, 'r')
    contenu = file.read()
    file.close()
    contenu = del_accent_char(contenu)

    traitement = []
    for elt in contenu:
        if elt in alphabet[:26]:
            traitement.append(elt)
    return ordonner_lettres(traitement)


def histogramme(message1, text_ref="text_en_aleatoire.txt"):
    message1 = del_accent_char(message1)
    histo2 = donnees_histo_defaut(text_ref)

    histo1 = del_accent_char(message1)

    histo1 = ordonner_lettres(histo1)

    pyplot.hist([histo2, histo1], range=(0, 26), bins=(26), color=["gold", "blue"],
                label=["Fréquences de référence", "Fréquences chiffre"], histtype='bar', density=True)
    pyplot.gcf().set_size_inches(8, 7)
    pyplot.xlabel("Lettres de l'alphabet")
    pyplot.ylabel("Fréquences d'apparition des lettres")
    pyplot.title(
        "Histogramme des fréquences d'apparition des lettres dans votre message" + "\n" + "comparé au texte de référence" + "\n" + "tiré du site Projet Gutemberg - libre de droit")
    pyplot.legend()
    pyplot.show()


if __name__ == '__main__':
    histogramme("jrbegfizyuerfigugyzgkjrehgfkrfuvjeyrtgfukz", "text_en_aleatoire")
