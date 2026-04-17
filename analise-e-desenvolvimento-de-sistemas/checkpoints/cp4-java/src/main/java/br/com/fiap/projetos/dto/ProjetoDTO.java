package br.com.fiap.projetos.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.Instant;

import jakarta.validation.constraints.NotBlank;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class ProjetoDTO {
    private Long id;

    @NotBlank
    private String nome;

    @NotBlank
    private String responsavel;

    private Instant dataCriacao;
}