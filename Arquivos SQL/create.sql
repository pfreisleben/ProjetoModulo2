CREATE TABLE bestas (
	id serial NOT NULL,
	nome varchar(255) NOT NULL,
	tipo varchar(255) NOT NULL,
	niveldesafio int4 NOT NULL,
	descricaogeral varchar(1000) NOT NULL,
	ca int4 NOT NULL,
	pv int4 NOT NULL,
	deslocamento int4 NOT NULL,
	forca int4 NOT NULL,
	destreza int4 NOT NULL,
	constituicao int4 NOT NULL,
	inteligencia int4 NOT NULL,
	sabedoria int4 NOT NULL,
	carisma int4 NOT NULL,
	imagem_url varchar NULL,
	CONSTRAINT bestas_pkey PRIMARY KEY (id)
);