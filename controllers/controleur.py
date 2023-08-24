from vues import AcceuilFenetre, AjoutCoursFenetre, DetailsCoursFenetre, EnregistrationSeanceFenetre, GestionSeancesFenetre, InscriptionNewEtudiantFenetre, InscriptionNewUserFenetre, ListeEtudiantFenetre, FenetreLogin, PlannificationSeanceFenetre, AbsenceFenetre
from PySide6.QtWidgets import QDialog, QVBoxLayout, QApplication, QHBoxLayout, QPushButton, QLabel, QListWidgetItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from models import Database
from functools import partial
from datetime import datetime


class Controleur:
    def __init__(self):
        self.log = FenetreLogin()
        self.data = Database()
        self.log.login.clicked.connect(self.connecter)
        self.log.signup.clicked.connect(self.inscrire)
        self.log.show()

    def connecter(self):
        if self.log.username.text() == "" or self.log.password.text() == "":
            self.log.dialg.exec()
        else:
            self.user_id = self.data.getuser(
                self.log.username.text(), self.log.password.text())
            if self.user_id:
                self.log.username.clear()
                self.log.password.clear()
                self.acceuillir()
            else:
                self.log.dialg.exec()

    def inscrire(self):
        self.f_inscription = InscriptionNewUserFenetre()
        self.log.close()
        self.f_inscription.submit.clicked.connect(self.ajouter_new_user)
        self.f_inscription.cancel.clicked.connect(
            partial(self.revenir, self.f_inscription, self.log))
        self.f_inscription.show()

    def ajouter_new_user(self):
        if self.f_inscription.mdp.text() == "" or self.f_inscription.nom.text() == "" or self.f_inscription.confirm_mdp.text() == "":
            self.f_inscription.dialg.exec()
        elif self.f_inscription.confirm_mdp.text() != self.f_inscription.mdp.text():
            self.f_inscription.dialg_label.setText(
                "Merci de bien confirmer votre mot de passe")
            self.f_inscription.dialg.exec()
        elif self.data.getuser(self.f_inscription.nom.text(), self.f_inscription.mdp.text()):
            self.f_inscription.dialg_label.setText(
                "Cette utilisateur existe déjà.")
            self.f_inscription.dialg.exec()
        else:
            self.data.ajouter_un_utilisateur(
                self.f_inscription.nom.text(), self.f_inscription.mdp.text())
            self.f_inscription.close()
            self.log.show()

    def revenir(self, a, b):
        """
        a = fenetre à fermer
        b = fenetre à ouvrir
        """
        a.close()
        b.show()

    def acceuillir(self):
        self.log.close()
        self.f_acceuil = AcceuilFenetre()
        self.afficher_liste_cours()
        self.f_acceuil.Ajouter.clicked.connect(self.ajouter_chapitre)
        self.f_acceuil.deconnecter.clicked.connect(
            partial(self.revenir, self.f_acceuil, self.log))
        self.f_acceuil.show()

    def afficher_liste_cours(self):
        tous_les_cours = self.data.getcours(self.user_id)
        if not tous_les_cours:
            self.f_acceuil.couche.addWidget(QLabel("AUCUN"))
        else:
            for i in tous_les_cours:
                layout = QHBoxLayout()
                lbl = QLabel(i['titre'])
                btn_details = QPushButton("Details")
                btn_modifier = QPushButton("Modifier")
                btn_details.clicked.connect(partial(self.voir_le_cours, i))
                btn_details.setStyleSheet("""
                    QPushButton{
                        border-radius:10px;
                        background-color: rgb(255, 163, 72);
                        color: rgb(255, 255, 255);
                        }
                        QPushButton:pressed{
                        background-color: rgb(230, 97, 0);
                        }
                """)
                btn_modifier.setStyleSheet("""
                    QPushButton{
                        border-radius:10px;
                        background-color: rgb(255, 163, 72);
                        color: rgb(255, 255, 255);
                        }
                        QPushButton:pressed{
                        background-color: rgb(230, 97, 0);
                        }
                """)

                layout.addWidget(lbl)
                layout.addWidget(btn_details)
                layout.addWidget(btn_modifier)
                self.f_acceuil.couche.addLayout(layout)

    def ajouter_chapitre(self):
        self.f_acceuil.close()
        self.liste_chapitre = []
        self.f_ajouter_cours = AjoutCoursFenetre()
        self.f_ajouter_cours.newchpitre.returnPressed.connect(
            self.new_chapitre)
        self.f_ajouter_cours.cancel.clicked.connect(
            partial(self.revenir, self.f_ajouter_cours, self.f_acceuil))
        self.f_ajouter_cours.submit.clicked.connect(self.submit_cours)
        self.f_ajouter_cours.show()

    def new_chapitre(self):
        if self.f_ajouter_cours.newchpitre.text() == "":
            pass
        else:
            labl = QLabel(self.f_ajouter_cours.newchpitre.text())
            labl.setStyleSheet(
                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 190, 111, 255), stop:1 rgba(255, 255, 255, 255));")
            self.f_ajouter_cours.couche.addWidget(labl)
            self.liste_chapitre.append(self.f_ajouter_cours.newchpitre.text())
            self.f_ajouter_cours.newchpitre.clear()

    def submit_cours(self):
        titre = self.f_ajouter_cours.nom.text()
        if titre == "" or self.liste_chapitre == []:
            self.f_ajouter_cours.dialg.exec()
        else:
            self.data.ajouter_cours(titre, self.liste_chapitre, self.user_id)
            self.f_ajouter_cours.cancel.clicked.connect(
                partial(self.revenir, self.f_ajouter_cours, self.f_acceuil))
            self.f_ajouter_cours.close()
            self.acceuillir()

    def voir_le_cours(self, dic):
        self.f_cours = DetailsCoursFenetre()
        for i in dic['chapitre']:
            item = QListWidgetItem(i)
            item.setTextAlignment(Qt.AlignmentFlag.AlignHCenter)
            item.setFont(QFont('Times', 20))
            self.f_cours.plan.addItem(item)
        self.f_cours.retour.clicked.connect(
            partial(self.revenir, self.f_cours, self.f_acceuil))
        self.f_cours.deconnecter.clicked.connect(
            partial(self.revenir, self.f_cours, self.log))

        self.f_cours.gestionetudiant.clicked.connect(
            partial(self.gestion_etudiant, dic['id']))
        self.f_cours.gestionabsence.clicked.connect(self.gestion_absence)
        self.f_cours.seances.clicked.connect(
            partial(self.gestion_seances, dic['id']))
        self.revenir(self.f_acceuil, self.f_cours)

    def gestion_etudiant(self, id):
        self.f_etudiant = ListeEtudiantFenetre()
        self.afficher_les_etudiants(id)
        self.f_etudiant.ajoutNewEtudiant.clicked.connect(
            partial(self.ajouter_un_etudiant, id))
        self.f_etudiant.retour.clicked.connect(
            partial(self.revenir, self.f_etudiant, self.f_cours))
        self.revenir(self.f_cours, self.f_etudiant)

    def afficher_les_etudiants(self, id):
        self.liste_etudiant = self.data.getEtudiant(id)
        if self.liste_etudiant == []:
            self.f_etudiant.couche.addWidget(
                QLabel("VOUS N'AVEZ PAS ENCORE UN ETUDIANT INCRIT POUR LE COURS"))
        else:
            for i in self.liste_etudiant:
                layout = QHBoxLayout()
                lbl = QLabel(i['nom'])
                lbl.setMinimumHeight(40)
                btn_profils = QPushButton("Profils")
                btn_profils.setMinimumHeight(40)
                btn_supprimer = QPushButton("Supprimer")
                btn_supprimer.setMinimumHeight(40)
                btn_supprimer.setStyleSheet("""
                    QPushButton{
                        border-radius:10px;
                        background-color: rgb(255, 163, 72);
                        color: rgb(255, 255, 255);
                        }
                        QPushButton:pressed{
                        background-color: rgb(230, 97, 0);
                        }
                """)
                btn_profils.setStyleSheet("""
                    QPushButton{
                        border-radius:10px;
                        background-color: rgb(255, 163, 72);
                        color: rgb(255, 255, 255);
                        }
                        QPushButton:pressed{
                        background-color: rgb(230, 97, 0);
                        }
                """)
                layout.addWidget(lbl)
                layout.addWidget(btn_profils)
                layout.addWidget(btn_supprimer)
                self.f_etudiant.couche.addLayout(layout)

    def ajouter_un_etudiant(self, cours_id):
        self.f_ajouter_etudiant = InscriptionNewEtudiantFenetre()
        self.revenir(self.f_etudiant, self.f_ajouter_etudiant)
        self.f_ajouter_etudiant.cancel.clicked.connect(
            partial(self.revenir, self.f_ajouter_etudiant, self.f_etudiant))
        self.f_ajouter_etudiant.submit.clicked.connect(
            partial(self.enregistrer_etudiant, cours_id))

    def enregistrer_etudiant(self, cours_id):
        date = self.f_ajouter_etudiant.dateDeNaissance.date().toString("yyyy-MM-dd")
        nom = self.f_ajouter_etudiant.nom.text()
        prenom = self.f_ajouter_etudiant.prenom.text()
        matricule = 'DTC'+str(self.data.getNombreEtudiant())
        if nom == "" or prenom == "":
            self.f_ajouter_etudiant.dialg.exec()
        else:
            self.data.ajouter_un_etudiant((nom + prenom), matricule, cours_id)
            self.f_ajouter_etudiant.close()
            self.gestion_etudiant(cours_id)

    def gestion_absence(self):
        pass

    def gestion_seances(self, cours_id):
        self.f_seance = GestionSeancesFenetre()

        def afficher_les_seances():
            prochaine_seances = self.data.getSeances(cours_id)
            if prochaine_seances == []:
                self.f_seance.layout_prochaine_seance.addWidget(
                    QLabel("AUCUN"))
            else:
                print(prochaine_seances)
                for i in prochaine_seances:
                    layout = QHBoxLayout()
                    date = QLabel(i['date'])
                    date.setMinimumHeight(30)
                    sujet = QLabel("Sujet: "+i['sujet'])
                    sujet.setMinimumHeight(30)
                    duree = QLabel("Duree du cours: "+i['duree'])
                    duree.setMinimumHeight(30)
                    layout.addWidget(date)
                    layout.addWidget(sujet)
                    layout.addWidget(duree)
                    self.f_seance.layout_prochaine_seance.addLayout(layout)

        self.f_seance.retour.clicked.connect(
            partial(self.revenir, self.f_seance, self.f_cours))
        self.f_seance.deconnecter.clicked.connect(
            partial(self.revenir, self.f_seance, self.log))
        afficher_les_seances()
        self.f_seance.plannifier.clicked.connect(
            partial(self.plannifier_une_seance, cours_id))
        self.f_seance.enregistrer.clicked.connect(self.seance_terminer)
        self.revenir(self.f_cours, self.f_seance)

    def plannifier_une_seance(self, cours_id):
        self.f_plannifier_seance = PlannificationSeanceFenetre()

        def enregistrer():
            sujet = self.f_plannifier_seance.sujet.text()
            details = self.f_plannifier_seance.details.toPlainText()
            duree = self.f_plannifier_seance.duree.time().toString("hh:mm").replace(":", "H")
            date = self.f_plannifier_seance.date.dateTime().toString(
                "dd-MM-yyyy hh:mm").replace("-", "/").replace(":", "H")

            aujourdhui = datetime.now()
            date_seance = datetime.strptime(self.f_plannifier_seance.date.dateTime(
            ).toString("dd-MM-yyyy hh:mm"), "%d-%m-%Y %H:%M")
            if sujet == "" or details == "" or duree == "00H00":
                self.f_plannifier_seance.dialg.exec()
            elif aujourdhui > date_seance:
                self.f_plannifier_seance.label5.setText(
                    "Erreur,Vous avez taper une date déjà passé.")
                self.f_plannifier_seance.dialg.exec()
            else:
                self.data.ajouter_une_seance(
                    date, sujet, details, duree, cours_id)
                self.f_plannifier_seance.close()
                self.gestion_seances(cours_id)

        self.f_plannifier_seance.cancel.clicked.connect(
            partial(self.revenir, self.f_plannifier_seance, self.f_seance))
        self.f_plannifier_seance.submit.clicked.connect(enregistrer)
        self.revenir(self.f_seance, self.f_plannifier_seance)

    def enregistrer_une_seance(self):
        pass

    def seance_terminer(self):
        pass
