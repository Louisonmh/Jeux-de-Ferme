package fr.devweb.projet484i.entity;
import fr.devweb.projet484i.VariablesGlobales;
import fr.devweb.projet484i.entity.Fermier;

import com.fasterxml.jackson.annotation.JsonBackReference;
import jakarta.persistence.*;

import lombok.Data;

import java.sql.Timestamp;
import java.time.LocalDate;


@Entity
@Table(name = "ventes")
@Data
public class Vente {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne
    @JoinColumn(name = "vendeur_id", nullable = false)
    @JsonBackReference
    private Fermier vendeur;

    @Column(name = "articles", nullable = false)
    private String articles;

    @Column(name = "date_vente", nullable = false)
    private Timestamp dateVente;

    @Column(name = "montant", nullable = false)
    private int prixUnitaire;

    @Column(name = "quantite", nullable = false)
    private int quantite;

    public Vente() {
        //construteur par défaut
    }
    
    public Vente(String articles, int prixUnitaire, int quantite) {
        this.dateVente = Timestamp.valueOf(LocalDate.now().atStartOfDay());
        this.articles = articles;
        this.prixUnitaire = prixUnitaire;
        this.quantite = quantite;
    }
}