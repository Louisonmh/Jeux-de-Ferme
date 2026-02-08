package fr.devweb.projet484i.entity;

import com.fasterxml.jackson.annotation.JsonBackReference;
import jakarta.persistence.*;
import lombok.Data;

import fr.devweb.projet484i.VariablesGlobales;

@Entity
@Table(name = "statistique")
@Data
public class Statistique {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @OneToOne
    @JoinColumn(name = "nomUtilisateur", nullable = false)
    @JsonBackReference
    private Fermier utilisateur;

    int oeufsVendu;
    int lapinsVenduCoop;
    int laitVendu;
    int achatMarche;
    int venteMarche;
    int solde;

    int pointEcus;
    int pointProd;
    int pointNego;
    int pointGlobal;

    public Statistique(){
        oeufsVendu = 0;
        lapinsVenduCoop = 0;
        laitVendu = 0;
        achatMarche = 0;
        venteMarche = 0;
        solde = 0;

        pointEcus = 0;
        pointProd = 0;
        pointNego = 0;
        pointGlobal = 0;
    }

    public void addOeufsVendu(int n){
        this.oeufsVendu += n;
        VariablesGlobales.addOeufsVendu(n);
    }

    public void addLapinsVenduCoop(int n){
        this.lapinsVenduCoop += n;
        VariablesGlobales.addLapinsVenduCoop(n);
    }

    public void addLaitVendu(int n){
        this.laitVendu += n;
        VariablesGlobales.addLaitVendu(n);
    }
    public void addAchatMarche(int n){
        this.achatMarche += n;
        VariablesGlobales.addAchatMarche(n);
    }

    public void addVenteMarche(int n){
        this.venteMarche += n;
        VariablesGlobales.addVenteMarche(n);
    }

    public void setSolde(){
        this.solde = utilisateur.getEcus();
    }

    public void setPointGlobal(){
        this.pointGlobal = this.pointEcus + this.pointNego + this.pointProd;
    }
}