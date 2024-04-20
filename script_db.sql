create database construcao;

CREATE SCHEMA gastos AUTHORIZATION postgres;

create table users (
	id serial CONSTRAINT pk_id_autor PRIMARY KEY,
	nome varchar(100) not null,
	idade int not null, 
	sexo varchar(1)
);

INSERT INTO users
(nome, idade, sexo)
VALUES('junior', 25, 'M');

alter table users
	add column telefone varchar(12) not null default 'N/A';

select x.nome from users x where x.sexo = 'M';

select * from users where nome = 'junior';

select * from users u where telefone ilike '9%'; 


UPDATE users
SET nome='Júnior'
WHERE id=1;


