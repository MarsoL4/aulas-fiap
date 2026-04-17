package br.com.fiap.projetos.entity;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Data;

import java.math.BigDecimal;
import java.util.UUID;

@Entity
@Table(name = "tb_recurso")
@Data
public class Recurso {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    private UUID id;

    @Column(name="nome_recurso")
    private String nome;

    @Column(name="identificao_legal", unique = true)
    private String identificacaoLegal;

    @Column(name = "custo_mensal", precision = 10, scale = 2)
    private BigDecimal custoMensal;

}
