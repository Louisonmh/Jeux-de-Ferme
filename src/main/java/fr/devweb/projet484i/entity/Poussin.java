package fr.devweb.projet484i.entity;

import fr.devweb.projet484i.VariablesGlobales;

import com.fasterxml.jackson.annotation.JsonBackReference;

import jakarta.persistence.*;
import lombok.Data;

import java.sql.Timestamp;
import java.util.Random;
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
import java.util.List;
import java.lang.Math;

@Entity
@Table(name = "poussins")
@Data
public class Poussin {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne
    @JoinColumn(name = "utilisateur_id", nullable = false)
    @JsonBackReference
    private Fermier utilisateur;

    private int age;
    private float poids;
    private Timestamp nourris;
    private Timestamp abreuve;
    private Timestamp sale;
    private Timestamp malade;

    public Poussin(){}

    public Poussin(int age, float poids){
        this.age = age;
        this.poids = poids;
        nourris = new Timestamp(System.currentTimeMillis() - (86400 * 1000));
        abreuve = new Timestamp(System.currentTimeMillis() - (86400 * 1000));
        sale = null;
        malade = null;
    }

    public void nourrir(){
        Timestamp now = new Timestamp(System.currentTimeMillis());
        if(nourris.getDate() != now.getDate() && (utilisateur.getEcus() - VariablesGlobales.PRIX_NOURRIR_POUSSIN) >= 0){
            nourris = now;
            poids += VariablesGlobales.POIDS_NOURRIE_POUSSIN;
            if(abreuve.getDate() == now.getDate()) {
                poids += VariablesGlobales.POIDS_ABREUVE_POUSSIN;
            }
            poids = Math.min(poids, VariablesGlobales.POIDS_MAX_POUSSIN);
            poids = Math.round(poids * 100.0) / 100.0f;
            utilisateur.suppEcus(VariablesGlobales.PRIX_NOURRIR_POUSSIN);
        }
    }

    public void nourrirSacNourriture(){
        Timestamp now = new Timestamp(System.currentTimeMillis());
        if(nourris.getDate() != now.getDate()){
            nourris = now;
            poids += VariablesGlobales.POIDS_NOURRIE_POUSSIN;
            if(abreuve.getDate() == now.getDate()) {
                poids += VariablesGlobales.POIDS_ABREUVE_POUSSIN;
            }
            poids = Math.round(poids * 100.0) / 100.0f;
            poids = Math.min(poids, VariablesGlobales.POIDS_MAX_POUSSIN);
        }
    }

    public void abreuve(){
        Timestamp now = new Timestamp(System.currentTimeMillis());
        if(abreuve.getDate() != now.getDate() && ((utilisateur.getEcus() - VariablesGlobales.PRIX_ABREUVE_POUSSIN) >= 0)){
            abreuve = now;
            if(nourris.getDate() == now.getDate()) {
                poids += VariablesGlobales.POIDS_ABREUVE_POUSSIN;
            }
            poids = Math.round(poids * 100.0) / 100.0f;
            poids = Math.min(poids, VariablesGlobales.POIDS_MAX_POUSSIN);
            utilisateur.suppEcus(VariablesGlobales.PRIX_ABREUVE_POUSSIN);
        }
    }

    public void abreuveSeauDeau(){
        Timestamp now = new Timestamp(System.currentTimeMillis());
        if(abreuve.getDate() != now.getDate()){
            abreuve = now;
            if(nourris.getDate() == now.getDate()) {
                poids += VariablesGlobales.POIDS_ABREUVE_POUSSIN;
            }
            poids = Math.round(poids * 100.0) / 100.0f;
            poids = Math.min(poids, VariablesGlobales.POIDS_MAX_POUSSIN);
        }
    }

    public void soigner() {
        if(malade != null && ((utilisateur.getEcus() - VariablesGlobales.PRIX_SOIGNER_POUSSIN) >= 0)){
            malade = null;
            utilisateur.suppEcus(VariablesGlobales.PRIX_SOIGNER_POUSSIN);
        }
    }

    public void soignerSeringue() {
        if(malade != null){
            malade = null;
        }
    }

    public void nettoyer() {
        if(sale != null && ((utilisateur.getEcus() - VariablesGlobales.PRIX_NETTOYER_POUSSIN) >= 0)){
            sale = null;
            utilisateur.suppEcus(VariablesGlobales.PRIX_NETTOYER_POUSSIN);
        }
    }

    public void nettoyerSavon() {
        if(sale != null){
            sale = null;
        }
    }

