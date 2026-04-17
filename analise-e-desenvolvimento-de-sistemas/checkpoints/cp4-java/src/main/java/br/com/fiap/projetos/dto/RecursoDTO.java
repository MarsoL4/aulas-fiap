package br.com.fiap.projetos.dto;

import jakarta.validation.constraints.Min;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.math.BigDecimal;
import java.util.UUID;

@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class RecursoDTO {

    private UUID id;

    @NotBlank
    private String nome;

    @NotNull
    private String identificacaoLegal;
    
    @Min(0)
    @NotNull
    private BigDecimal custoMensal;

}
