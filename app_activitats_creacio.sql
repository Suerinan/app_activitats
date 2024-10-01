show databases;

create database app_activitats;

use app_activitats;

show tables;

CREATE TABLE usuaris (
    dni_usuari VARCHAR(9) PRIMARY KEY,
    nom_usuari VARCHAR(20) NOT NULL,
    cognoms_usuari VARCHAR(50) NOT NULL,
    edad_usuari INT NOT NULL,
    contrasenya_usuari VARCHAR(16) NOT NULL
);

CREATE TABLE activitats (
    nom_activitat VARCHAR(20) PRIMARY KEY,
    descripcio_activitat TEXT,
    capacitat_maxima INT NOT NULL
);

CREATE TABLE usuari_activitat (
    dni_usuari VARCHAR(9),
    nom_activitat VARCHAR(20),
    PRIMARY KEY (dni_usuari, nom_activitat),
    FOREIGN KEY (dni_usuari) REFERENCES usuaris(dni_usuari) ON DELETE CASCADE,
    FOREIGN KEY (nom_activitat) REFERENCES activitats(nom_activitat) ON DELETE CASCADE
);

describe usuari_activitat;

INSERT INTO usuaris (dni_usuari, nom_usuari, cognoms_usuari, edad_usuari, contrasenya_usuari)
VALUES ('12345678A', 'Pepito', 'Grillo González', 19, 'password123');

INSERT INTO activitats (nom_activitat, descripcio_activitat, capacitat_maxima)
VALUES ('futbol', 'Un deporte de de dos equipos enfrentados. Gana quien mete gol', 22);

INSERT INTO usuari_activitat (dni_usuari, nom_activitat)
VALUES ('12345678A', 'futbol');
