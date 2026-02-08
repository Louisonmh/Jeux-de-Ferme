package fr.devweb.projet484i.entity;

import fr.devweb.projet484i.VariablesGlobales;

import com.fasterxml.jackson.annotation.JsonBackReference;

import jakarta.persistence.*;
import lombok.Data;

import java.sql.Timestamp;
import java.util.Random;
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

import java.time.LocalDateTime;
import java.util.List;
import java.lang.Math;

@Entity
@Table(name = "poules")
@Data
public class Poule {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne
    @JoinColumn(name = "utilisateur_id", nullable = false)
    @JsonBackReference
    private Fermier utilisateur;

    private boolean enCouvaison;
    private int age;
    private float poids;
    private Timestamp nourris;
    private Timestamp abreuve;
    private Timestamp sale;
    private Timestamp malade;

    public Poule() {}

    public Poule(int age, float poids){
        enCouvaison = false;
        this.age = age;
        this.poids = poids;
        nourris = new Timestamp(System.currentTimeMillis() - (86400 * 1000));
        abreuve = new Timestamp(System.currentTimeMillis() - (86400 * 1000));
        sale = null;
        malade = null;
    }

    public boolean pondre(){
        if(estNourrie() && estPropre() && estSaine() && (enCouvaison == false) && estAdulte()){
            // pond entre 0, 1 et 2 oeufs, 1 chance sur 3 pour chaque
            Random r = new Random();
            double val = r.nextFloat();
            if(val < (1f/3)){
                utilisateur.getRemise().incOeufs(0);
            }
            else if(val < (2f/3)){
                utilisateur.getRemise().incOeufs(1);
            }
            else{
                utilisateur.getRemise().incOeufs(2);
            }
            return true;
        }
        return false;
    }

    public void couver(){
        if(!enCouvaison){
            enCouvaison = true;
            utilisateur.getRemise().decOeufs(1);
        }
    }

    public void couvaison(){
        enCouvaison = true;
    }

    public void arreterCouver(){
        if(enCouvaison){
            enCouvaison = false;
            Poussin poussin = new Poussin(VariablesGlobales.AGE_POUSSIN, VariablesGlobales.POIDS_POUSSIN);
            utilisateur.addPoussin(poussin);
        }
    }

    public void nourrir(){
        Timestamp now = new Timestamp(System.currentTimeMillis());

        LocalDate newNow = now.toLocalDateTime().toLocalDate();
        LocalDate dernierRepas = nourris.toLocalDateTime().toLocalDate();

        if(dernierRepas.getDayOfYear() != newNow.getDayOfYear() && (utilisateur.getEcus() - VariablesGlobales.PRIX_NOURRIR_POULE) >= 0){
            nourris = now;
            poids += VariablesGlobales.POIDS_NOURRIE_POULE;
            if(abreuve.getDate() == now.getDate()) {
                poids += VariablesGlobales.POIDS_ABREUVE_POULE;
            }
            poids = Math.min(poids, VariablesGlobales.POIDS_MAX_POULE);
            poids = Math.round(poids * 100.0) / 100.0f;
            utilisateur.suppEcus(VariablesGlobales.PRIX_NOURRIR_POULE);
        }
    }

    public void nourrirSacNourriture(){
        Timestamp now = new Timestamp(System.currentTimeMillis());
        if(nourris.getDate() != now.getDate()){
            nourris = now;
            poids += VariablesGlobales.POIDS_NOURRIE_POULE;
            if(abreuve.getDate() == now.getDate()) {
                poids += VariablesGlobales.POIDS_ABREUVE_POULE;
            }
            poids = Math.round(poids * 100.0) / 100.0f;
            poids = Math.min(poids, VariablesGlobales.POIDS_MAX_POULE);
        }
    }

    public void abreuve(){
        Timestamp now = new Timestamp(System.currentTimeMillis());
        if(abreuve.getDate() != now.getDate() && ((utilisateur.getEcus() - VariablesGlobales.PRIX_ABREUVE_POULE) >= 0)){
            abreuve = now;
            if(nourris.getDate() == now.getDate()) {
                poids += VariablesGlobales.POIDS_ABREUVE_POULE;
            }
            poids = Math.round(poids * 100.0) / 100.0f;
            poids = Math.min(poids, VariablesGlobales.POIDS_MAX_POULE);
            utilisateur.suppEcus(VariablesGlobales.PRIX_ABREUVE_POULE);
        }
    }

    public void abreuveSeauDeau(){
        Timestamp now = new Timestamp(System.currentTimeMillis());
        if(abreuve.getDate() != now.getDate()){
            abreuve = now;
            if(nourris.getDate() == now.getDate()) {
                poids += VariablesGlobales.POIDS_ABREUVE_POULE;
            }
            poids = Math.round(poids * 100.0) / 100.0f;
            poids = Math.min(poids, VariablesGlobales.POIDS_MAX_POULE);
        }
    }

