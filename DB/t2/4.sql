DROP TABLE IF EXISTS cliente CASCADE;
CREATE TABLE cliente
(
cedula VARCHAR(15) NOT NULL PRIMARY KEY,
nombre VARCHAR(50) NOT NULL,
direccion VARCHAR(50),
telefono VARCHAR(10)
);


DROP TABLE IF EXISTS sala CASCADE;
CREATE TABLE sala
(
numero_sala VARCHAR(4) NOT NULL PRIMARY KEY,
piso VARCHAR(2) NOT NULL,
capacidad INTEGER
);


DROP TABLE IF EXISTS pelicula CASCADE;
CREATE TABLE pelicula
(
codigo_pelicula VARCHAR(10) NOT NULL PRIMARY KEY,
titulo VARCHAR(30) NOT NULL,
genero VARCHAR(20),
director VARCHAR(50)
);


DROP TABLE IF EXISTS proyeccion CASCADE;
CREATE TABLE proyeccion
(
  numero_sala VARCHAR(4) NOT NULL,
  codigo_pelicula VARCHAR(10) NOT NULL,
  fecha VARCHAR(15),
  hora VARCHAR(10),
  FOREIGN KEY (codigo_pelicula) REFERENCES pelicula(codigo_pelicula),
  FOREIGN KEY (numero_sala) REFERENCES sala(numero_sala)
);


DROP TABLE IF EXISTS peliculas_cliente CASCADE;
CREATE TABLE peliculas_cliente
(
  codigo_pelicula VARCHAR(10) NOT NULL,
  cedula VARCHAR(15) NOT NULL,
  categoria VARCHAR(20),
  FOREIGN KEY (codigo_pelicula) REFERENCES pelicula(codigo_pelicula),
  FOREIGN KEY (cedula) REFERENCES cliente(cedula)
);

-- comandos para agregar cosas

INSERT INTO cliente(cedula,nombre,direccion,telefono) VALUES('123456','jon','calle 6 3-23','1123456')
INSERT INTO cliente VALUES('123457','mike','calle 7 32-34','112347')
INSERT INTO cliente VALUES('123458','mike','calle 8 3-35','112348')
INSERT INTO cliente VALUES('123459','mike','calle 9 3-36','112349')
INSERT INTO cliente VALUES('123450','mike','calle 0 3-37','112340')

INSERT INTO sala(numero_sala,piso,capacidad) VALUES('1','1',30)
INSERT INTO sala VALUES('1','1',30)
INSERT INTO sala VALUES('2','1',30)
INSERT INTO sala VALUES('3','2',20)
INSERT INTO sala VALUES('4','2',20)

INSERT INTO pelicula(codigo_pelicula,titulo,genero,director) VALUES('1234','stomp','comedy','jason')
INSERT INTO pelicula VALUES('1235','mad','drama','quentin')
INSERT INTO pelicula VALUES('1236','speed','action','steven')
INSERT INTO pelicula VALUES('1237','instance','drama','summer')
INSERT INTO pelicula VALUES('1238','godless','fantasy','yamamoto')

INSERT INTO proyeccion (numero_sala,codigo_pelicula,fecha,hora) VALUES('1','1234','14/04/2023','13:00') 
INSERT INTO proyeccion VALUES('1','1234','14/04/2023','13:00')
INSERT INTO proyeccion VALUES('1','1234','14/04/2023','13:00')
INSERT INTO proyeccion VALUES('1','1234','14/04/2023','13:00')
INSERT INTO proyeccion VALUES('1','1234','14/04/2023','13:00')

 numero_sala VARCHAR(4) NOT NULL,
  codigo_pelicula VARCHAR(10) NOT NULL,
  fecha VARCHAR(15),
  hora VARCHAR(10),