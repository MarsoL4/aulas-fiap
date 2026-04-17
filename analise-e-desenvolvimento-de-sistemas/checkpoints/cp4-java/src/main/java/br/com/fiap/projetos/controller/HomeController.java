package br.com.fiap.projetos.controller;

import lombok.AllArgsConstructor;
import lombok.extern.java.Log;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/")
@AllArgsConstructor
@Log
public class HomeController {

    /**
     * Exibe a página inicial do sistema.
     */
    @GetMapping
    public String home(Model model){
        return "home";
    }

}
