package br.com.fiap.projetos.controller;

import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.http.HttpStatus;

@ControllerAdvice
public class GlobalExceptionHandler {

    /**
     * Trata exceções de recurso não encontrado, como quando um projeto ou recurso não existe.
     */
    @ExceptionHandler({org.springframework.dao.EmptyResultDataAccessException.class, java.util.NoSuchElementException.class})
    @ResponseStatus(HttpStatus.NOT_FOUND)
    public String handleResourceNotFound(Exception ex, Model model) {
        model.addAttribute("mensagem", "Recurso não encontrado.");
        return "error";
    }

    /**
     * Trata erros de validação de formulários, exibindo mensagens amigáveis ao usuário.
     */
    @ExceptionHandler(org.springframework.web.bind.MethodArgumentNotValidException.class)
    @ResponseStatus(HttpStatus.BAD_REQUEST)
    public String handleValidationException(org.springframework.web.bind.MethodArgumentNotValidException ex, Model model) {
        StringBuilder mensagem = new StringBuilder("Erro de validação: ");
        ex.getBindingResult().getFieldErrors().forEach(error -> {
            mensagem.append(error.getField()).append(" - ").append(error.getDefaultMessage()).append("; ");
        });
        model.addAttribute("mensagem", mensagem.toString());
        return "error";
    }

    /**
     * Trata exceções genéricas e inesperadas, exibindo uma mensagem padrão.
     */
    @ExceptionHandler(Exception.class)
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    public String handleGenericException(Exception ex, Model model) {
        model.addAttribute("mensagem", "Ocorreu um erro inesperado. Tente novamente mais tarde.");
        return "error";
    }
}