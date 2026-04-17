--Tomada de Decisão

set serveroutput on;

DECLARE
    genero CHAR(1) := '&digite';
BEGIN
    IF upper(genero) = 'F' THEN
        dbms_output.put_line('O gênero informado é Feminino');
    ELSIF upper(genero) = 'M' THEN
        dbms_output.put_line('O gênero informado é Masculino');
    ELSE
        dbms_output.put_line('Outros');
    END IF;
END;

/----------------------------------------------------------------/
--Exercícios

-- 1) CRIAR UM BLOCO ANÔNIMO PARA INFORMAR SE O NÚMERO INFORMADO É PAR OU ÍMPAR.
set serveroutput on; 

DECLARE
    numero NUMBER := &digite;
BEGIN
    IF mod(numero, 2) = 0 THEN
        dbms_output.put_line('O número é Par');
    ELSE
        dbms_output.put_line('O número é Ímpar');
    END IF;
END;


-- 2) CRIAR UM BLOCO ANÔNIMO PARA INFORMAR O USUÁRIO SE A NOTA ESTÁ ACIMA DA MÉDIA, NA MÉDIA OU ABAIXO
/*
- ACIMA DE 8 E MENOR QUE 10 = NOTA ACIMA DA MÉDIA!
- ENTRE 6 E 7 = NA MÉDIA
- MENOR QUE 6 = REPROVADO
*/

set serveroutput on; 

DECLARE
    nota NUMBER := &digite;
BEGIN
    IF
        nota >= 8
        AND nota <= 10
    THEN
        dbms_output.put_line('SUA NOTA ESTÁ ACIMA DA MÉDIA');
    ELSIF nota BETWEEN 6 AND 7 THEN
        dbms_output.put_line('SUA NOTA ESTÁ NA MÉDIA');
    ELSE
        dbms_output.put_line('VOCÊ ESTÁ REPROVADO');
    END IF;
END;


