CREATE DATABASE EscuelaMagica;

USE EscuelaMagica;

CREATE TABLE Alumnos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL,
    apellido VARCHAR(20) NOT NULL,
    identificacion VARCHAR(10) NOT NULL UNIQUE,
    edad TINYINT NOT NULL,
    afinidad_magica ENUM('Magia de Acero', 'Magia de Agua', 'Magia de Aire', 'Magia de Alas', 'Magia de Algodón', 'Magia de Almagre', 'Anti-Magia', 'Magia de Arena', 'Magia de Arenisca', 'Magia de Barro', 'Magia de Bestia', 'Magia de Bestia Demoníaca', 'Magia de Bronce', 'Magia de Brújula', 'Magia de Burbujas', 'Magia de Cadenas', 'Magia de Cabello', 'Magia de Canto', 'Magia de Cenizas', 'Magia de Cerezos', 'Magia de Cobre', 'Magia de Comida', 'Magia Compuesta', 'Magia de Comunicación', 'Magia de Corindón', 'Magia de Corte', 'Magia de Creación', 'Magia de Cristal', 'Magia de Cuerpo', 'Magia Curativa', 'Magia de Dados', 'Magia de Danza', 'Magia Debilitante', 'Magia de Espacio', 'Magia de Espadas', 'Magia de Espectros', 'Magia de Espejo', 'Magia de Espinas', 'Magia Espiritual', 'Magia de Fuego', 'Magia de Gel', 'Magia de Gravedad', 'Magia de Hielo', 'Magia de Hilos', 'Magia de Hongos', 'Magia de Huesos', 'Magia de Humo', 'Magia de Ilusión', 'Magia de Imitación', 'Magia de Juego', 'Magia Kotodama', 'Magia del Árbol del Mundo', 'Magia de Luz', 'Magia de Maleficio', 'Magia de Plantas Venenosas', 'Magia de Maldición', 'Método de Maná', 'Magia de Memoria', 'Magia de Mercurio', 'Magia de Mosquito', 'Magia de Mucosidad', 'Magia de Niebla', 'Magia de Nieve', 'Magia de Ojos', 'Magia de Oscuridad', 'Magia de Piedra', 'Magia de Pintura', 'Magia de Plantas', 'Magia de Plumas', 'Magia prohibida', 'Magia de Rayo', 'Magia de Recombinación', 'Magia de Reencarnación', 'Magia Reforzante', 'Magia de Restricción','Magia de Roca', 'Magia de Sangre', 'Magia de Sellado', 'Magia de Shakudo', 'Magia de Sombra', 'Magia de Sueños', 'Magia de Tiempo', 'Magia de Tierra', 'Trampa Mágica', 'Magia de Transformación', 'Magia de Transparencia', 'Magia de Veneno', 'Magia de Vidrio', 'Magia de Viento', 'Magia de Vídes', 'Magia de Vórtice', 'Magia de Árboles') NOT NULL,
    grimorio ENUM('Sinceridad – Trébol de 1 hoja', 'Esperanza – Trébol de 2 hojas', 'Amor – Trébol de 3 hojas', 'Buena Fortuna - Trébol de 4 hojas', 'Desesperación – Trébol de 5 hojas') NOT NULL
);

