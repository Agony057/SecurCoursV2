import mysql.connector

baseDeDonnees = mysql.connector.connect(host="devbdd.iutmetz.univ-lorraine.fr", user="agozzino3u_appli",
                                        password="32222926", database="agozzino3u_SAE_ProjetTuteure")
cursor = baseDeDonnees.cursor()

def demande_casier(casier):
    # retourne le nombre de personne qui ont le casier demandé
    req_demande_casier = f"SELECT COUNT(*) FROM Identite WHERE Casier_id = '{casier}'"
    cursor.execute(req_demande_casier)
    return cursor.fetchone()[0]


def efface_casier(casier):
    # remplace numéro de casier de l'étudiant par null
    req_efface_casier = f"UPDATE Identite " \
                           f"SET Casier_id = NULL " \
                           f"WHERE Casier_id = '{casier}'"
    cursor.execute(req_efface_casier)


def casier_libre_occupe(casier):
    # occuper un casier
    req_casier_libre_occupe = "UPDATE Casier " \
                        "SET Libre = FALSE " \
                        f"WHERE id = '{casier}'"

def casier_occupe_libre(casier):
    # liberer un casier
    req_casier_occupe_libre = "UPDATE Casier " \
                    "SET Libre = TRUE " \
                    f"WHERE id = '{casier}'"


def identite_utilsateur_casier(casier):
    # retourne nom prenom classe d'un utilisateur par son casier
    req_utilisateur_casier = f"SELECT Nom, Prenom, Classe_id FROM Identite WHERE Casier_id = {casier}"
    cursor.execute(req_utilisateur_casier)
    return cursor.fetchone()


def identifiant_existe(identifiant):
    # retourne le nombre de personnes qui ont déjà cet identifiant
    req_identifiant_existe = f"SELECT COUNT(*) FROM Identite WHERE id = '{identifiant}'"
    cursor.execute(req_identifiant_existe)
    return cursor.fetchone()[0]


def uid_existe(uid):
    # retourne le nombre de personnes qui ont déjà cet uid
    req_uid_existe = f"SELECT COUNT(*) FROM Identite WHERE NoCarte = '{uid}'"
    cursor.execute(req_uid_existe)
    return cursor.fetchone()[0]


def identite_utilisateur_uid(uid):
    # retourne le nom prenom classe d'un utilisateur par son uid
    req_utilisateur_uid = f"SELECT Nom, Prenom, Classe_id FROM Identite WHERE NoCarte = '{uid}'"
    cursor.execute(req_utilisateur_uid)
    return cursor.fetchone()


def efface_uid(uid):
    # remplace l'uid de l'utilisateur par null
    req_efface_uid = f"UPDATE Identite " \
                           f"SET NoCarte = NULL " \
                           f"WHERE NoCarte = '{uid}'"
    cursor.execute(req_efface_uid)


def demande_ajout(nom, prenom, classe):
    # retourne le nombre de personne qui ont le meme nom prenom et classe
    req_demande_ajout = f"SELECT COUNT(*) FROM Identite WHERE Nom = '{nom}' AND Prenom = '{prenom}' AND Classe_id = '{classe}'"
    cursor.execute(req_demande_ajout)
    return cursor.fetchone()[0]


def liste_classe_eleve():
    # retourne les id des classes sans la classe Or = Professeur
    req_liste_classe_eleve = "SELECT id FROM Classe WHERE id != 'Or'"
    cursor.execute(req_liste_classe_eleve)
    return cursor.fetchall()


def liste_casier_libre():
    #retourne liste de casier libre
    req_liste_casier_libre = "SELECT id FROM Casier WHERE Libre = TRUE"
    cursor.execute(req_liste_casier_libre)
    return cursor.fetchall()


def ajout(uid, identifiant, nom, prenom, classe, casier):
    # ajouter un utilisateur a la base de donnée
    if len(uid) == 0 and len(casier) == 0:
        # condition sans uid et sans casier
        req_ajout = "INSERT INTO Identite(id, Nom, Prenom, Classe_id) VALUES " \
                    f"('{identifiant}', '{nom}', '{prenom}', '{classe}')"
    elif len(uid) == 0:
        # condition sans uid
        req_ajout = "INSERT INTO Identite(id, Nom, Prenom, Classe_id, Casier_id) VALUES " \
                    f"('{identifiant}', '{nom}', '{prenom}', '{classe}', {casier})"
    elif len(casier) == 0:
        # condition sans casier
        req_ajout = "INSERT INTO Identite(id, NoCarte, Nom, Prenom, Classe_id) VALUES " \
                    f"('{identifiant}', '{uid}', '{nom}', '{prenom}', '{classe}')"
    else:
        # sans condition avec casier et avec uid
        req_ajout = "INSERT INTO Identite(id, NoCarte, Nom, Prenom, Classe_id, Casier_id) VALUES " \
                    f"('{identifiant}', '{uid}', '{nom}', '{prenom}', '{classe}', {casier})"
    cursor.execute(req_ajout)
    # commit obligatoire pour mise à jour de la base donnée
    baseDeDonnees.commit()


def modifier_eleve(id, uid, nom, prenom, classe, casier):
    # modifier un utilisateur de la base de donnée
    if len(uid) == 0 and len(casier) == 0:
        req_modif = "UPDATE Identite " \
                    f"SET Nom = '{nom}', Prenom = '{prenom}', Classe_id = '{classe}' " \
                    f"WHERE id = '{id}'"
    elif len(uid) == 0:
        req_modif = "UPDATE Identite " \
                    f"SET Nom = '{nom}', Prenom = '{prenom}', Classe_id = '{classe}', Casier_id = {casier} " \
                    f"WHERE id = '{id}'"
    elif len(casier) == 0:
        req_modif = "UPDATE Identite " \
                    f"SET NoCarte = '{uid}', Nom = '{nom}', Prenom = '{prenom}', Classe_id = '{classe}' " \
                    f"WHERE id = '{id}'"
    else:
        req_modif = "UPDATE Identite " \
                    f"SET NoCarte = '{uid}', Nom = '{nom}', Prenom = '{prenom}', " \
                    f"Classe_id = '{classe}', Casier_id = {casier} " \
                    f"WHERE id = '{id}'"
    cursor.execute(req_modif)
    # commit obligatoire pour mise à jour de la base donnée
    baseDeDonnees.commit()


cursor.execute("SELECT * FROM Identite ORDER BY Nom")
rows = cursor.fetchall()
# print(rows)
# # print(rows[0][0]) # Tableau dans un tableau le résultat de fetchall
# print()
# # print(len(rows)) Longueur de la table
for row in rows:
    print(row)

# print()

# tuple = ("'ZELL'")
# query = f"Select * from Identite where Nom = {tuple} "
# cursor.execute(query)
# print(cursor.fetchall())


# query = f"insert into Identite(NoCarte, Nom, Prenom, Classe_id, Casier_id) VALUES ('{uid}', 'ZZZ', 'Zzz', 'Vert', {casier})"
# cursor.execute(query)
# baseDeDonnees.commit()

