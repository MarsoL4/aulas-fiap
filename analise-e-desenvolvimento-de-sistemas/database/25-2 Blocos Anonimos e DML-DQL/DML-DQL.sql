-- Criação da Tabela aluno
/*
CREATE TABLE aluno (
    ra   CHAR(9),
    nome VARCHAR2(50),
    CONSTRAINT aluno_pk PRIMARY KEY ( ra )
);
*/

-- Insere dados iniciais na Tabela aluno
/*
INSERT INTO aluno (ra, nome) VALUES ('111222333', 'Antonio Alves');
INSERT INTO aluno (ra, nome) VALUES ('333444555', 'Beatriz Bernardes');
INSERT INTO aluno (ra, nome) VALUES ('555666777', 'Cláudio Cardoso');
*/

-- Exemplo de Instrução DQL:
DECLARE
    v_ra   CHAR(9) := '333444555';
    v_nome VARCHAR2(50);
BEGIN
    SELECT
        nome
    INTO v_nome
    FROM
        aluno
    WHERE
        ra = v_ra;

    dbms_output.put_line('O nome do aluno é: ' || v_nome);
END;

-- Exemplo de Instrução DML 1:
DECLARE 
	V_RA CHAR(9) := '444555666'; 
	V_NOME VARCHAR2(50) := 'Daniela Dorneles'; 
BEGIN 
	INSERT INTO ALUNO (RA,NOME) VALUES (V_RA,V_NOME); 
END;

-- Exemplo de Instrução DML 2:
DECLARE
    v_ra   CHAR(9) := '111222333';
    v_nome VARCHAR2(50) := 'Antonio Rodrigues';
BEGIN
    UPDATE aluno
    SET
        nome = v_nome
    WHERE
        ra = v_ra;

END;

-- Exemplo de Instrução DML 3:
DECLARE
    v_ra CHAR(9) := '444555666';
BEGIN
    DELETE FROM aluno
    WHERE
        ra = v_ra;

END;




    
    