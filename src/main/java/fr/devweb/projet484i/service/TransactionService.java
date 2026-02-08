package fr.devweb.projet484i.service;

import fr.devweb.projet484i.entity.*;
import fr.devweb.projet484i.repository.*;
import fr.devweb.projet484i.repository.VenteRepository.MoyenneEtQuantiteParNomArticle;
import fr.devweb.projet484i.VariablesGlobales;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.data.domain.PageRequest;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Optional;

@Service
public class TransactionService {

    private final VenteRepository venteRepository;
    private final MarcheRepository marcheRepository;
    private final CooperativeRepository cooperativeRepository;
    private final FermierRepository fermierRepository;


    @Autowired
    public TransactionService(VenteRepository venteRepository, FermierRepository fermierRepository, MarcheRepository marcheRepository, CooperativeRepository cooperativeRepository) {
        this.marcheRepository = marcheRepository;
        this.venteRepository = venteRepository;
        this.fermierRepository = fermierRepository;
        this.cooperativeRepository = cooperativeRepository;
    }

    @Scheduled(cron = "0 0,30 * * * *")// Exécute toutes les 30min
    public void mettreAJourMarche() {
        List<MoyenneEtQuantiteParNomArticle> statsMarche = venteRepository.getMoyenneEtQuantiteParNomArticle();

        for (MoyenneEtQuantiteParNomArticle stat : statsMarche) {
            Marche marche = new Marche();
            marche.setArticles(stat.getArticles());
            marche.setQuantiteRestante(stat.getQuantite());
            marche.setMoyennePonderee(stat.getMoyennePonderee());

            marcheRepository.save(marche);
        }
    }


    // Mettre en vente un article
    @Transactional
    public void mettreEnVente(String vendeurName, String articles, int prixUnitaire, int quantite) {

        // Vérification de la validité de l'article
        validerArticle(articles);

        // Vérification de la validité du prix
        if (prixUnitaire <= 0) {
            throw new IllegalArgumentException("Prix unitaire invalide");
        }

        // Vérification de la validité de la quantité
        if (quantite <= 0) {
            throw new IllegalArgumentException("Quantité invalide");
        }
        // Récupérer l'utilisateur
        Fermier fermier = fermierRepository.findById(vendeurName).orElseThrow(() -> new IllegalArgumentException("Acheteur non trouvé"));

        if (articles.equals(VariablesGlobales.LAPINS_MALES)) {
            if (fermier.getClapier().getNbLapinsMales() < quantite) {
                quantite = fermier.getClapier().getNbLapinsMales();
            }
            fermier.getClapier().suppAdultesMales(quantite);
        }

        if(articles.equals(VariablesGlobales.LAPINS_FEMELLES)) {
            if (fermier.getClapier().getNbLapinsFemelles() < quantite) {
                quantite = fermier.getClapier().getNbLapinsFemelles();
            }
            fermier.getClapier().suppAdultesFemelles(quantite);
        }

        if (articles.equals(VariablesGlobales.POULE)) {
            List<Poule> poules = fermier.getPoules();
            int poulesCouv = 0;
            for (Poule poule : poules) {
                    if(poule.isEnCouvaison()) {
                        poulesCouv++;
                    }
                }
            if ((poules.size() - poulesCouv) < quantite) {
                quantite = (poules.size() - poulesCouv);
            }
            // Supprime les premières poules vendues
            for (int i = 0; i < quantite; i++) {
                Poule poule = poules.get(poulesCouv);
                poules.remove(poule);
            }
        }
        
        if (articles.equals(VariablesGlobales.COQ)) {
            List<Coq> coqs = fermier.getCoqs();
            if (coqs.size() < quantite) {
                quantite = coqs.size();
            }
            // Supprime les premières coqs vendues
            for (int i = 0; i < quantite; i++) {
                Coq coq = coqs.get(0); // toujours supprimer le premier, car la liste est raccourcie à chaque itération
                coqs.remove(coq);
            }
        }

        fermierRepository.save(fermier);

        // Créer la nouvelle vente
        Vente vente = new Vente(articles, prixUnitaire, quantite);
        vente.setVendeur(fermier);
        venteRepository.save(vente);
    }
    

