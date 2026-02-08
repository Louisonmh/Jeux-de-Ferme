package fr.devweb.projet484i.entity;

import jakarta.persistence.*;

import lombok.Data;

/**
 * Classe représentant un marché.
 * Un marché est associé à un article et contient la moyenne pondérée de cet article.
 */
@Entity
@Table(name = "marches")
@Data
public class Marche {
    @Id
    private String articles;
    private int quantiteRestante;
    private int moyennePonderee;

    public Marche() {
        // Constructeur par défaut
    }
}