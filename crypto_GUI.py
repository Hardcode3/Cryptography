# -*- coding:utf-8 -*-
__projet__ = "MODELISATION INFO"
__nom_fichier__ = "crypto_GUI"
__author__ = "PENOT Baptiste"
__date__ = "décembre 2021"

# !!!!!!!!! bibliothèques
#               - qdarkstyle
#               - qtpy
#               - matplotlib
#           à installer avant de lancer le programme !!!!!!!!!!

# importation des différentes classes utilisées pour les chiffres + matplotlib + qdarkstyle (thème pour pyqt5) nécessitant qtpy pour fonctionner
import sys
import ast
import qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# import des classes
from classes_et_fonctions.preparation_chiffre import del_accent_char
from classes_et_fonctions.cryptanalyse import histogramme
from classes_et_fonctions.beaufort import Beaufort
from classes_et_fonctions.beaufort_allemande import Beaufort_allemande
from classes_et_fonctions.bellaso import Bellaso
from classes_et_fonctions.Trithemius import Trithemius
from classes_et_fonctions.Gronsfeld import Gronsfeld
from classes_et_fonctions.procede_autoclave import Procede_autoclave
from classes_et_fonctions.variante_rozier import Vigenere_rozier
from classes_et_fonctions.Vigenere import Vigenere
from classes_et_fonctions.atbash import Atbash
from classes_et_fonctions.cesar import Cesar
from classes_et_fonctions.polybe import Polybe
from classes_et_fonctions.collon import Collon
from classes_et_fonctions.che import Che
from classes_et_fonctions.quatre_carres import Quatre_carres
from classes_et_fonctions.hill import Hill


