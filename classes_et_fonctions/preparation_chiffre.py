# -*- coding:utf-8 -*-
__projet__ = "PROJET_CRYPTO"
__nom_fichier__ = "preparation_chiffre"
__author__ = "PENOT BAPTISTE"
__date__ = "novembre 2021"

alphabet = 5 * ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
                "V", "W", "X", "Y", "Z"]


def del_accent_char(chain, space=False):
    """
    FONCTION POUR ENLEVER LES ACCENTS - METTRE EN MAJUSCULE - ENLEVER LES ESPACES
    :param chain: une chaine de caractères comprenant des majuscules, minuscules, accents, ponctuations
    :return: cette même chaine en majuscule, sans accent ni ponctuation
    """

    # liste des accents possibles
    # table qui associe les valeurs ASCII avec accent aux valeurs sans accent
    table_correspondance = {192: 65,
                            193: 65,
                            194: 65,
                            195: 65,
                            196: 65,
                            197: 65,
                            198: 65,
                            199: 67,
                            200: 69,
                            201: 69,
                            202: 69,
                            203: 69,
                            204: 73,
                            205: 73,
                            206: 73,
                            207: 73,
                            208: 68,
                            209: 78,
                            210: 79,
                            211: 79,
                            212: 79,
                            213: 79,
                            214: 79,
                            216: 79,
                            217: 85,
                            218: 85,
                            219: 85,
                            220: 85,
                            221: 89,
                            224: 97,
                            225: 97,
                            226: 97,
                            227: 97,
                            228: 97,
                            229: 97,
                            230: 97,
                            231: 99,
                            232: 101,
                            233: 101,
                            234: 101,
                            235: 101,
                            236: 105,
                            237: 105,
                            238: 105,
                            239: 105,
                            240: 111,
                            241: 110,
                            242: 111,
                            243: 111,
                            244: 111,
                            245: 111,
                            246: 111,
                            248: 111,
                            249: 117,
                            250: 117,
                            251: 117,
                            252: 117,
                            253: 121,

                            # la plupart des caractères spéciaux
                            33: 32,
                            34: 32,
                            35: 32,
                            36: 32,
                            37: 32,
                            38: 32,
                            39: 32,
                            40: 32,
                            41: 32,
                            42: 32,
                            43: 32,
                            44: 32,
                            45: 32,
                            46: 32,
                            47: 32,
                            58: 32,
                            59: 32,
                            60: 32,
                            61: 32,
                            62: 32,
                            63: 32,
                            64: 32,
                            95: 32,
                            96: 32,
                            145: 32,
                            146: 32,
                            147: 32,
                            148: 32,
                            }

    new_chain = ""

    for rg in range(len(chain)):
        # si le code ASCII décimal correspond à une lettre accentuée
        ascii_char = ord(chain[rg])

        if 192 <= ascii_char <= 214 or 216 <= ascii_char <= 253 or 33 <= ascii_char <= 47 or 58 <= ascii_char <= 64 or 95 <= ascii_char <= 96 or 145 <= ascii_char <= 148:
            # alors on obtient le code ASCII décial de la lettre non accentuée associée
            # ord() obtient le code ASCII décimal du caractère
            # chr() donne le caractère à partir de la décimale ASCII
            new_chain += str(chr(table_correspondance[ord(chain[rg])]))

        else:
            new_chain += chain[rg]
    # pour mettre en majuscule et enlever les espaces dans le mot chiffré

    if space == 0:
        # si la valeur de space est celle par défaut (False) alors on enlève les espaces, sinon, si c'est spécifié, on ne les enlève pas
        new_chain = new_chain.replace(" ", "")
    return new_chain.upper()


def adapt_clef(mot, clef, taille_sup_clef=0):
    """
    FONCTION POUR ADAPTER LA TAILLE DE LA CLEF AU MOT À CHIFFRER
    :param mot: un mot à chiffrer (string)
    :param clef: une clef permettant de chiffrer le mot (string)
    :param taille_sup_clef : taille de la clef par rapport au message
    (pour certaines méthodes, on a besoin que la clef soit plus longue d'un certain nombre de caractères)
    :return: une clef adaptée à la taille du mot (répétée ou coupée)
    """
    if len(mot) < len(clef):
        # si le mot est plus cour que la clef, alors on coupe la clef à la longueur du mot
        return clef[0:len(mot) + taille_sup_clef]

    elif len(mot) > len(clef):
        # si le mot est plus long, alors on répète la clef autant de fois que nécessaire pour que mot et clef aient la même taille
        clef_f = clef
        counter = 0
        while len(mot) > len(clef_f) and counter < 20:
            counter += 1
            clef_f += clef
        return clef_f[0:len(mot) + taille_sup_clef]

    else:
        # si la clef est déjà de la même taille que le mot, rien à faire
        return clef


if __name__ == '__main__':
    print(adapt_clef("test", "fromage"))
    print(adapt_clef("anticonstitutionnellement", "chien"))
    print(adapt_clef('test', "parc"))
    print(del_accent_char("è à ' ", space = 0))
