package br.com.fiap.projetos.controller;

import br.com.fiap.projetos.dto.RecursoDTO;
import br.com.fiap.projetos.service.RecursoService;
import jakarta.validation.Valid;
import lombok.AllArgsConstructor;
import lombok.extern.java.Log;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import java.util.UUID;

@Controller
@RequestMapping("/recursos")
@AllArgsConstructor
@Log
public class RecursoController {

    // Serviço responsável pela lógica de negócio dos recursos
    private final RecursoService recursoService;

    /**
     * Exibe a lista de recursos cadastrados.
     */
    @GetMapping
    public String listar(Model model) {
        model.addAttribute("recursos", recursoService.findAll());
        return "recursos/lista";
    }

    /**
     * Exibe o formulário para cadastrar um novo recurso.
     */
    @GetMapping("/novo")
    public String novo(Model model) {
        model.addAttribute("recurso", new RecursoDTO());
        return "recursos/formulario";
    }

    /**
     * Salva um novo recurso ou atualiza um existente.
     * Caso haja erros de validação, retorna para o formulário.
     */
    @PostMapping("/salvar")
    public String salvar(@Valid @ModelAttribute("produto") RecursoDTO recurso, BindingResult bindingResults, Model model){
        if (bindingResults.hasErrors()) {
            // Loga os erros de validação para análise
            bindingResults.getAllErrors().forEach(e-> log.info(e.toString()));
            model.addAttribute("recurso", recurso);
            return "recursos/formulario";
        }
        recursoService.save(recurso);
        return "redirect:/recursos";
    }

    /**
     * Exibe o formulário para editar um recurso existente.
     */
    @GetMapping("/editar/{uuid}")
    public String editar(@PathVariable UUID uuid, Model model) {
        model.addAttribute("recurso", recursoService.findById(uuid));
        return "recursos/formulario";
    }

    /**
     * Remove um recurso pelo UUID e redireciona para a listagem.
     */
    @GetMapping("/deletar/{uuid}")
    public String deletar(@PathVariable UUID uuid){
        recursoService.apagar(uuid);
        return "redirect:/recursos";
    }


}