    @Transactional
    public void acheterMarche(String acheteurName, String articles, int quantite) {
        // Vérification de la validité de l'article
        validerArticle(articles);

        // Vérification de la validité de la quantité
        if (quantite <= 0) {
            throw new IllegalArgumentException("Quantité invalide");
        }
    
        // Vérification de la validité de l'acheteur
        Fermier acheteur = getAcheteurValide(acheteurName, quantite);

        int prixUnitaireMoyen = getPrixUnitaireMoyen(articles);
        int prixTotal = prixUnitaireMoyen * quantite;
    
        // Vérification du solde de l'acheteur
        verifierSoldeAcheteur(acheteur, prixTotal);
    
        // Récupération des ventes disponibles
        Page<Vente> ventesDisponibles = venteRepository.findByArticlesOrderByPrixUnitaireAsc(
                articles, PageRequest.of(0, 12)
        );
    

        int quantiteRestante = quantite;
        // Traitement des ventes et achats
        for (Vente vente : ventesDisponibles) {
            if (quantiteRestante == 0) break;
            if (vente.getVendeur().getNomUtilisateur().equals(acheteur.getNomUtilisateur())) {
                continue; // Ne pas acheter à soi-même
            }

            int quantiteAchetee = Math.min(quantiteRestante, vente.getQuantite());
            int prixVente = prixUnitaireMoyen * quantiteAchetee;

            // Traitement des ventes
            traiterVente(vente, acheteur, quantiteAchetee, prixVente, articles);
    
            quantiteRestante -= quantiteAchetee;
        }
    
        // Vérification de la quantité restante
        if (quantiteRestante > 0) {
            throw new IllegalArgumentException("Stock insuffisant sur le marché pour satisfaire la demande.");
        }
    
        // Mise à jour de l'acheteur
        acheteur.suppEcus(prixTotal);
        acheteur.setNbAchat(acheteur.getNbAchat() + quantite);
        acheteur.getStatistique().addAchatMarche(quantite);
        fermierRepository.save(acheteur);
    }

    private void validerArticle(String article) {
        List<String> articlesAutorises = Arrays.asList(
                VariablesGlobales.POULE,
                VariablesGlobales.COQ,
                VariablesGlobales.LAPINS_FEMELLES,
                VariablesGlobales.LAPINS_MALES,
                VariablesGlobales.OEUF,
                VariablesGlobales.LAIT,
                VariablesGlobales.SAVON,
                VariablesGlobales.SERINGUE,
                VariablesGlobales.SAC_NOURRITURE,
                VariablesGlobales.EAU,
                VariablesGlobales.PAILLE
        );
        // Vérification de la validité de l'article
        if (!articlesAutorises.contains(article)) {
            throw new IllegalArgumentException("Article non autorisé pour l'achat");
        }
    }
    
    private Fermier getAcheteurValide(String name, int quantite) {
        Fermier acheteur = fermierRepository.findById(name)
                .orElseThrow(() -> new IllegalArgumentException("Acheteur non trouvé"));

        if (acheteur.getNbAchat() >= 12 || acheteur.getNbAchat() + quantite > 12) {
            throw new IllegalArgumentException("Limite d'achats quotidienne atteinte ou dépassée.");
        }
        return acheteur;
    }
    
    private int getPrixUnitaireMoyen(String article) {
        int prix = marcheRepository.getMoyennePondereeParArticle(article);
        if (prix == 0) {
            throw new IllegalArgumentException("Aucun article disponible à la vente.");
        }
        return prix;
    }
    
    private void verifierSoldeAcheteur(Fermier acheteur, int montant) {
        if (acheteur.getEcus() < montant) {
            throw new IllegalArgumentException("Fonds insuffisants.");
        }
    }
    
