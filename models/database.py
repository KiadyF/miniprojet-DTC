import sqlite3
import pickle


class Database():
    def __init__(self):
        self.connexion = sqlite3.connect("data.db")
        self.curseur = self.connexion.cursor()
        self.creer_les_tables()

    # création des tables nécessaire
    def creer_les_tables(self):

        # Table user
        self.curseur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                password TEXT UNIQUE
                )
        """)

        # Table cours
        self.curseur.execute("""
            CREATE TABLE IF NOT EXISTS cours (
                id INTEGER PRIMARY KEY,
                titre TEXT,
                chapitre BLOB,
                user_id INTEGER,
                FOREIGN KEY(user_id) REFERENCES user(id)
                )
        """)

        # Table etudiants
        self.curseur.execute("""
            CREATE TABLE IF NOT EXISTS etudiants (
                id INTEGER PRIMARY KEY,
                nom TEXT,
                date DATE,
                matricule TEXT UNIQUE,
                cours_id INTEGER,
                FOREIGN KEY(cours_id) REFERENCES cours(id)
                )
        """)

        # Table seances des cours
        self.curseur.execute("""
            CREATE TABLE IF NOT EXISTS seances (
                id INTEGER PRIMARY KEY,
                date TEXT,
                sujet TEXT,
                details TEXT,
                cours_id INTEGER,
                temirner INTEGER,
                duree TEXT,
                FOREIGN KEY(cours_id) REFERENCES cours(id)
            )
        """)

        # Table des activités
        self.curseur.execute("""
            CREATE TABLE IF NOT EXISTS activites (
                id INTEGER PRIMARY KEY,
                seance_id INTEGER,
                description TEXT,
                FOREIGN KEY(seance_id) REFERENCES seances(id)
            )
        """)

        # Table des absences
        self.curseur.execute("""
            CREATE TABLE IF NOT EXISTS absences (
                id INTEGER PRIMARY KEY,
                matricule_etudiant TEXT,
                seance_id INTEGER,
                FOREIGN KEY(matricule_etudiant) REFERENCES etudiants(matricule),
                FOREIGN KEY(seance_id) REFERENCES seances(id)
            )
        """)

        self.connexion.commit()

    def ajouter_cours(self, titre, chapitres, user_id):
        chps = pickle.dumps(chapitres)
        self.curseur.execute("""
        INSERT INTO cours(titre,chapitre,user_id) VALUES(?,?,?)
        """, (titre, chps, user_id))
        self.connexion.commit()

    def ajouter_un_utilisateur(self, nom, pswd):
        self.curseur.execute("""
        INSERT INTO users(username,password) VALUES(?,?)
        """, (nom, pswd))
        self.connexion.commit()

    def ajouter_un_etudiant(self, nom, matricule, cours_id):
        curseur = self.connexion.cursor()
        curseur.execute(
            "INSERT INTO etudiants (nom, matricule,cours_id) VALUES (?,?,?)", (nom, matricule, cours_id))
        self.connexion.commit()

    def ajouter_une_seance(self, date, sujet, details, duree, cours):
        curseur = self.connexion.cursor()
        curseur.execute(
            "INSERT INTO seances (date, sujet, details,temirner,duree,cours_id) VALUES (?, ?, ?, ?, ?, ?)", (date, sujet, details, 0, duree, cours))
        self.connexion.commit()

    def ajouter_un_absent(self, matricule, seance_id):
        curseur = self.connexion.cursor()
        curseur.execute(
            "INSERT INTO absences (matricule_etudiant, seance_id) VALUES (?, ?)", (matricule, seance_id))
        self.connexion.commit()

    def ajouter_une_activite(self, seance_id, description):
        curseur = self.connexion.cursor()
        curseur.execute(
            "INSERT INTO activites (seance_id, description) VALUES (?, ?)", (seance_id, description))
        self.connexion.commit()

    def getuser(self, nom, pwd):
        row = self.curseur.execute("""
            SELECT * FROM users WHERE username = ? AND password = ?
        """, (nom, pwd))
        resultat = row.fetchone()
        if resultat:
            return resultat[0]
        return None

    def getcours(self, user_id):
        row = self.curseur.execute("""
        SELECT * FROM cours WHERE user_id = ?
        """, (user_id,))
        liste = []
        resultat = row.fetchall()
        for i in resultat:
            dictionnaires = {}
            chps = pickle.loads(i[2])
            dictionnaires['id'] = i[0]
            dictionnaires['titre'] = i[1]
            dictionnaires['chapitre'] = chps
            liste.append(dictionnaires)
        return liste

    def getEtudiant(self, cours_id):
        row = self.curseur.execute("""
        SELECT * FROM etudiants WHERE cours_id = ?
        """, (cours_id,))
        liste = []
        resultat = row.fetchall()
        for i in resultat:
            dictionnaires = {}
            dictionnaires['id'] = i[0]
            dictionnaires['nom'] = i[1]
            dictionnaires['date_naissance'] = i[2]
            dictionnaires['matricule'] = i[3]
            liste.append(dictionnaires)
        return liste

    def getNombreEtudiant(self):
        row = self.curseur.execute("""
        SELECT id FROM etudiants
        """)
        resultat = row.fetchall()
        if resultat:
            return (len(resultat))
        return 00

    def getSeances(self, cours_id):
        row = self.curseur.execute("""
        SELECT * FROM seances WHERE cours_id = ? AND temirner = ?
        """, (cours_id, 0))
        liste = []
        resultat = row.fetchall()
        for i in resultat:
            dictionnaires = {}
            dictionnaires['id'] = i[0]
            dictionnaires['date'] = i[1]
            dictionnaires['sujet'] = i[2]
            dictionnaires['duree'] = i[6]
            liste.append(dictionnaires)
        return liste

    def modifier_infos_etudiant(self):
        pass

    def modifier_un_absent(self):
        pass

    def modifier_une_seance(self):
        pass

    def modifier_une_activite(self):
        pass

    def fermer(self):
        self.connexion.close()
