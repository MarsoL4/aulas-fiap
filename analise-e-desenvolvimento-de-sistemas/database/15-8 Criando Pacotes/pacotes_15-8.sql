---------------------------------------
-- Preparação do ambiente        
-- Apagar a tabela empr.         
-- Criar e popular a tabela empr 
---------------------------------------

-- Apaga a tabela 'empr' caso ela exista.
DROP TABLE empr PURGE;

-- Cria a tabela 'empr' com campos de empregado.
CREATE TABLE empr
(cd_empregado NUMBER(5) PRIMARY KEY,
 nm_empregado VARCHAR2(30),
 vl_salario   NUMBER(9,2),
 vl_comissao  NUMBER(9,2),
 cd_depart    NUMBER(3));

-- Insere dados fictícios na tabela 'empr'.
INSERT INTO empr VALUES (100, 'Pulquéria', 12728.47, NULL,10);
INSERT INTO empr VALUES (110, 'Alarico', 890, 3000,20);
INSERT INTO empr VALUES (130, 'Absolon', 1200, 7000,30);
INSERT INTO empr VALUES (200, 'Kitty', 9870.22, NULL,20);

-- Confirma as alterações na tabela.
COMMIT;

---------------------------------
-- Códigos Exemplo para PACOTE  
---------------------------------

-- Cria o pacote 'comis_pkg' com funções e procedimentos para comissão.
CREATE OR REPLACE PACKAGE comis_pkg IS
  v_comiss_padrao  NUMBER := 0.10;  
  FUNCTION valida(p_comis NUMBER) RETURN BOOLEAN;
  PROCEDURE reset_comis(nova_comis NUMBER);
END comis_pkg;
/ 

-- Cria o corpo do pacote 'comis_pkg' com lógica de validação e reset de comissão.
CREATE OR REPLACE PACKAGE BODY comis_pkg IS
  FUNCTION valida(p_comis NUMBER) RETURN BOOLEAN IS
    v_max_comis 	empr.vl_comissao%type;
  BEGIN
    -- Verifica se a comissão está dentro do intervalo permitido.
    SELECT MAX(vl_comissao) INTO v_max_comis
    FROM empr;
    RETURN (p_comis BETWEEN 0 AND v_max_comis);
  END valida;

  PROCEDURE reset_comis (nova_comis NUMBER) IS 
     v_comiss_padrao empr.vl_comissao%type;
  BEGIN
    -- Se a comissão for válida, atualiza; caso contrário, gera um erro.
    IF valida(nova_comis) THEN
      v_comiss_padrao := nova_comis; 
    ELSE  RAISE_APPLICATION_ERROR(
            -20210, 'Comissão Inválida');
    END IF;
  END reset_comis;
END comis_pkg;
/ 

-- Executa procedimento para resetar a comissão para 10000.
execute comis_pkg.reset_comis(10000);

-- Executa procedimento para resetar a comissão para 1000 (causa erro se inválida).
execute comis_pkg.reset_comis(1000);

-- Cria um pacote 'global_consts' com constantes de conversão de unidades.
CREATE OR REPLACE PACKAGE global_consts IS
  c_mile_2_kilo    CONSTANT  NUMBER  :=  1.6093;
  c_kilo_2_mile    CONSTANT  NUMBER  :=  0.6214;
  c_yard_2_meter   CONSTANT  NUMBER  :=  0.9144;
  c_meter_2_yard   CONSTANT  NUMBER  :=  1.0936;
END global_consts;

-- Exibe a conversão de 20 milhas para quilômetros.
SET SERVEROUTPUT ON
BEGIN
   DBMS_OUTPUT.PUT_LINE('20 milhas = ' ||
        20 * global_consts.c_mile_2_kilo || ' km');
END;
/ 

-- Cria uma função que converte metros para jardas.
SET SERVEROUTPUT ON
CREATE OR REPLACE FUNCTION mtr2yrd(p_m NUMBER) RETURN NUMBER IS
BEGIN
  RETURN (p_m * global_consts.c_meter_2_yard);
END mtr2yrd;
/
-- Executa a função para converter 1 metro para jardas.
EXECUTE DBMS_OUTPUT.PUT_LINE(mtr2yrd(1))

-- Exibe todos os registros da tabela 'empr'.
select * from empr;

-- Exibe o código de empregado e a conversão de metros para jardas.
select cd_empregado, mtr2yrd(cd_empregado) from empr;
