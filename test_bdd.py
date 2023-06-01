import mysql.connector

baseDeDonnees = mysql.connector.connect(host="devbdd.iutmetz.univ-lorraine.fr", user="agozzino3u_appli",
                                        password="32222926", database="agozzino3u_SAE_ProjetTuteure")
cursor = baseDeDonnees.cursor()
# cursor.execute("CREATE TABLE Identite (uid varchar(20) PRIMARY KEY, nom varchar(20) not null, prenom varchar(20) not null) ")
# cursor.execute("insert into Identite values ('21551', 'AGOZZINO', 'Anthony')")
# cursor.execute("insert into Identite values ('21851', 'ZELL', 'Renaud')")
# baseDeDonnees.commit()
cursor.execute("SELECT * FROM Identite ORDER BY Nom")
rows = cursor.fetchall()
print(rows)
# print(rows[0][0]) Tableau dans un tableau le résultat de fetchall
print()
# print(len(rows)) Longueur de la table
for row in rows:
    print(row)

print()

tuple = ("'ZELL'")
query = f"Select * from Identite where Nom = {tuple} "
cursor.execute(query)
print(cursor.fetchall())