    public boolean famine(){
        Timestamp now = new Timestamp(System.currentTimeMillis());
        LocalDate newNow = now.toLocalDateTime().toLocalDate();
        LocalDate dernierRepas = nourris.toLocalDateTime().toLocalDate();
        int difJour = (int)ChronoUnit.DAYS.between(dernierRepas, newNow);
        switch(difJour){
            case 2:
                poids -= VariablesGlobales.POIDS_FAMINE1J;
                poids = Math.round(poids * 100.0) / 100.0f;
                return false;
            case 3:
                poids -= VariablesGlobales.POIDS_FAMINE2J;
                poids = Math.round(poids * 100.0) / 100.0f;
                return false;
            case 4:
                poids -= VariablesGlobales.POIDS_FAMINE3J;
                poids = Math.round(poids * 100.0) / 100.0f;
                return false;
            case 5:
                List<Poussin> poussins = utilisateur.getPoussins();
                poussins.remove(poussins.indexOf(this));
                return true;
            default:
                return false;
        }
    }

    public boolean tuer(){
        if(malade != null){
            Timestamp now = new Timestamp(System.currentTimeMillis());
            LocalDate newNow = now.toLocalDateTime().toLocalDate();
            LocalDate newMalade = malade.toLocalDateTime().toLocalDate();
            int difJour = (int)ChronoUnit.DAYS.between(newMalade, newNow);
            if(difJour >= 4){
                List<Poussin> poussins = utilisateur.getPoussins();
                poussins.remove(poussins.indexOf(this));
                return true;
            }
        }
        return false;
    }

    public boolean grandir(){
        if(poids >= 2.5 && age >= 5){
            Random r = new Random();
            int val = r.nextInt(2);
            if(val == 0){
                Poule poule = new Poule(age, poids);
                utilisateur.addPoule(poule);
            }
            else{
                Coq coq = new Coq(age, poids);
                utilisateur.addCoq(coq);
            }
            List<Poussin> poussins = utilisateur.getPoussins();
            poussins.remove(poussins.indexOf(this));
            return true;
        }
        return false;
    }

    public void adultes(){
        poids = 2.5f;
        age = 5;
    }

    public boolean estPropre() {
        return sale == null;
    }

    public boolean estSain() {
        return malade == null;
    }

    public boolean estNourrie() {
        Timestamp now = new Timestamp(System.currentTimeMillis());
        return nourris.getDate() == now.getDate();
    }

    public boolean estAbreuver() {
        Timestamp now = new Timestamp(System.currentTimeMillis());
        return abreuve.getDate() == now.getDate();
    }

    public void affamerPoussin() {
        nourris = new Timestamp(System.currentTimeMillis() - 2*(86400 * 1000));
    }

    public void affamerPoussin2() {
        nourris = new Timestamp(System.currentTimeMillis() - 3*(86400 * 1000));
    }

    public void affamerPoussin3() {
        nourris = new Timestamp(System.currentTimeMillis() - 4*(86400 * 1000));
    }

    public void affamerPoussin4() {
        nourris = new Timestamp(System.currentTimeMillis() - 5*(86400 * 1000));
    }

    public void assoifferPoussin() {
        abreuve = new Timestamp(System.currentTimeMillis() - (86400 * 1000));
    }

    public void salePoussin() {
        sale = new Timestamp(System.currentTimeMillis() - (86400 * 1000));
    }

    public void maladePoussin() {
        malade = new Timestamp(System.currentTimeMillis() - (86400 * 1000));
    }

    public void maladePoussin4() {
        malade = new Timestamp(System.currentTimeMillis() - 5*(86400 * 1000));
    }

    public void maigrir(){
        poids = 0.5f;
    }

    public void incAge(){
        age += 1;
    }

    public void nourrirHier(){
        Timestamp now = new Timestamp(System.currentTimeMillis() - (86400 * 1000));
        if((utilisateur.getEcus() - VariablesGlobales.PRIX_NOURRIR_POUSSIN) >= 0){
            nourris = now;
            poids += VariablesGlobales.POIDS_NOURRIE_POUSSIN;
            if(abreuve.getDate() == now.getDate()) {
                poids += VariablesGlobales.POIDS_ABREUVE_POUSSIN;
            }
            poids = Math.min(poids, VariablesGlobales.POIDS_MAX_POUSSIN);
            poids = Math.round(poids * 100.0) / 100.0f;
            utilisateur.suppEcus(VariablesGlobales.PRIX_NOURRIR_POUSSIN);
        }
    }

    public void abreuveHier(){
        Timestamp now = new Timestamp(System.currentTimeMillis() - (86400 * 1000));
        if(((utilisateur.getEcus() - VariablesGlobales.PRIX_ABREUVE_POUSSIN) >= 0)){
            abreuve = now;
            if(nourris.getDate() == now.getDate()) {
                poids += VariablesGlobales.POIDS_ABREUVE_POUSSIN;
            }
            poids = Math.round(poids * 100.0) / 100.0f;
            poids = Math.min(poids, VariablesGlobales.POIDS_MAX_POUSSIN);
            utilisateur.suppEcus(VariablesGlobales.PRIX_ABREUVE_POUSSIN);
        }
    }
}