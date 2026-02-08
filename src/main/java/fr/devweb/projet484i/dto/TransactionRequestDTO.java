package fr.devweb.projet484i.dto;

import fr.devweb.projet484i.entity.Vente;
import fr.devweb.projet484i.entity.Fermier;
import lombok.Data;

@Data
public class TransactionRequestDTO {
    private Long id;
    private String articles;
    private int prixUnitaire; // pas utilisé pour l'achat
    private int quantite;
    private String nomUtilisateur;

    public TransactionRequestDTO() {
        // constructeur vide pour Jackson
    }

    public TransactionRequestDTO(Vente vente) {
        this.id = vente.getId();
        this.articles = vente.getArticles();
        this.prixUnitaire = vente.getPrixUnitaire();
        this.quantite = vente.getQuantite();
        this.nomUtilisateur = vente.getVendeur().getNomUtilisateur(); // On récupère le nomUtilisateur du vendeur
    }
}