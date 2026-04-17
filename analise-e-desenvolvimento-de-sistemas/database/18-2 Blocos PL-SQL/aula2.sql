--Seleciona os paises que tem de 1 a 5 estados:
/*SELECT
    a.nom_pais          pais,
    COUNT(b.nom_estado) "QTD ESTADOS"
FROM
    pf1788.pais   a
    LEFT JOIN pf1788.estado b ON ( a.cod_pais = b.cod_pais )
GROUP BY
    a.nom_pais
HAVING
    COUNT(b.nom_estado) BETWEEN 1 AND 5
ORDER BY
    2 DESC
    
    
--Seleciona os paises que tem mais de 5 estados:
SELECT
    a.nom_pais          pais,
    COUNT(b.nom_estado) "QTD ESTADOS"
FROM
    pf1788.pais   a
    LEFT JOIN pf1788.estado b ON ( a.cod_pais = b.cod_pais )
GROUP BY
    a.nom_pais
HAVING
    COUNT(b.nom_estado)>5
ORDER BY
    2 DESC
 
 
-- Vê quantas cidades um estado tem:
SELECT
    a.nom_pais          pais,
    b.nom_estado        estado,
    COUNT(c.nom_cidade) "QTD CIDADES"
FROM
         pf1788.pais a
    JOIN pf1788.estado b ON ( a.cod_pais = b.cod_pais )
    LEFT JOIN pf1788.cidade c ON ( b.cod_estado = c.cod_estado )
GROUP BY
    a.nom_pais,
    b.nom_estado
ORDER BY
    3 DESC,1,2
*/


-- INTRODUÇÃO A BLOCO ANÔNIMO
SET SERVEROUTPUT ON;
DECLARE
    idade NUMBER; --Define o tipo da variável idade
    nome  VARCHAR2(30) := 'VERGS';
    ende   VARCHAR2(50) := '&ENDERECO'; -- o '&' indica que o valor do endereço deverá ser inserido na execução manualmente
BEGIN
    idade := 39; --Define o valor da idade
    dbms_output.put_line('A IDADE INFORMADA É: ' || idade); --No terminal será exibida essa frase com a variável idade onde foi indicado
    dbms_output.put_line('O NOME INFORMADO É: ' || nome);
    dbms_output.put_line('ENDEREÇO INFORMADO É: ' || ende);
END;


--Exercício 1: Criar um bloco PL-SQL para calcular o valor do novo salário mínimo que deverá ser de 25% em cima do atual, que é de R$ ?????.
DECLARE
    v_salario_atual NUMBER := 1509; -- Substitua pelo valor atual do salário mínimo
    v_novo_salario  NUMBER;
BEGIN
	   -- Calcula o novo salário com aumento de 25%
    v_novo_salario := v_salario_atual * 1.25;
   -- Exibe o resultado
    dbms_output.put_line('Salário atual: R$ ' || to_char(v_salario_atual, '999G999D99'));
    dbms_output.put_line('Novo salário com 25% de aumento: R$ ' || to_char(v_novo_salario, '999G999D99'));
END;


-- Exercício 2: Criar um bloco PL-SQL para calcular o valor em REAIS de 45 dólares, sendo que o valor do câmbio a ser considerado é de R$????.
DECLARE
    v_dolar NUMBER := 45;
    v_reais NUMBER;
BEGIN
    v_reais := v_dolar * 6;
    dbms_output.put_line('Valor em dólar: $ ' || v_dolar);
    dbms_output.put_line('Valor em reais: R$ ' || v_reais);
END;


/*--Exercício 3: Criar um bloco PL-SQL para calcular o valor das parcelas de uma compra de um carro, nas seguintes condições: 
OBSERVAÇÃO: 
1 - Parcelas para aquisição em 10 pagamentos. 
2 - O valor da compra deverá ser informado em tempo de execução. 
3 – O valor total dos juros é de 3% e deverá ser aplicado sobre o montante financiado 
4 – No final informar o valor de cada parcela.*/
DECLARE
    carro NUMBER := &valor;
BEGIN
    dbms_output.put_line('Valor do carro á vista: R$ ' || carro);
    dbms_output.put_line('Valor de cada parcela: R$ ' ||(carro * 1.03) / 10);
    dbms_output.put_line('Valor do carro financiado: R$ ' || carro * 1.03);
END;
