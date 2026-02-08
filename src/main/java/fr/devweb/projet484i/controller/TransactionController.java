package fr.devweb.projet484i.controller;

import fr.devweb.projet484i.entity.*;
import fr.devweb.projet484i.repository.*;
import fr.devweb.projet484i.service.TransactionService;
import fr.devweb.projet484i.dto.TransactionRequestDTO;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.RequestBody;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.http.HttpStatus;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.List;
import java.util.stream.Collectors;
import java.util.Map;
import java.util.HashMap;

@RestController
@RequestMapping("/transactions")
public class TransactionController {

    private final TransactionService transactionService;
    private final VenteRepository venteRepository;
    private final MarcheRepository marcheRepository;
    private final CooperativeRepository cooperativeRepository;
    private static final Logger log = LoggerFactory.getLogger(TransactionController.class);

    @Autowired
    public TransactionController(TransactionService transactionService, VenteRepository venteRepository, MarcheRepository marcheRepository, CooperativeRepository cooperativeRepository) {
        this.marcheRepository = marcheRepository;
        this.venteRepository = venteRepository;
        this.transactionService = transactionService;
        this.cooperativeRepository = cooperativeRepository;
    }

    @GetMapping("/ventes")
    public Page<TransactionRequestDTO> getVentes(Pageable pageable) {
        return venteRepository.findAll(pageable)
            .map(TransactionRequestDTO::new);
    }

    @GetMapping("/marche")
    public List<Marche> getMarcheStats() {
        return marcheRepository.findAll();
    }
    
    
    // Mettre en vente un article sur le marché
    @PostMapping("/marche/miseEnVente")
    public ResponseEntity<Map<String, String>> mettreEnVenteAuMarche(@RequestBody TransactionRequestDTO requestDTO,
                                                Authentication authentication) {
        log.info(" Tentative de traitement de la transaction...");
        try {
            String vendeurName = authentication.getName();
            log.info(" Reçu demande de mise en vente");
            log.info("Vendeur: {}, Article: {}, Prix: {}, Quantité: {}", vendeurName, requestDTO.getArticles(), requestDTO.getPrixUnitaire(), requestDTO.getQuantite());
            transactionService.mettreEnVente(vendeurName,  requestDTO.getArticles(), requestDTO.getPrixUnitaire(), requestDTO.getQuantite());

            // Réponse avec JSON valide
            Map<String, String> response = new HashMap<>();
            response.put("message", "Vente réussie. Super");
            return ResponseEntity.ok(response);
        } catch (Exception e) {
            log.error(" Erreur lors de la mise en vente: {}", e.getMessage(), e);
            // Si une erreur survient, renvoie un Map avec l'erreur
            Map<String, String> errorResponse = new HashMap<>();
            errorResponse.put("error", "Une erreur est survenue.");
            return ResponseEntity.badRequest().body(errorResponse); 
        }
    }

    // Acheter des articles sur le marché
    @PostMapping("/marche/acheter")
    public ResponseEntity<Map<String, String>> acheterAuMarche(@RequestBody TransactionRequestDTO requestDTO,
                                                Authentication authentication) {
        log.info(" Tentative de traitement de la transaction...");
        try {
            String acheteurName = authentication.getName();
            log.info(" Reçu demande d'achat");
            log.info("Acheteur: {}, Articles: {}, Quantité: {}", acheteurName, requestDTO.getArticles(), requestDTO.getQuantite());
            transactionService.acheterMarche(acheteurName, requestDTO.getArticles(), requestDTO.getQuantite());

            // Réponse avec JSON valide
            Map<String, String> response = new HashMap<>();
            response.put("message", "Achat réussie. Super");
            return ResponseEntity.ok(response);
        } catch (Exception e) {
            log.error(" Erreur lors de l'achat: {}", e.getMessage(), e);
            // Si une erreur survient, renvoie un Map avec l'erreur
            Map<String, String> errorResponse = new HashMap<>();
            errorResponse.put("error", "Une erreur est survenue.");
            return ResponseEntity.badRequest().body(errorResponse); 
        }
    }

    @GetMapping("/cooperative")
    public Cooperative getCoop() {
        return transactionService.getOrCreateCoop();
    }

    // Vendre des articles à la coopérative
    @PostMapping("/cooperative/vendre")
    public ResponseEntity<String> vendreCoop(@RequestBody TransactionRequestDTO requestDTO, Authentication authentication) {
        log.info(" Tentative de traitement de la transaction...");
        try {
            String vendeurName = authentication.getName();
            log.info(" Reçu demande de mise en vente");
            log.info("Vendeur: {}, Article: {}, Quantité: {}", vendeurName, requestDTO.getArticles(), requestDTO.getQuantite());
            transactionService.vendreCoop(vendeurName, requestDTO.getArticles(), requestDTO.getQuantite());
            return ResponseEntity.ok("Vente réussie. Super");
        } catch (Exception e) {
            log.error(" Erreur lors de la vente: {}", e.getMessage(), e);
            return ResponseEntity.badRequest().body(null);
        }
    }

    // Acheter des articles à la coopérative
    @PostMapping("/cooperative/acheter")
    public ResponseEntity<String> acheterCoop(@RequestBody TransactionRequestDTO requestDTO, Authentication authentication) {
        log.info(" Tentative de traitement de la transaction...");
        try {
            String acheteurName = authentication.getName();
            log.info(" Reçu demande d'achat");
            log.info("Acheteur: {}, Articles: {}, Quantité: {}", acheteurName, requestDTO.getArticles(), requestDTO.getQuantite());
            transactionService.acheterCoop(acheteurName, requestDTO.getArticles(), requestDTO.getQuantite());
            return ResponseEntity.ok("Achat effectué avec succès.");
        } catch (Exception e) {
            log.error(" Erreur lors de l'achat: {}", e.getMessage(), e);
            return ResponseEntity.badRequest().body(e.getMessage());
        }
    }

    // S'assurer que la coopérative a du stock
    @PostMapping("/cooperative/remplir")
    public void remplirCoop(Authentication authentication) {
        transactionService.remplirCoop(authentication.getName());
    }

    // S'assurer que la coopérative a du stock
    @PostMapping("/cooperative/remplirForce")
    public void remplirFCoop() {
        transactionService.passageJourCoop();
    }

    // S'assurer que la coopérative n'a aucun stock
    @PostMapping("/cooperative/vider")
    public void viderCoop(Authentication authentication) {
        transactionService.viderCoop(authentication.getName());
    }
    
}