    private void traiterVente(Vente vente, Fermier acheteur, int quantiteAchetee, int prixVente, String article) {
        Fermier vendeur = vente.getVendeur();
        ajouterArticlesAAcheteur(acheteur, article, quantiteAchetee);
    
        vente.setQuantite(vente.getQuantite() - quantiteAchetee);
        if (vente.getQuantite() == 0) {
            venteRepository.delete(vente);
        } else {
            venteRepository.save(vente);
        }
        vendeur.addEcus(prixVente);
        vendeur.getStatistique().addVenteMarche(quantiteAchetee);
        fermierRepository.save(vendeur);
    }
    
    
    private void ajouterArticlesAAcheteur(Fermier acheteur, String article, int quantite) {
        for (int i = 0; i < quantite; i++) {
            switch (article) {
                case VariablesGlobales.POULE -> {
                    Poule poule = new Poule(VariablesGlobales.AGE_POULE, VariablesGlobales.POIDS_POULE);
                    poule.setUtilisateur(acheteur);
                    acheteur.getPoules().add(poule);
                }
                case VariablesGlobales.COQ -> {
                    Coq coq = new Coq(VariablesGlobales.AGE_COQ, VariablesGlobales.POIDS_COQ);
                    coq.setUtilisateur(acheteur);
                    acheteur.getCoqs().add(coq); 
                }
                case VariablesGlobales.LAPINS_FEMELLES -> {
                    acheteur.getClapier().addAdultesFemelles(1);
                }
                case VariablesGlobales.LAPINS_MALES -> {
                    acheteur.getClapier().addAdultesMales(1);
                }
                case VariablesGlobales.EAU -> {
                    acheteur.getRemise().incEau(1);
                }
                case VariablesGlobales.SAVON -> {
                    acheteur.getRemise().incSavons(1);
                }
                case VariablesGlobales.SERINGUE -> {
                    acheteur.getRemise().incSeringues(1);
                }
                case VariablesGlobales.SAC_NOURRITURE -> {
                    acheteur.getRemise().incSacsNourriture(1);
                }
                case VariablesGlobales.PAILLE -> {
                    acheteur.getRemise().incBottesPaille(1);
                }


                default ->
                    throw new IllegalArgumentException("Type d'article non reconnu : " + article);
            }
        }
    }

    // Fonctions propres à la coopérative

    @Transactional
    public Cooperative getOrCreateCoop() {
        // Vérifier si la ferme existe déjà
        int nbFermiers = fermierRepository.findAll().size();
        List<Cooperative> listeCoop = cooperativeRepository.findAll();
        if (listeCoop.size() > 0) {
            Cooperative existingCoop = listeCoop.get(0);
            return existingCoop; // Retourner la ferme existante
        }

        // Sinon, créer une nouvelle ferme
        Cooperative coop = new Cooperative(nbFermiers);
        return cooperativeRepository.save(coop);
    }

    @Scheduled(cron = "0 0 22 * * *") // UTC TIME
    public void passageJourCoop() {
        List<Fermier> fermiers = fermierRepository.findAll();
        int nbFermiers = fermiers.size();
        Cooperative coop = getOrCreateCoop();
        cooperativeRepository.save(coop);
    }

