package fr.devweb.projet484i.entity;

import com.fasterxml.jackson.annotation.JsonManagedReference;
import jakarta.persistence.*;
import lombok.Data;

import fr.devweb.projet484i.VariablesGlobales;

import java.sql.Timestamp;
import java.util.ArrayList;
import java.util.List;


@Entity
@Table(name = "fermiers")
@Data
public class Fermier {

    @Id
    private String nomUtilisateur; //ID = nom de l'utilisateur loggé

    @OneToOne(mappedBy = "utilisateur", cascade = CascadeType.ALL, orphanRemoval = true)
    @JsonManagedReference
    private Remise remise;

    @OneToOne(mappedBy = "utilisateur", cascade = CascadeType.ALL, orphanRemoval = true)
    @JsonManagedReference
    private Statistique statistique;

    @OneToMany(mappedBy = "utilisateur", cascade = CascadeType.ALL, orphanRemoval = true)
    @JsonManagedReference
    private List<Coq> coqs = new ArrayList<>();

    @OneToMany(mappedBy = "utilisateur", cascade = CascadeType.ALL, orphanRemoval = true)
    @JsonManagedReference
    private List<Poule> poules = new ArrayList<>();

    @OneToMany(mappedBy = "utilisateur", cascade = CascadeType.ALL, orphanRemoval = true)
    @JsonManagedReference
    private List<Poussin> poussins = new ArrayList<>();

    @OneToOne(mappedBy = "utilisateur", cascade = CascadeType.ALL, orphanRemoval = true)
    @JsonManagedReference
    private Clapier clapier;

    @OneToOne(mappedBy = "utilisateur", cascade = CascadeType.ALL, orphanRemoval = true)
    @JsonManagedReference
    private Vache vache;

    @OneToMany(mappedBy = "vendeur", cascade = CascadeType.ALL, orphanRemoval = true)
    @JsonManagedReference
    private List<Vente> ventes = new ArrayList<>(); // Liste des articles mise en vente au marché

    private boolean enHibernation;
    private int ecus;

    @Column(name = "nb_achat", nullable = false, columnDefinition = "int default 0")
    private int nbAchat;
    
    private int empruntRembourse;

    public Fermier() {}

    public Fermier(String nomUtilisateur) {
        this.nomUtilisateur = nomUtilisateur;
        this.ecus = VariablesGlobales.ECUS;
        this.empruntRembourse = 0;
        this.nbAchat = 0;
        enHibernation = false;
    }

    public void addEcus(int ecus){
        this.ecus += ecus;
        this.getStatistique().setSolde();
        VariablesGlobales.addSolde(ecus);
    }

    public void suppEcus(int ecus){
        this.ecus -= ecus;
        this.getStatistique().setSolde();
        VariablesGlobales.reducSolde(ecus);
    }

    public void zeroEcus(){
        this.ecus = 0;
    }

    public void setVache(Vache vache){
        vache.setUtilisateur(this);
        this.vache = vache;
    }

    public void setClapier(Clapier clapier){
        clapier.setUtilisateur(this);
        this.clapier = clapier;
    }

    public void setRemise(Remise remise) {
        this.remise = remise;
        remise.setUtilisateur(this);
    }

    public void setPoules(List<Poule> poules){
        this.poules = poules;
        for(Poule poule : poules){
            poule.setUtilisateur(this);
        }
    }

    public void addPoule(Poule poule){
        this.poules.add(poule);
        poule.setUtilisateur(this);
    }

    public void setCoqs(List<Coq> coqs){
        this.coqs = coqs;
        for(Coq coq : coqs){
            coq.setUtilisateur(this);
        }
    }

    public void addCoq(Coq coq){
        this.coqs.add(coq);
        coq.setUtilisateur(this);
    }

    public void setPoussins(List<Poussin> poussins){
        this.poussins = poussins;
        for(Poussin poussin : poussins){
            poussin.setUtilisateur(this);
        }
    }

    public void addPoussin(Poussin poussin){
        this.poussins.add(poussin);
        poussin.setUtilisateur(this);
    }

    public void setStatistique(Statistique statistique){
        this.statistique = statistique;
        statistique.setUtilisateur(this);
    }

    public void rembourserEmprunt(int montant){
        if (montant > ecus) {
            throw new IllegalArgumentException("Pas assez d'écus");
        }
        if (montant <= 0) {
            throw new IllegalArgumentException("Montant doit être positif");
        }
        if (this.empruntRembourse + montant > VariablesGlobales.MONTANT_EMPRUNT){
            montant = VariablesGlobales.MONTANT_EMPRUNT - this.empruntRembourse;
        }
        suppEcus(montant);
        this.empruntRembourse += montant;
    }

    public void hiberner() {
        enHibernation = true;
    }

    public void sortirHibernation() {
        enHibernation = false;
    }
}
