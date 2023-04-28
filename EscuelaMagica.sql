CREATE DATABASE EscuelaMagica;

USE EscuelaMagica;

CREATE TABLE Alumnos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL,
    apellido VARCHAR(20) NOT NULL,
    identificacion VARCHAR(10) NOT NULL UNIQUE,
    edad TINYINT NOT NULL,
    afinidad_magica ENUM('Magia de Acero', 'Magia de Agua', 'Magia de Aire', 'Magia de Alas', 'Magia de Algodón') NOT NULL,
    grimorio ENUM('Sinceridad', 'Esperanza', 'Amor', 'Buena Fortuna', 'Desesperación') NOT NULL
);