    @Transactional
    public void vendreCoop(String vendeurName, String articles, int quantite) {

        // Vérification de la validité de l'article
        validerArticle(articles);

        // Vérification de la validité de la quantité
        if (quantite <= 0) {
            throw new IllegalArgumentException("Quantité invalide");
        }
        // Récupérer l'utilisateur
        Fermier fermier = fermierRepository.findById(vendeurName).orElseThrow(() -> new IllegalArgumentException("Vendeur non trouvé"));

        int prix = 0;

        if (articles.equals(VariablesGlobales.LAPINS_MALES)) {
            if(fermier.getRemise().getLapinsMales() < quantite) {
                quantite = fermier.getRemise().getLapinsMales();
            }
            prix = getPrixCoop(articles) * quantite;
            fermier.getClapier().suppAdultesMales(quantite);
            fermier.addEcus(prix);
            fermier.getStatistique().addLapinsVenduCoop(quantite);
        }

        if(articles.equals(VariablesGlobales.LAPINS_FEMELLES)) {
            if(fermier.getRemise().getLapinsFemelles() < quantite) {
                quantite = fermier.getRemise().getLapinsFemelles();
            }
            prix = getPrixCoop(articles) * quantite;
            fermier.getClapier().suppAdultesFemelles(quantite);
            fermier.addEcus(prix);
            fermier.getStatistique().addLapinsVenduCoop(quantite);
        }

        if (articles.equals(VariablesGlobales.OEUF)) {
            if(fermier.getRemise().getOeuf() < quantite) {
                quantite = fermier.getRemise().getOeuf();
            }
            prix = getPrixCoop(articles) * quantite;
            fermier.getRemise().decOeufs(quantite);
            fermier.addEcus(prix);
            fermier.getStatistique().addOeufsVendu(quantite);
        }
        
        if (articles.equals(VariablesGlobales.LAIT)) {
            if(fermier.getRemise().getLitresLait() < quantite) {
                quantite = fermier.getRemise().getLitresLait();
            }
            prix = getPrixCoop(articles) * quantite;
            fermier.getRemise().decLitresLait(quantite);
            fermier.addEcus(prix);
            fermier.getStatistique().addLaitVendu(quantite);
        }

        fermierRepository.save(fermier);

        // Créer la nouvelle vente
        Vente vente = new Vente(articles, prix, quantite);
        vente.setVendeur(fermier);
        venteRepository.save(vente);
    }

    @Transactional
    public void acheterCoop(String acheteurName, String articles, int quantite) {
        // Vérification de la validité de l'article
        validerArticle(articles);

        // Vérification de la validité de la quantité
        if (quantite <= 0) {
            throw new IllegalArgumentException("Quantité invalide");
        }
    
        // Vérification de la validité de l'acheteur
        Fermier acheteur = getAcheteurValide(acheteurName, quantite);

        int prix = getPrixCoop(articles) * quantite;
    
        // Vérification du solde de l'acheteur
        verifierSoldeAcheteur(acheteur, prix);
    
        // On ne peut pas acheter plus qu'il n'y a dans la coop
        if(quantite > getQttCoop(articles)) {
            quantite = getQttCoop(articles);
            prix = getPrixCoop(articles) * quantite;
        }
    
        // Mise à jour de l'acheteur
        ajouterArticlesAAcheteur(acheteur, articles, quantite);
        acheteur.suppEcus(prix);
        acheteur.setNbAchat(acheteur.getNbAchat() + quantite);
        fermierRepository.save(acheteur);

        suppArticlesCoop(articles, quantite);
    }
    
    @Transactional
    public int getPrixCoop(String article) {
        switch (article) {
            case VariablesGlobales.POULE -> {
                return VariablesGlobales.PRIX_COOP_POULE;
            }
            case VariablesGlobales.COQ -> {
                return VariablesGlobales.PRIX_COOP_COQ;
            }
            case VariablesGlobales.LAPINS_FEMELLES -> {
                return VariablesGlobales.PRIX_COOP_LAPIN_FEMELLE;
            }
            case VariablesGlobales.LAPINS_MALES -> {
                return VariablesGlobales.PRIX_COOP_LAPIN_MALE;
            }
            case VariablesGlobales.EAU -> {
                return VariablesGlobales.PRIX_COOP_EAU;
            }
            case VariablesGlobales.LAIT -> {
                return VariablesGlobales.PRIX_COOP_LAIT;
            }
            case VariablesGlobales.OEUF -> {
                return VariablesGlobales.PRIX_COOP_OEUF;
            }
            case VariablesGlobales.SAVON -> {
                return VariablesGlobales.PRIX_COOP_SAVON;
            }
            case VariablesGlobales.SERINGUE -> {
                return VariablesGlobales.PRIX_COOP_SERINGUE;
            }
            case VariablesGlobales.SAC_NOURRITURE -> {
                return VariablesGlobales.PRIX_COOP_SAC_NOURRITURE;
            }
            case VariablesGlobales.PAILLE -> {
                return VariablesGlobales.PRIX_COOP_PAILLE;
            }
            default -> {
                return 0;
            }
        }
    }