# classe gérant l'interface graphique
class Mainwindow(QTabWidget):
    def __init__(self):
        super().__init__()

        # Mise en place de quelques caractères de la fenêtre principale de l'interface graphique (titre, icone, taille)
        self.setWindowTitle("Cryptographie - Cryptanalyse")
        self.setWindowIcon(QIcon("cadenas-ouvert.png"))
        self.setFixedSize(650, 300)

        # chaque page de la fenêtre principale est créée, nommée et enfin appellée via une méthode de la classe GUI
        ################################# PAGE 1 #################################
        self.tab_cryptographie_ = QWidget()
        self.addTab(self.tab_cryptographie_, "Cryptographie")
        self.tab_cryptographie_ui()

        ################################# PAGE 2 #################################
        self.tab_cryptoanalyse_ = QWidget()
        self.addTab(self.tab_cryptoanalyse_, "Cryptanalyse")
        self.tab_cryptanalyse_ui()

        ################################# PAGE 3 #################################
        self.tab_infos_ = QWidget()
        self.addTab(self.tab_infos_, "A propos")
        self.tab_infos_ui()

        ## liste des différentes classes selon si elles nécessitent ou non une cle de chiffrement, et si oui, de quel type
        # utilisé plus tard dans les méthodes indices et process
        # pour les clef à valeurs entières
        self.list_clef_int_ = [Gronsfeld, Cesar, Che]
        # pour les clefs sous forme de chaines de caractères
        self.list_cle_char_ = [Beaufort, Beaufort_allemande, Bellaso, Vigenere_rozier, Vigenere]
        # pour les méthodes qui ne nécessitent pas de clefs
        self.list_no_key_ = [Trithemius, Atbash, Polybe]

        ## Afin d'obtenir la classe associée à la sélection de la combobox, on utilise un dictionnaire
        # utilisé surtout dans la méthode selection_combobox_cryptographie
        self.dico_méthodes_ = {"Méthode de Beaufort": Beaufort, "Beaufort variante à l'Allemande": Beaufort_allemande,
                               "Méthode de Bellaso": Bellaso, "Méthode de Trithémius": Trithemius,
                               "Méthode de Gronsfeld": Gronsfeld,
                               "Procédé autoclave": Procede_autoclave, "Variante de Rozier": Vigenere_rozier,
                               "Méthode de Vigenère": Vigenere, "Méthode de Atbash": Atbash,
                               "Méthode de Polybe": Polybe,
                               "Méthode de César": Cesar, "Méthode de Collon": Collon, "Code du Che": Che,
                               "Quatre carrés": Quatre_carres, "Méthode de Hill": Hill}

        # un dictionnaire pour lier à chaque méthode une description de celle-ci, utilisé dans la méthode info_box
        self.dico_message_box_ = {
            Atbash: "Il s’agit d’une variante de la méthode de césar. Dans ce cas, pas besoin de clé, le nouvel alphabet est simplement l’alphabet à l’envers. Encore une fois, chaque lettre du mot à coder est remplacée par la lettre associée dans le nouvel alphabet (celui à l’envers). Par exemple, un A est codé par un Z et un C est codé par un X dans le cas de l’utilisation de la méthode de Atbash.  ",
            Trithemius : "Il s'agit d'une variante de lecture de la table de Trithème",
            Cesar: "Cette méthode est probablement parmi les plus simples. Elle nécessite un mot d’entrée que l’on souhaite coder ainsi qu’une clé. Un nouvel alphabet décalé de n rang est généré, « n » étant la clé donnée par l’utilisateur. Chaque lettre du mot à coder est ensuite remplacer par la lettre associée dans le nouvel alphabet. Par exemple, pour une clé valant 4, un A est codé par un E. ",
            Polybe: "Le nouvel alphabet est en fait une matrice 5x5 dont chacune des cases contient une lettre, les lettres I et J sont affectées dans la même case et ne seront donc pas différenciées lors du décodage d’un message par cette méthode. Pour coder un message par cette méthode, on affecte chaque lettre du message à coder à ses coordonnées (x, y) dans la matrice 5x5. Les coordonnées x comme y sont donc comprises entre 0 et 4. Par exemple, le message OUI ET NON sera codé par la suite d’entiers suivante : 233413 0433 222322.",
            Che: "Cette méthode mythique fut notamment utilisée par Che Guevara pour communiquer avec Fidel Castro. Elle est plus complexe que les précédentes car elle présente des étapes supplémentaires. Dans un premier temps, on effectue une simple substitution des différentes lettres du message à coder par les valeurs associées. On obtient donc une suite de chiffres compris entre 0 et 9. On regroupe cette suite en blocs de 5 chiffres que l’on additionne ensuite en modulo 10 avec une clé à 5 chiffres choisie par l’utilisateur. ",
            Vigenere: "Toute la méthode repose sur l’utilisation d’une table : la table de Trithème, reprise par Vigenère. Il s’agit d’un abaque sous la forme d’une matrice, comprenant 27 lignes et 27 colonnes. La première ligne et la première colonne servant de graduation, cette table permet de trouver un caractère en connaissant le message clair et sa clef.  ",
            Beaufort: "Dans cette variante du chiffre de Vigenère, les axes de lecture du chiffre et du message clair sont simplement inversés. Le principe reste le même.",
            Beaufort_allemande: "Cette variante résulte encore une fois d’une autre façon de lire la table de Trithème.",
            Vigenere_rozier: "Cette méthode de chiffrement possède un schéma de lecture significativement des autres méthodes puisque lettre du message clair et chiffré sont toutes deux lues sur la première ligne du tableau. D’autre part, la clef est utilisée deux fois : une première fois pour déterminer une lettre de la clef, et une seconde pour obtenir la lettre suivante. Bien que paraissant plus complexe, la méthode de Rozier se ramène à un chiffre de Vigenère simple en réalisant une permutation circulaire d’un cran sur la clef. ",
            Gronsfeld: "Cette méthode est basée sur l’utilisation d’une clef numérique, et non plus d’une chaine de caractères. La clef est adaptée à la taille du message, répétée ou recoupée si besoin. Chaque nombre correspondra à un décalage à imposer à chaque lettre du message clair. ",
            Procede_autoclave: "Ce chiffrement utilise une clef déterminée grâce au message clair. Une lettre est choisie et placée en première position devant celui-ci et constitue la clef. L’utilisateur qui chiffre a donc seulement besoin de choisir une lettre, et celui qui déchiffre doit connaître le message clair et sa lettre associée. ",
            Bellaso: "Belasso utilise un système légèrement moins élaboré que Porta tout en restant sur le même principe : une table contenant divers alphabets, tous constitués à partir d’un unique premier permet de chiffrer un message grâce à un clef. Cependant, Belasso travaille en termes de mots.  ",
            Hill: "Chaque caractère est remplacé par un nombre n (soit son rang diminué de 1 dans l’alphabet, soit son code ASCII, diminué de 32). Les caractères sont ensuite regroupés par bloc de p caractères. Les valeurs des caractères définissent alors un vecteur X. Une matrice A de taille p x p est ensuite choisie. La valeur du déterminant de la matrice est sélectionnée de façon qu’il soit premier avec la longueur de l’alphabet utilisé. Les autres termes de la matrice sont choisis de façon qu’elle soit inversible modulo n, ce qui est indispensable pour pouvoir décrypter le message. Les vecteurs Y sont ensuite calculés tels que : AX=Y ",
            Collon: "Le chiffrement selon la méthode de Collon nécessite une grille (5x5 généralement), et un nombre N donné. On sépare le message en série de N lettres. Pour chaque lettre, on cherche sa position dans la grille, pour ensuite trouver la lettre située la plus à gauche de la ligne et celle situé le plus en bas de la colonne. Ces deux nouvelles lettres remplaceront leur lettre d’origine dans le nouveau message. L’ordre appliqué pour le message codé est le suivant : les N lettres de ligne, puis les N lettres de colonne et ensuite une autre série est accolé. Par exemple, DCODE donne DC OD E donnant AAYXLAYYAZ une fois encodé. ",
            Quatre_carres: "La méthode utilise 4 carrés disposé comme le montre l’illustration ci-dessous. Les carrés du haut à gauche et du bas à droite contiennent les 25 lettres de l’alphabet (j souvent exclu), dans l’ordre alphabétique. Les deux autres contiennent également ces lettres mais disposées aléatoirement. La méthode consiste à découper le mot en paquet de deux lettres. La première est placé dans le carré ordonné du haut la seconde celui ordonné en bas. Deux droites verticales et horizontales sont ensuite tracé pour chaque lettre. L’intersection dans le carré désordonné du haut donne la première, la seconde se trouvant dans le carré désordonné du bas."
        }

    ################################# PAGE 1 #################################
    # première page qui gère toute la partie cryptographie
    def tab_cryptographie_ui(self):
        ### création des boutons et des différents objets de l'interface graphique ###
        ## création des boutons
        self.b_quitter_ = self.create_button("Quitter", qApp.quit)
        self.b_lancer_ = self.create_button("Lancer", self.process)
        self.b_tout_effacer_ = self.create_button("Tout effacer", self.tout_effacer)
        self.b_info_ = self.create_button("INFORMATIONS", self.infos_box)

        ## création des labels

        self.label_mot_ = self.create_label("Message clair : ")
        self.label_cle_ = self.create_label("Clé (si besoin) : ")
        self.label_result_ = self.create_label("Message chiffré : ")
        self.label_code_decode_ = self.create_label("Vous souhaitez : ")
        self.label_choix_methode_ = self.create_label("Choix de la méthode : ")
        self.label_indice_ = self.create_label("")

        ## création des line edits permettant l'édition du message clair, de la clef, et du résultat
        self.edit_mot_ = QLineEdit(self)
        self.edit_cle_ = QLineEdit(self)
        self.edit_result_ = QLineEdit(self)
        # afin de n'accepter que la saisie des chaines de caractères, on met en place un validator
        self.set_char_validator(self.edit_mot_)

        ## création des radio button permettant le choix codage/décodage
        self.radiob_code_ = QRadioButton("coder")
        self.radiob_decode_ = QRadioButton("décoder")

        ## création de la combo box permettant le choix du chiffre
        self.combobox_methodes_ = QComboBox()

        # label signalant que certaines méthodes codées n'ont pas été ajoutées à l'interface graphique
        self.label_indice_.setText(
            "Méthodes de Collon et des quatre carrés codées mais non implémentées dans l'application")

        # ajout des différentes options à la combobox
        self.combobox_methodes_.insertItem(0, "Sélectionner une méthode")
        self.combobox_methodes_.insertItem(1, "---- SUBSTITUTIONS MONOALPHABETIQUES ----")
        self.combobox_methodes_.insertItem(2, "Méthode de Atbash")
        self.combobox_methodes_.insertItem(3, "Méthode de Trithémius")
        self.combobox_methodes_.insertItem(4, "Méthode de Polybe")
        self.combobox_methodes_.insertItem(5, "Méthode de César")
        self.combobox_methodes_.insertItem(6, "Code du Che")
        self.combobox_methodes_.insertItem(7, "---- SUBSTITUTIONS POLYALPHABETIQUES ----")
        self.combobox_methodes_.insertItem(8, "Méthode de Beaufort")
        self.combobox_methodes_.insertItem(9, "Beaufort variante à l'Allemande")
        self.combobox_methodes_.insertItem(10, "Méthode de Bellaso")
        self.combobox_methodes_.insertItem(11, "Méthode de Gronsfeld")
        self.combobox_methodes_.insertItem(12, "Procédé autoclave")
        self.combobox_methodes_.insertItem(13, "Variante de Rozier")
        self.combobox_methodes_.insertItem(14, "Méthode de Vigenère")
        self.combobox_methodes_.insertItem(15, "---- CHIFFRE PAR CALCUL ----")
        self.combobox_methodes_.insertItem(16, "Méthode de Hill")
        self.combobox_methodes_.insertItem(17, "---- CHIFFRES POLYGRAPHIQUES ----")
        self.combobox_methodes_.insertItem(18, "Méthode de Collon")
        self.combobox_methodes_.insertItem(19, "Quatre carrés")

        # liste permettant de regrouper les onglets de la combobox qui ne devrons pas être sélectionnés et qui feront
        # donc apparaître un message d'erreur si sélectionné
        self.list_onglets_inutilisables_ = ["Sélectionner une méthode", "---- SUBSTITUTIONS MONOALPHABETIQUES ----",
                                            "---- SUBSTITUTIONS POLYALPHABETIQUES ----",
                                            "---- CHIFFRES POLYGRAPHIQUES ----", "Méthode de Collon", "Quatre carrés",
                                            "---- CHIFFRE PAR CALCUL ----"]

        # par défaut, le radio bouton de codage est coché et les line edits sont grisés en mode lecture uniquement
        self.edit_cle_.setReadOnly(True)
        self.edit_mot_.setReadOnly(True)
        self.edit_result_.setReadOnly(True)
        self.radiob_code_.setChecked(True)

        # l'interface choisie dans cette page de l'application est une grille
        interface = QGridLayout()

        # chaque choix d'une méthode dans la combobox appelle la méthode indice qui gère le label d'indices (permettant
        # à l'utilisateur d'être informé sur ce qu'il doit saisir ou non)
        self.combobox_methodes_.activated.connect(self.indices)

        ## placement des différents éléments sur l'interface
        # n° ligne / n° colonne / Nbe de lignes occupées / Nbe de colonnes occupées
        # boutons
        interface.addWidget(self.b_quitter_, 10, 0, 1, 1)
        interface.addWidget(self.b_lancer_, 9, 1, 1, 2)
        interface.addWidget(self.b_tout_effacer_, 9, 0, 1, 1)
        interface.addWidget(self.b_info_, 10, 1, 1, 2)

        # labels
        interface.addWidget(self.label_mot_, 3, 0, 1, 1)
        interface.addWidget(self.label_cle_, 5, 0, 1, 1)
        interface.addWidget(self.label_result_, 8, 0, 1, 1)
        interface.addWidget(self.label_code_decode_, 4, 0, 1, 1)
        interface.addWidget(self.label_choix_methode_, 1, 0, 1, 1)
        interface.addWidget(self.label_indice_, 2, 0, 1, 3)

        # line edit
        interface.addWidget(self.edit_mot_, 3, 1, 1, 2)
        interface.addWidget(self.edit_cle_, 5, 1, 1, 1)
        # interface.addWidget(self.edit_cle_complexes_, 5, 2, 1, 1)
        interface.addWidget(self.edit_result_, 8, 1, 1, 2)

        # radio button
        interface.addWidget(self.radiob_code_, 4, 1, 1, 1)
        interface.addWidget(self.radiob_decode_, 4, 2, 1, 1)

        # combobox
        interface.addWidget(self.combobox_methodes_, 1, 1, 1, 2)

        # application du layout à la page de l'application
        self.tab_cryptographie_.setLayout(interface)

    ################################# PAGE 2 #################################
    # seconde page qui gère toute la partie cryptanalyse
    def tab_cryptanalyse_ui(self):

        ## combobox permettant le choix de la langue pour l'analyse des fréquences des lettres sur les fichiers textes
        self.combobox_langue_ = QComboBox()

        # ajout à la combobox des items
        self.combobox_langue_.insertItem(0, "Français")
        self.combobox_langue_.insertItem(1, "Anglais")

        ## création des boutons et liaison aux différentes méthodes qu'ils appellent
        self.b_quitter_ = self.create_button("Quitter", qApp.quit)
        self.b_charger_fichier_ = self.create_button("Charger un fichier", self.charger_fichier)
        self.b_charger_fichier_.hide()
        self.b_lancer_histo_ = self.create_button("Lancer l'analyse d'occurence", self.plot_histo)
        self.b_effacer_ = self.create_button("Effacer", self.tout_effacer)
        self.b_lancer_bigramme_ = self.create_button("Fabriquer un bigramme", self.bigram)

        ## radio button permettant de choisir entre une saisie manuelle et la lecture d'un fichier pour les analyses de fréquences des lettres
        self.radio_buton_fichier_ = QRadioButton("Choisir un fichier")
        self.radio_buton_userinput_ = QRadioButton("Taper un texte")

        # le bouton saisie manuelle est coché par défaut
        self.radio_buton_userinput_.setChecked(True)

        # les radio button sont reliés à leurs méthodes respectives
        self.radio_buton_userinput_.toggled.connect(self.choix_entree_tab2)
        self.radio_buton_fichier_.toggled.connect(self.choix_entree_tab2)

        ## labels de la page de cryptanalyse
        self.label_langue0_ = self.create_label("Choix de la langue : ")
        self.label_langue1_ = self.create_label("(pour le choix du texte de référence)")
        self.label_import_ = self.create_label("Choisir une entrée : ")
        self.label_user_input_ = self.create_label("Entrer un texte : ")

        # label url permettant l'ouverture d'une page d'aide
        self.label_url_ = self.create_label(
            '<a href="https://www.apprendre-en-ligne.net/crypto/decrypt/reconnaitre.html">Reconnaître un chiffre - Ars Cryptographica<\a>')
        self.label_url_.setOpenExternalLinks(True)

        ## line edits permettant la saisie de la phrase à analyser et du fichier à ouvrir
        self.edit_filename_ = QLineEdit()

        # le lineedit affichant le nom du fichier lorsqu'il est sélectionné ne doit pas être modifiable : lecture seule
        self.edit_filename_.setReadOnly(True)

        self.edit_txt_tab2_ = QLineEdit()

        # le line edit n'accepte que les caractères puisque le but est d'analyser la fréquence des lettres
        self.set_char_validator(self.edit_txt_tab2_)

        ## le layout choisi est une grille
        interface = QGridLayout()

        ## disposition des différents éléments dans le layout
        # labels
        interface.addWidget(self.label_langue0_, 0, 0)
        interface.addWidget(self.label_langue1_, 0, 3)
        interface.addWidget(self.label_user_input_, 2, 0)
        interface.addWidget(self.label_import_, 1, 0)
        interface.addWidget(self.label_url_, 3, 1, 1, 2)

        # boutons
        interface.addWidget(self.b_quitter_, 5, 0)
        interface.addWidget(self.b_charger_fichier_, 2, 0)
        interface.addWidget(self.b_effacer_, 4, 0)
        interface.addWidget(self.b_lancer_histo_, 4, 1, 1, 3)
        interface.addWidget(self.b_lancer_bigramme_, 5, 1, 1, 3)
        interface.addWidget(self.combobox_langue_, 0, 1, 1, 2)

        # radio button
        interface.addWidget(self.radio_buton_fichier_, 1, 1)
        interface.addWidget(self.radio_buton_userinput_, 1, 2)

        # text edits
        interface.addWidget(self.edit_filename_, 2, 1, 1, 3)
        interface.addWidget(self.edit_txt_tab2_, 2, 1, 1, 3)

        ## application du layout à la page de cryptoanalyse de l'application
        self.tab_cryptoanalyse_.setLayout(interface)

    ################################# PAGE 2 #################################
    # seconde page qui affiche les informations sur l'application
    def tab_infos_ui(self):

        # les informations sur nous
        self.label_infos_ = self.create_label("Ce programme a été réalisé par :" + "\n"
                                              + "" + "\n"
                                              + "ACETO Lilian" + "\n"
                                              + "ARNAUT Théo" + "\n"
                                              + "CACHARD Benoit" + "\n"
                                              + "PENOT Baptiste" + "\n"
                                              + "" + "\n"
                                              + "étudiants à l'ENSG Nancy")

        # ajout d'une image à la page et centrage de l'image
        self.label_image_ = QLabel()
        self.label_image_.setAlignment(Qt.AlignCenter)
        self.label_image_.setPixmap(QPixmap("transparent-hash-icon_resized.png"))

        # l'interface est aussi une grille
        interface = QGridLayout()

        # les deux seuls éléments sont un label et l'image disposés côte à côte
        interface.addWidget(self.label_infos_, 0, 0)
        interface.addWidget(self.label_image_, 0, 1)

        # application du layout à la page infos de l'application
        self.tab_infos_.setLayout(interface)

        self.show()

    def process(self):
        """
        Méthode liée au bouton lancer : elle code ou décode une méthode choisie par l'utilisateur dans la combobox
        :return: None
        """
        # variables locales
        message = self.edit_mot_.text()
        cle = self.edit_cle_.text()
        result = self.edit_result_.text()

        # uniquement pour la méthode de Hill
        if self.selection_combobox_cryptographie() is Hill:
            # la cle est un string, si besoin convertie en liste grâce à la commande suivante
            cle = ast.literal_eval(cle)

        # exceptions : les méthodes qui requièrent d'être traitées à part pour le codage ou le décodage sont rentrées dans deux listes
        exceptions_codage = [Che, Quatre_carres]
        exceptions_decodage = [Che, Quatre_carres]

        # si la sélection de la combobox n'appelle pas une méthode de chiffrement, on affiche un message d'erreur
        if self.combobox_methodes_.currentText() in self.list_onglets_inutilisables_:
            self.crate_message_box("Sélectionner une méthode")

        # si le texte edit de la clef est vide et que la méthode choisie requiert une cle int ou char, on affiche un message d'erreur
        if (
                self.edit_cle_.text() == "" and (
                self.selection_combobox_cryptographie() in self.list_cle_char_ or self.selection_combobox_cryptographie() in self.list_clef_int_)):
            self.crate_message_box("Renseigner une clé", error=True)

        else:

            # lorsqu'aucun message clair n'est spécifié, message d'erreur
            if not self.edit_mot_.text():
                self.crate_message_box("Rentrer un mot à chiffrer")

            # si le radio button pour coder est coché, on code le message
            if self.radiob_code_.isChecked():

                # si la méthode choisie dans la combobox n'est pas une exception
                if self.selection_combobox_cryptographie() not in exceptions_codage:
                    # méthode générale pour afficher le message chiffré dans le text edit du résultat
                    self.edit_result_.setText(self.selection_combobox_cryptographie()(message, cle).chiffrement())

                # sinon si le message est une exception : par ex Che
                elif self.selection_combobox_cryptographie() is Che:
                    # méthode particulière pour le code du Che
                    self.edit_result_.setText(str(Che(message, cle).chiffrement()))

                # ou bien de l'exception de Hill (la cle est une liste de trois éléments)
                elif self.selection_combobox_cryptographie() is Hill:
                    self.edit_result_.setText(str(Hill(del_accent_char(message), cle).chiffrement()))

            # si le radio button décoder est coché, alors on décode le message
            if self.radiob_decode_.isChecked():

                # si la sélection de la combobox n'est pas une exception, méthode générale pour afficher le message décodé
                if self.selection_combobox_cryptographie() not in exceptions_decodage:
                    self.edit_mot_.setText(self.selection_combobox_cryptographie()(result, cle).dechiffrement())

                # sinon si il s'agit de l'exception Che
                elif self.selection_combobox_cryptographie() is Che:
                    result = ast.literal_eval(result)
                    self.edit_mot_.setText(Che(result, cle).dechiffrement())

                # ou bien de l'exception de Hill (la cle est une liste de trois éléments)
                elif self.selection_combobox_cryptographie() is Hill:
                    self.edit_mot_.setText(str(Hill(str(result), cle).dechiffrement()))

    def indices(self):
        """
        Gère l'affichage des indices sur le label indices en fonction de la sélection de la combobox
        - pour que l'utilisateur ait des informations sur la nature de ce qu'il doit saisir
        - pour mettre des validator afin d'éviter les erreurs liées à la saisie
        - pour mettre des text edits en lecture seule si besoin
        :return: None
        """
        ## à chaque changement de méthode de la combobox
        # le text du text edit est effacé afin d'éviter les erreurs liés aux validators
        self.edit_cle_.clear()
        self.edit_result_.clear()
        # les validateurs sont remis à 0 afin de pouvoir en changer selon la méthode choisie
        self.edit_mot_.setValidator(QRegularExpressionValidator())
        self.edit_cle_.setValidator(QRegularExpressionValidator())
        # les lectures seules sont remises à 0
        self.edit_mot_.setReadOnly(False)
        self.edit_cle_.setReadOnly(False)
        self.edit_result_.setReadOnly(False)

        self.label_cle_.setText("Clé (si besoin)")

        # si la méthode sélectionnée fait partie des sélections non souhaitées, message d'erreur et lecture seule de tous les line edits
        if self.combobox_methodes_.currentText() in self.list_onglets_inutilisables_:
            self.crate_message_box("Sélectionner une méthode", error=True)
            self.label_indice_.clear()
            self.edit_mot_.setReadOnly(True)
            self.edit_cle_.setReadOnly(True)
            self.edit_result_.setReadOnly(True)

        # si la méthode sélectionnée est ok et que le line edit de la clef n'est pas vide
        else:
            # si la méthode est à clef entière
            if self.selection_combobox_cryptographie() in self.list_clef_int_:
                self.edit_cle_.clear()

                # et si la méthode choisir est César, int validator + changement du label indice
                if self.selection_combobox_cryptographie() is Cesar:
                    self.label_indice_.setText(
                        "NB : La clef doit être un entier compris entre 0 et 25 (il s'agit du décalage)")
                    self.edit_cle_.setValidator(QIntValidator(0, 25))

                # et si la méthode choisir est Che, validator + changement du label indice
                if self.selection_combobox_cryptographie() is Che:
                    self.label_indice_.setText("NB : La clef doit être un nombre à 5 chiffres")
                    self.edit_cle_.setValidator(QIntValidator(0, 99999))
                    self.edit_result_.setReadOnly(True)

                # si la méthode est une des autres méthodes demandant un chiffre entier, message standardisé pour
                # le label + int validator
                else:
                    self.label_indice_.setText("NB : La cle doit être constituée de chiffres")
                    self.edit_cle_.setValidator(QIntValidator(0, 99999))

            # si la méthoe choisie requiert une clef = chaine de caractères
            if self.selection_combobox_cryptographie() in self.list_cle_char_:

                # et si la méthode n'est pas Bellaso, alors on appelle la méthode permettant d'appliquer un validator
                # pour les chaines de caractères + maj du label indice
                if self.selection_combobox_cryptographie is not Bellaso:
                    self.set_char_validator(self.edit_cle_)
                self.label_indice_.setText("NB : La clef doit être une chaine de caractères")

            # si la séélection de la combobox ne requiert aucune cle, lecture seule + changement du label indice
            if self.selection_combobox_cryptographie() in self.list_no_key_:
                self.label_indice_.setText("NB : Aucune cle n'est requise pour cette méthode")
                self.edit_cle_.setReadOnly(True)

            # si la méthode est procédé autoclave, alors validateur pour les strings + maj label indice
            if self.selection_combobox_cryptographie() is Procede_autoclave:
                self.set_char_validator(self.edit_cle_)
                self.label_indice_.setText("NB : Rentrer le message clair précédé d'une lettre de votre choix")

            if self.selection_combobox_cryptographie() is Hill:
                self.label_indice_.setText("NB : la clef doit être sous la forme : [a, b, c] avec a, b, c des entiers")
                self.edit_cle_.setText("[7, 5, 9]")

    def selection_combobox_cryptographie(self):
        """
        Renvoie le nom utilisable de la classe associée à la saisie de la combobox de la page cryptographie
        :return: nom de la classe qui peut maintenant être appelée
        """
        return self.dico_méthodes_[self.combobox_methodes_.currentText()]

    def infos_box(self):
        """
        Méthode liée au bouton informations de la page cryptographie et donnant des détails sur chaque méthodes
        afin de faciliter la saisie
        :return: None
        """

        # si la sélection de la combobox est un onglet d'information, alors message d'erreur
        if self.combobox_methodes_.currentText() in self.list_onglets_inutilisables_:
            self.crate_message_box("Sélectionner une méthode pour pouvoir chiffrer ou déchiffrer")
        # sinon, on affiche un message d'information sur la méthode en question, en faisant appel au dictionnaire message box
        else:
            choix_actuel_combobox = self.selection_combobox_cryptographie()
            information_message_box = "Détail sur la " + self.combobox_methodes_.currentText()
            self.crate_message_box(information_message_box, informations=self.dico_message_box_[choix_actuel_combobox])

    def create_button(self, text, methode=None):
        """
        Créé un bouton, en l'associant à une méthode
        :param text: texte écrit sur le bouton dans l'interface graphique
        :param methode: méthode liée au bouton
        :return: le bouton
        """
        bouton = QPushButton(text, self)

        if methode != None:
            bouton.clicked.connect(methode)
        return bouton

    def crate_message_box(self, main_message, informations=None, details=None, error=None):
        """
        Créé une message box d'information ou d'alerte selon le besoin
        :param main_message: message principal à afficher dans la message box
        :param informations: informations sur le message d'erreur, par défaut il n'y en a pas
        :param details: message détaillé sur l'erreur, par défaut il n'y en a pas
        :param error: par défaut sigle d'information, sinon ajoute un sigle d'erreur dans la fenêtre
        :return: None
        """

        # fonction pour créer un message box quelconque
        message_box_ = QMessageBox(self)
        # boutons par défaut : seulement le bouton ok
        message_box_.setStandardButtons(QMessageBox.Ok)
        message_box_.setText(main_message)
        message_box_.setIcon(QMessageBox.Information)
        if informations is not None:
            message_box_.setInformativeText(informations)
        if error is not None:
            message_box_.setIcon(QMessageBox.Warning)
        if details is not None:
            message_box_.setDetailedText(details)
        message_box_.exec()

    def create_label(self, text, position=center):
        """
        Créé un label aligné au centre par défaut
        :param text: texte du label
        :param position: centrée par défaut, modifiable si besoin
        :return: le label
        """
        label = QLabel(text, self)
        label.setAlignment(Qt.AlignCenter)
        return label

    def charger_fichier(self):
        """
        Ouvre un fichier grâce à une fenêtre de sélection, lit son contenu
        :return: None
        """

        # le contenu du fichier est initialisé
        self.contenu_fichier_ = ""

        # le fichier est choisi par l'utilisateur et ouvert
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File')
        self.edit_filename_.setText(filename)
        file = open(filename, 'r')

        # lecture du contenu du fichier
        self.contenu_fichier_ = ""
        for elt in file:
            self.contenu_fichier_ += elt
        file.close()

        # si aucun fichier n'est sélectionnée, message d'erreur
        if not self.edit_filename_.text():
            self.crate_message_box("Choisir un fichier", informations=True)

    def choix_entree_tab2(self):
        """
        Communique aux autres méthodes quel radio button de la page cryptanalyse est sélectionné
        :return: 1 si l'utilisateur a coché l'entrée manuelle
                 0 si il a choisi de sélectionner un fichier
        """
        if self.radio_buton_userinput_.isChecked():
            self.edit_filename_.hide()
            self.label_choix_methode_.hide()
            self.b_charger_fichier_.hide()
            self.edit_txt_tab2_.show()
            return 1

        elif self.radio_buton_fichier_.isChecked():
            self.edit_txt_tab2_.hide()
            self.edit_filename_.show()
            self.b_charger_fichier_.show()
            return 0

    def plot_histo(self):
        """
        Affiche un histogramme des fréquences des lettres avec les données d'entrée
        :return: None
        """
        # selon la langue choisie, on choisi un texte de référence à analyser : en FR ou en EN
        if self.combobox_langue_.currentIndex() == 0:
            self.text_for_histo_ref_ = "text_fr_aleatoire"
        else:
            self.text_for_histo_ref_ = "text_en_aleatoire"

        # si l'entrée manuelle est sélectionnée
        if self.choix_entree_tab2():

            # et que le text edit d'entrée manuelle est vide, message d'erreur
            if self.edit_txt_tab2_.text() == "":
                self.crate_message_box("Renseigner un message à analyser", error=True)

            # sinon on affiche l'histogramme avec les données d'entrées grâce au module matplotlib
            else:
                histogramme(self.edit_txt_tab2_.text(), text_ref=self.text_for_histo_ref_)

        # si l'entrée est un fichier
        elif not self.choix_entree_tab2():
            # et que le line edit du nom du fichier est vide, message d'erreur
            if self.edit_filename_.text() == "":
                self.crate_message_box("Sélectionner un fichier à analyser", error=True)

            # sinon affichage de l'histogramme grâce aux données d'entrée à l'aide de matplotlib
            else:
                histogramme(self.contenu_fichier_, text_ref=self.text_for_histo_ref_)

    def set_char_validator(self, object):
        """
        Permet d'appliquer un validateur sur un text edit de façon plus compacte et plus lisible : 1 ligne contre 3
        :param object: objet sur lequel est appliqué le validateur : line edit
        :return: None
        """
        regex = QRegExp("[a-z-A-Z_]+")
        char_validator = QRegExpValidator(regex)
        object.setValidator(char_validator)

    def tout_effacer(self):
        """
        Lié au bouton tout effacer, efface tous les line_edits de la page cryptographie et cryptanalyse
        :return:
        """
        self.edit_mot_.clear()
        self.edit_result_.clear()
        self.edit_cle_.clear()
        self.edit_filename_.clear()
        self.edit_txt_tab2_.clear()

    def bigram(self):
        """
        Affiche une fenêtre du bigramme du texte d'entrée
        :return: None
        """
        print("")


def main():
    ## creation d'un application
    app = QApplication(sys.argv)
    # application d'un thème foncé, plus esthétique
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    # ajout d'une icone de barre des tâches (non fonctionnel ?!)
    QSystemTrayIcon(QIcon("cadenas-ouvert.png")).show()

    # affichage de l'interface
    crypto = Mainwindow()
    crypto.show()

    # lancement de l'application
    r = app.exec_()


if __name__ == "__main__":
    main()
    # liste des codes non fonctionnels :
    # nf : collon
    # nf : quatre_carre
    # nf : porta