    public void soigner() {
        if(malade != null && ((utilisateur.getEcus() - VariablesGlobales.PRIX_SOIGNER_POULE) >= 0)){
            malade = null;
            utilisateur.suppEcus(VariablesGlobales.PRIX_SOIGNER_POULE);
        }
    }

    public void soignerSeringue() {
        if(malade != null){
            malade = null;
        }
    }

    public void nettoyer() {
        if(sale != null && ((utilisateur.getEcus() - VariablesGlobales.PRIX_NETTOYER_POULE) >= 0)){
            sale = null;
            utilisateur.suppEcus(VariablesGlobales.PRIX_NETTOYER_POULE);
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
                List<Poule> poules = utilisateur.getPoules();
                poules.remove(poules.indexOf(this));
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
            if(difJour >= 5){
                List<Poule> poules = utilisateur.getPoules();
                poules.remove(poules.indexOf(this));
                return true;
            }
        }
        return false;
    }

    public boolean regression(){
        if(poids < 2.5f){
            Poussin poussin = new Poussin(age, poids);
            utilisateur.addPoussin(poussin);
            List<Poule> poules = utilisateur.getPoules();
            poules.remove(poules.indexOf(this));
            return true;
        }
        return false;
    }

    public void enfant(){
        poids = 0.5f;
    }

    public boolean estAdulte() {
        return age >= 5 && poids >= 2.5;
    }

    public boolean estPropre() {
        return sale == null;
    }

    public boolean estSaine() {
        return malade == null;
    }

    public boolean estNourrie() {
        Timestamp now = new Timestamp(System.currentTimeMillis());
        return nourris.getDate() == now.getDate() - 1;
    }

    public boolean estAbreuver() {
        Timestamp now = new Timestamp(System.currentTimeMillis());
        return abreuve.getDate() == now.getDate();
    }

    public void abreuver() {
        abreuve = new Timestamp(System.currentTimeMillis());
    }

    public void affamerPoule() {
        nourris = new Timestamp(System.currentTimeMillis() - 2*(86400 * 1000));
    }

    public void affamerPoule2() {
        nourris = new Timestamp(System.currentTimeMillis() - 3*(86400 * 1000));
    }

    public void affamerPoule3() {
        nourris = new Timestamp(System.currentTimeMillis() - 4*(86400 * 1000));
    }

    public void affamerPoule4() {
        nourris = new Timestamp(System.currentTimeMillis() - 5*(86400 * 1000));
    }

    public void assoifferPoule() {
        abreuve = new Timestamp(System.currentTimeMillis() - (86400 * 1000));
    }

    public void salePoule() {
        sale = new Timestamp(System.currentTimeMillis() - (86400 * 1000));
    }

    public void maladePoule() {
        malade = new Timestamp(System.currentTimeMillis() - (86400 * 1000));
    }

    public void maladePoule4() {
        malade = new Timestamp(System.currentTimeMillis() - 5*(86400 * 1000));
    }

    public void maigrir(){
        poids = 2.5f;
    }

    public void incAge(){
        age += 1;
    }

    public void nourrirHier(){
        Timestamp now = new Timestamp(System.currentTimeMillis() - (86400 * 1000));
        if((utilisateur.getEcus() - VariablesGlobales.PRIX_NOURRIR_POULE) >= 0){
            nourris = now;
            poids += VariablesGlobales.POIDS_NOURRIE_POULE;
            if(abreuve.getDate() == now.getDate()) {
                poids += VariablesGlobales.POIDS_ABREUVE_POULE;
            }
            poids = Math.min(poids, VariablesGlobales.POIDS_MAX_POULE);
            poids = Math.round(poids * 100.0) / 100.0f;
            utilisateur.suppEcus(VariablesGlobales.PRIX_NOURRIR_POULE);
        }
    }

    public void abreuveHier(){
        Timestamp now = new Timestamp(System.currentTimeMillis() - (86400 * 1000));
        if(((utilisateur.getEcus() - VariablesGlobales.PRIX_ABREUVE_POULE) >= 0)){
            abreuve = now;
            if(nourris.getDate() == now.getDate()) {
                poids += VariablesGlobales.POIDS_ABREUVE_POULE;
            }
            poids = Math.round(poids * 100.0) / 100.0f;
            poids = Math.min(poids, VariablesGlobales.POIDS_MAX_POULE);
            utilisateur.suppEcus(VariablesGlobales.PRIX_ABREUVE_POULE);
        }
    }
}