    @Transactional
    public int getQttCoop(String article) {
        Cooperative coop = cooperativeRepository.findAll().get(0);
        switch (article) {
            case VariablesGlobales.POULE -> {
                return coop.getQttPoule();
            }
            case VariablesGlobales.COQ -> {
                return coop.getQttCoq();
            }
            case VariablesGlobales.LAPINS_FEMELLES -> {
                return coop.getQttLapinFemelle();
            }
            case VariablesGlobales.LAPINS_MALES -> {
                return coop.getQttLapinMale();
            }
            case VariablesGlobales.EAU -> {
                return coop.getQttEau();
            }
            case VariablesGlobales.SAVON -> {
                return coop.getQttSavon();
            }
            case VariablesGlobales.SERINGUE -> {
                return coop.getQttSeringue();
            }
            case VariablesGlobales.SAC_NOURRITURE -> {
                return coop.getQttSacNourriture();
            }
            case VariablesGlobales.PAILLE -> {
                return coop.getQttPaille();
            }
            default -> {
                return 0;
            }
        }
    }

    @Transactional
    public void suppArticlesCoop(String article, int quantite) {
        Cooperative coop = cooperativeRepository.findAll().get(0);
        switch (article) {
            case VariablesGlobales.POULE -> {
                coop.setQttPoule(coop.getQttPoule() - quantite);
            }
            case VariablesGlobales.COQ -> {
                coop.setQttCoq(coop.getQttCoq() - quantite);
            }
            case VariablesGlobales.LAPINS_FEMELLES -> {
                coop.setQttLapinFemelle(coop.getQttLapinFemelle() - quantite);
            }
            case VariablesGlobales.LAPINS_MALES -> {
                coop.setQttLapinMale(coop.getQttLapinMale() - quantite);
            }
            case VariablesGlobales.EAU -> {
                coop.setQttEau(coop.getQttEau() - quantite);
            }
            case VariablesGlobales.SAVON -> {
                coop.setQttSavon(coop.getQttSavon() - quantite);
            }
            case VariablesGlobales.SERINGUE -> {
                coop.setQttSeringue(coop.getQttSeringue() - quantite);
            }
            case VariablesGlobales.SAC_NOURRITURE -> {
                coop.setQttSacNourriture(coop.getQttSacNourriture() - quantite);
            }
            case VariablesGlobales.PAILLE -> {
                coop.setQttPaille(coop.getQttPaille() - quantite);
            }
            default -> {
                System.out.print("article pas valide");
            }
        }
        cooperativeRepository.save(coop);
    }

    @Transactional
    public void remplirCoop(String utilisateurName) {
        Cooperative coop = cooperativeRepository.findAll().get(0);
        coop.resetQttArticles(5);
        cooperativeRepository.save(coop);
    }

    @Transactional
    public void viderCoop(String utilisateurName) {
        Cooperative coop = cooperativeRepository.findAll().get(0);
        coop.viderCoop();
        cooperativeRepository.save(coop);
    }

    @Scheduled(cron = "0 0 3,15,20 * * *") // UTC TIME
    @Transactional
    public void ouvrirCoop() {
        Cooperative coop = cooperativeRepository.findAll().get(0);
        coop.ouvrirCoop();
        cooperativeRepository.save(coop);
    }

    @Scheduled(cron = "0 0 1,12,18 * * *") // UTC TIME
    @Transactional
    public void fermerCoop() {
        Cooperative coop = cooperativeRepository.findAll().get(0);
        coop.fermerCoop();
        cooperativeRepository.save(coop);
    }
}