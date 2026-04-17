package br.com.fiap.projetos.service;

import br.com.fiap.projetos.dto.RecursoDTO;
import br.com.fiap.projetos.entity.Recurso;
import br.com.fiap.projetos.repository.RecursoRepository;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.UUID;
import java.util.stream.Collectors;

@Service
@AllArgsConstructor
public class RecursoService {
    private final RecursoRepository recursoRepository;

    private static RecursoDTO toDTO(Recurso recurso) {
        return RecursoDTO.builder()
                .id(recurso.getId())
                .nome(recurso.getNome())
                .custoMensal(recurso.getCustoMensal())
                .identificacaoLegal(recurso.getIdentificacaoLegal())
                .build();
    }

    private static Recurso toEntity(RecursoDTO recursoDTO) {
        Recurso recurso = new Recurso();
        recurso.setId(recursoDTO.getId());
        recurso.setNome(recursoDTO.getNome());
        recurso.setCustoMensal(recursoDTO.getCustoMensal());
        recurso.setIdentificacaoLegal(recursoDTO.getIdentificacaoLegal());
        return recurso;
    }

    public List<RecursoDTO> findAll() {
        return recursoRepository.findAll().stream()
                .map(RecursoService::toDTO)
                .collect(Collectors.toList());
    }

    public RecursoDTO findById(UUID uuid){
        Optional<Recurso> recurso = recursoRepository.findById(uuid);
        if (recurso.isPresent()) {
            return toDTO(recurso.get());
        }
        return null;
    }

    public Recurso save(RecursoDTO recursoDTO) {
        return recursoRepository.save(toEntity(recursoDTO));
    }

    public Recurso findByIdentificacaoLegal(String identificaoLegal) {
        return recursoRepository.findByIdentificacaoLegal(identificaoLegal);
    }

    public void apagar(UUID uuid) {
        recursoRepository.deleteById(uuid);
    }

    public RecursoDTO atualizar(RecursoDTO recursoDTO) {
        Recurso recursoSalvo = recursoRepository.save(toEntity(recursoDTO));
        return toDTO(recursoSalvo);
    }
}
