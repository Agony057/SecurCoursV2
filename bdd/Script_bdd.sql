-- ---------------------------------------------------------------------------------------------------------------------------
-- -------------------------------------------- || SAE PARTIE 2 SQL || -------------------------------------------------------
-- ---------------------------------------------------------------------------------------------------------------------------
-- -------------------------------------- || Projet 1 : Gestion des Salles || ------------------------------------------------
-- ---------------------------------------------------------------------------------------------------------------------------
-- 
-- ---------------------------------------------------------------------------------------------------------------------------
-- -------------------------------------------- || Suppression TABLE || ------------------------------------------------------
-- ---------------------------------------------------------------------------------------------------------------------------
-- 
DROP TABLE IF EXISTS Identite CASCADE;
DROP TABLE IF EXISTS Casier CASCADE;
DROP TABLE IF EXISTS Classe CASCADE;
-- 
-- ---------------------------------------------------------------------------------------------------------------------------
-- ----------------------------------------------- || Création TABLE || ------------------------------------------------------
-- ---------------------------------------------------------------------------------------------------------------------------
-- 
CREATE TABLE Classe(
	id VARCHAR(10) NOT NULL CHECK(id IN('Vert', 'Bleu', 'Jaune', 'Rouge', 'Orange', 'Or')),
    Libelle VARCHAR(25) NOT NULL,
    PRIMARY KEY (id)
);
-- 
CREATE TABLE Casier(
	id INT NOT NULL CHECK(id > 0 && id <=2),
	Ouvert BOOLEAN NOT NULL DEFAULT FALSE,
	Libre BOOLEAN NOT NULL DEFAULT TRUE,
	PRIMARY KEY (id)
);
-- 
CREATE TABLE Identite(
	NoCarte VARCHAR(15) DEFAULT NULL,
    id VARCHAR(10),
    Nom VARCHAR(50) NOT NULL,
    Prenom VARCHAR (50) NOT NULL,
    Classe_id VARCHAR(15) NOT NULL,
	Statut VARCHAR(20) DEFAULT NULL CHECK(Statut IN('ADMIN', NULL)),
	Casier_id INT DEFAULT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (Classe_id) REFERENCES Classe(id),
	FOREIGN KEY (Casier_id) REFERENCES Casier(id)
);
--
-- ---------------------------------------------------------------------------------------------------------------------------
-- -------------------------------------------- || Insertion données || ------------------------------------------------------
-- ---------------------------------------------------------------------------------------------------------------------------
--
INSERT INTO Classe VALUES ('Bleu', 'Seconde Bac Pro TMA'),
						('Vert', 'Première Bac Pro TMA'),
                        ('Rouge', 'Terminale Bac Pro TMA'),
						('Jaune', 'Première CAP MF'),
                        ('Orange', 'Terminale CAP MF'),
						('Or', 'Professeur');
--
INSERT INTO Identite(NoCarte, Nom, Prenom, Classe_id, Statut, id) VALUES
							('000-000-000-000', 'BEAUDOUIN', 'Corentin', 'Or', 'ADMIN', 'BEACOR1'),
							('111-111-111-111', 'MENNINGER', 'Jason', 'Jaune', NULL, 'MENJAS1'),
							('222-222-222-222', 'ZELL', 'Renaud', 'Vert', NULL, 'ZELREN1'),
							('333-333-333-333', 'TIJOU', 'Allan', 'Jaune', NULL, 'TIJALA1'),
							('444-444-444-444', 'VIARDOT', 'Thibault', 'Vert', NULL, 'VIATHI1'),
							('555-555-555-555', 'AGOZZINO', 'Anthony', 'Bleu', NULL, 'AGOANT1');
-- 
INSERT INTO Casier(id) VALUES (1),(2);
-- 
-- -------------------------------------- || 2 select pour verifier les données des 2 tables || ------------------------------
-- 
SELECT * FROM Classe ORDER BY Libelle;
SELECT * FROM Identite ORDER BY Nom;
SELECT * FROM Casier ORDER BY id;
--
-- ---------------------------------------------------------------------------------------------------------------------------
-- -------------------------------------------------- || FIN DES Création || -------------------------------------------------
-- ---------------------------------------------------------------------------------------------------------------------------