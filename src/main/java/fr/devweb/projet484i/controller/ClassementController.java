package fr.devweb.projet484i.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import fr.devweb.projet484i.service.ClassementService;
import fr.devweb.projet484i.service.FermierService;
import fr.devweb.projet484i.entity.Fermier;

import java.util.List;
import java.net.Authenticator;
import java.util.ArrayList;
import java.util.Optional;
import org.springframework.security.core.Authentication;
import fr.devweb.projet484i.VariablesGlobales;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@RestController
@RequestMapping("/classement")
public class ClassementController {

    private final ClassementService classementService;
    private final FermierService fermierService;

    public ClassementController(ClassementService classementService, FermierService fermierService){
        this.classementService = classementService;
        this.fermierService = fermierService;
    }

    @GetMapping("/triEcus")
    public List<Fermier> triParEcus(){
        return classementService.triParEcus();
    }

    @GetMapping("/triProd")
    public List<Fermier> triParProd(){
        return classementService.triParProd();
    }
    
    @GetMapping("/triNego")
    public List<Fermier> triParNego(){
        return classementService.triParNego();
    }
    
    @GetMapping("/triGlobal")
    public List<Fermier> triParGlobal(){
        return classementService.triParGlobal();
    }

    @PostMapping("/addVenteMarche/{n}")
    public void addVenteMarche(Authentication authentication, @PathVariable("n") int n){
        classementService.addVenteMarche(authentication.getName(), n);
    }
}