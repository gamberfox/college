DROP TABLE IF EXISTS Cliente CASCADE;
CREATE TABLE Cliente
(
cedula VARCHAR(15) NOT NULL PRIMARY KEY,
nombre VARCHAR(50) NOT NULL,
direccion VARCHAR(50),
telefono VARCHAR(10)
);


DROP TABLE IF EXISTS Sala CASCADE;
CREATE TABLE Sala
(
numero_sala VARCHAR(4) NOT NULL PRIMARY KEY,
piso VARCHAR(2) NOT NULL,
capacidad INTEGER
);


DROP TABLE IF EXISTS Pelicula CASCADE;
CREATE TABLE Pelicula
(
codigo_pelicula VARCHAR(10) NOT NULL PRIMARY KEY,
titulo VARCHAR(30) NOT NULL,
genero VARCHAR(20),
director VARCHAR(50)
);


DROP TABLE IF EXISTS Proyeccion CASCADE;
CREATE TABLE Proyeccion
(
  numero_sala VARCHAR(4) NOT NULL,
  codigo_pelicula VARCHAR(10) NOT NULL,
  fecha VARCHAR(15),
  hora VARCHAR(10),
  FOREIGN KEY (codigo_pelicula) REFERENCES pelicula(codigo_pelicula),
  FOREIGN KEY (numero_sala) REFERENCES sala(numero_sala)
);


DROP TABLE IF EXISTS Peliculas_Cliente CASCADE;
CREATE TABLE Peliculas_Cliente
(
  codigo_pelicula VARCHAR(10) NOT NULL,
  cedula VARCHAR(15) NOT NULL,
  categoria VARCHAR(20),
  FOREIGN KEY (codigo_pelicula) REFERENCES pelicula(codigo_pelicula),
  FOREIGN KEY (cedula) REFERENCES cliente(cedula)
);