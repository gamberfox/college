DROP TABLE IF EXISTS cliente CASCADE;
CREATE TABLE cliente
(
cedula VARCHAR(10) NOT NULL PRIMARY KEY,
nombre VARCHAR(50) NOT NULL,
direccion VARCHAR(50),
telefono VARCHAR(10)
);


DROP TABLE IF EXISTS sala CASCADE;
CREATE TABLE sala
(
numero_sala VARCHAR(3) NOT NULL PRIMARY KEY,
piso VARCHAR(3) NOT NULL,
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
  fecha VARCHAR(10),
  hora VARCHAR(6),
  FOREIGN KEY (codigo_pelicula) REFERENCES pelicula(codigo_pelicula),
  FOREIGN KEY (numero_sala) REFERENCES sala(numero_sala)
);


DROP TABLE IF EXISTS pelicula_cliente CASCADE;
CREATE TABLE pelicula_cliente
(
  codigo_pelicula VARCHAR(10) NOT NULL,
  cedula VARCHAR(10) NOT NULL,
  categoria VARCHAR(20),
  FOREIGN KEY (codigo_pelicula) REFERENCES pelicula(codigo_pelicula),
  FOREIGN KEY (cedula) REFERENCES cliente(cedula)
);

-- comandos para agregar cosas

INSERT INTO cliente(cedula,nombre,direccion,telefono) VALUES('1111111111','jon','calle 1 3-23','1123451');
INSERT INTO cliente VALUES('1111111112','mike','calle 2 32-34','1123452');
INSERT INTO cliente VALUES('1111111113','dina','calle 3 43-35','1123453');
INSERT INTO cliente VALUES('1111111114','lucy','calle 4 12-36','1123454');
INSERT INTO cliente VALUES('1111111115','kevin','calle 5 65-37','1123455');
INSERT INTO cliente VALUES('10203040','Pedro Perez','calle 5 65-37','1123456');

INSERT INTO sala(numero_sala,piso,capacidad) VALUES('1','1',30);
INSERT INTO sala VALUES('2','1',30);
INSERT INTO sala VALUES('3','1',30);
INSERT INTO sala VALUES('4','2',20);
INSERT INTO sala VALUES('5','2',20);

INSERT INTO pelicula(codigo_pelicula,titulo,genero,director) VALUES('1234','stomp','comedy','jason');
INSERT INTO pelicula VALUES('1235','mad','drama','quentin');
INSERT INTO pelicula VALUES('1236','speed','action','steven');
INSERT INTO pelicula VALUES('1237','instance','drama','summer');
INSERT INTO pelicula VALUES('1238','godless','fantasy','yamamoto');

INSERT INTO proyeccion (numero_sala,codigo_pelicula,fecha,hora) VALUES('1','1234','14/04/2023','13:00');
INSERT INTO proyeccion VALUES('2','1235','14/04/2023','13:00');
INSERT INTO proyeccion VALUES('3','1236','14/04/2023','13:00');
INSERT INTO proyeccion VALUES('4','1237','14/04/2023','13:00');
INSERT INTO proyeccion VALUES('5','1238','14/04/2023','13:00');


INSERT INTO pelicula_cliente(codigo_pelicula,cedula,categoria) VALUES('1234','1111111111','infantil');
INSERT INTO pelicula_cliente VALUES('1235','1111111112','adultos');
INSERT INTO pelicula_cliente VALUES('1236','1111111113','adolescentes');
INSERT INTO pelicula_cliente VALUES('1237','1111111114','adultos');
INSERT INTO pelicula_cliente VALUES('1238','1111111115','adultos');
INSERT INTO pelicula_cliente VALUES('1236','10203040','adolescentes');

-- ejercicios: σ π ⋈
--1.π(nommbre, telefono)[σ(cedula=’10203040’) cliente]
--  SELECT  nombre,telefono FROM  cliente	WHERE  cedula='10203040';

--2.

--3.π(titulo,fecha)[σ(nombre='Pedro Perez') (cliente ⋈ [pelicula_cliente ⋈ (proyeccion ⋈ pelicula)])]
--  SELECT  titulo,fecha
--  FROM  cliente  NATURAL JOIN  pelicula_cliente NATURAL JOIN proyeccion NATURAL JOIN pelicula
--  WHERE nombre='Pedro Perez';


--4.π(numero_sala,piso,capacidad)
--          [σ(pelicula.genero=’drama’ OR pelicula.genero=’accion’) [Sala ⋈ (proyeccion ⋈ pelicula)]]
--  SELECT  numero_sala,piso,capacidad
--  FROM sala NATURAL JOIN (proyeccion NATURAL JOIN pelicula)
--  WHERE pelicula.genero='accion' OR pelicula.genero='drama';

--5.

--