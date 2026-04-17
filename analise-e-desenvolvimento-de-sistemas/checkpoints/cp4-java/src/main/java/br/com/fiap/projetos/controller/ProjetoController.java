package br.com.fiap.projetos.controller;

import br.com.fiap.projetos.dto.ProjetoDTO;
import br.com.fiap.projetos.service.ProjetoService;
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

/**
 * Controller responsável pelo fluxo de cadastro, edição, deleção e listagem de projetos.
 */
@Controller
@RequestMapping("/projetos")
@AllArgsConstructor
@Log
public class ProjetoController {

    private final ProjetoService projetoService;

    /**
     * Exibe a lista de projetos.
     */
    @GetMapping
    public String listar(Model model) {
        model.addAttribute("projetos", projetoService.listar());
        return "projetos/lista";
    }

    /**
     * Exibe o formulário para cadastrar um novo projeto.
     */
    @GetMapping("/novo")
    public String novo(Model model) {
        model.addAttribute("projeto", new ProjetoDTO());
        return "projetos/formulario";
    }

    /**
     * Salva um novo projeto ou atualiza um existente.
     * Caso haja erros de validação, retorna para o formulário.
     */
    @PostMapping("/salvar")
    public String salvar(@Valid @ModelAttribute("projeto") ProjetoDTO projeto, BindingResult bindingResult, Model model) {
        if (bindingResult.hasErrors()) {
            // Log de erros de validação
            bindingResult.getAllErrors().forEach(e -> log.info(e.toString()));
            model.addAttribute("projeto", projeto);
            return "projetos/formulario";
        }
        projetoService.criar(projeto);
        return "redirect:/projetos";
    }

    /**
     * Exibe o formulário para editar um projeto existente.
     */
    @GetMapping("/editar/{id}")
    public String editar(@PathVariable Long id, Model model) {
        ProjetoDTO projeto = projetoService.findById(id);
        if (projeto == null) {
            // Lança exceção específica para recurso não encontrado, tratada pelo GlobalExceptionHandler
            throw new java.util.NoSuchElementException("Projeto não encontrado");
        }
        model.addAttribute("projeto", projeto);
        return "projetos/formulario";
    }

    /**
     * Remove um projeto pelo id e redireciona para a listagem.
     */
    @GetMapping("/deletar/{id}")
    public String deletar(@PathVariable Long id) {
        projetoService.apagar(id);
        return "redirect:/projetos";
    }
}