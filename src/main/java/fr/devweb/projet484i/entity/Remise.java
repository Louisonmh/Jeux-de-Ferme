package fr.devweb.projet484i.entity;

import com.fasterxml.jackson.annotation.JsonBackReference;

import fr.devweb.projet484i.VariablesGlobales;
import jakarta.persistence.*;

import lombok.Data;

@Entity
@Table(name = "remises")
@Data
public class Remise {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @OneToOne
    @JoinColumn(name = "nomUtilisateur", nullable = false)
    @JsonBackReference
    private Fermier utilisateur;

    private int eau;
    private int bottes_de_paille;
    private int seringue;
    private int savon;
    private int sac_nourriture;
    private int lapinsMales;
    private int lapinsFemelles;
    private int oeuf;
    private int litresLait;

    public Remise() {
        eau = 0;
        bottes_de_paille = 0;
        seringue = 0;
        savon = 0;
        sac_nourriture = 0;
        lapinsMales = 0;
        lapinsFemelles = 0;
        oeuf = 0;
        litresLait = 0;
    }

    public void vider() {
        eau = 0;
        bottes_de_paille = 0;
        seringue = 0;
        savon = 0;
        sac_nourriture = 0;
        lapinsMales = 0;
        lapinsFemelles = 0;
        oeuf = 0;
        litresLait = 0;
    }

    public void remplirUn() {
        eau = 1;
        bottes_de_paille = 1;
        seringue = 1;
        savon = 1;
        sac_nourriture = 1;
        lapinsMales = 1;
        lapinsFemelles = 1;
        oeuf = 1;
        litresLait = 1;
    }

    public void remplirPlusieurs() {
        eau = 5;
        bottes_de_paille = 5;
        seringue = 5;
        savon = 5;
        sac_nourriture = 5;
        lapinsMales = 5;
        lapinsFemelles = 5;
        oeuf = 5;
        litresLait = 5;
    }

    public void incEau(int n) {
        eau += n;
    }

    public void decEau() {
        eau -= 1;
        eau = Math.max(eau, 0);
    }

    public void incBottesPaille(int n) {
        bottes_de_paille += n;
    }

    public void decBottesPaille() {
        bottes_de_paille -= 1;
        bottes_de_paille = Math.max(bottes_de_paille, 0);
    }

    public void incSeringues(int n) {
        seringue += n;
    }

    public void decSeringues() {
        seringue -= 1;
        seringue = Math.max(seringue, 0);
    }

    public void incSavons(int n) {
        savon += n;
    }

    public void decSavons() {
        savon -= 1;
        savon = Math.max(savon, 0);
    }

    public void incSacsNourriture(int n) {
        sac_nourriture += n;
    }

    public void decSacsNourriture() {
        sac_nourriture -= 1;
        sac_nourriture = Math.max(sac_nourriture, 0);
    }

    public void incOeufs(int n) {
        oeuf += n;
        utilisateur.getStatistique().addOeufsVendu(n);
        VariablesGlobales.addOeufsVendu(n);
    }

    public void decOeufs(int n) {
        oeuf -= n;
        oeuf = Math.max(oeuf, 0);
    }

    public void incLitresLait(int n) {
        litresLait += n;
    }

    public void decLitresLait(int n) {
        litresLait -= n;
        litresLait = Math.max(litresLait, 0);
    }
}