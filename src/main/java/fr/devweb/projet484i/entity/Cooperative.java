package fr.devweb.projet484i.entity;

import jakarta.persistence.*;

import lombok.Data;

@Entity
@Table(name = "cooperative")
@Data
public class Cooperative {
    @Id
    private String nom;

    private int qttLapinMale;
    private int qttLapinFemelle;
    private int qttPoule;
    private int qttCoq;
    private int qttSavon;
    private int qttEau;
    private int qttSacNourriture;
    private int qttPaille;
    private int qttSeringue;

    private boolean ouverte;

    public Cooperative(int n) {
        nom = "coop_";
        ouverte = true;
        resetQttArticles(n);
    }

    public Cooperative() {
    }

    public void resetQttArticles(int n) {
        qttLapinMale = n;
        qttLapinFemelle = n;
        qttPoule = n;
        qttCoq = n;
        qttSavon = n;
        qttEau = n;
        qttSacNourriture = n;
        qttPaille = n;
        qttSeringue = n;
    }

    public void viderCoop() {
        qttLapinMale = 0;
        qttLapinFemelle = 0;
        qttPoule = 0;
        qttCoq = 0;
        qttSavon = 0;
        qttEau = 0;
        qttSacNourriture = 0;
        qttPaille = 0;
        qttSeringue = 0;
    }

    public void ouvrirCoop() {
        ouverte = true;
    }

    public void fermerCoop() {
        ouverte = false;
    }
}