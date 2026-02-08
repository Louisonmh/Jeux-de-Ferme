package fr.devweb.projet484i.entity;

import fr.devweb.projet484i.VariablesGlobales;

import com.fasterxml.jackson.annotation.JsonBackReference;

import jakarta.persistence.*;
import lombok.Data;

import java.sql.Timestamp;

import java.util.Random;

@Entity
@Table(name = "clapier")
@Data
public class Clapier {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private boolean adultesNourris;
    private boolean adultesAbreuves;
    private boolean adultesSales;
    private boolean adultesMalades;
    private boolean enfantsNourris;
    private boolean enfantsAbreuves;
    private boolean enfantsSales;
    private boolean enfantsMalades;

    @Column(nullable = false)
    private int nbLapinsMales;

    @Column(nullable = false)
    private int nbLapinsFemelles;

    @Column(nullable = false)
    private int nbLapereauxBebes;

    @Column(nullable = false)
    private int nbLapereauxPetits;

    @Column(nullable = false)
    private int nbLapereauxGros;

    @OneToOne
    @JoinColumn(name = "nomUtilisateur", nullable = false)
    @JsonBackReference
    private Fermier utilisateur;

    public Clapier() {
        adultesNourris = false;
        adultesAbreuves = false;
        adultesSales = false;
        adultesMalades = false;
        enfantsNourris = true;
        enfantsAbreuves = true;
        enfantsSales = false;
        enfantsMalades = false;
        nbLapinsMales = 0;
        nbLapinsFemelles = 0;
        nbLapereauxBebes = 8;
        nbLapereauxPetits = 0;
        nbLapereauxGros = 0;
    }

    public void affamerAdultes() {
        adultesNourris = false;
    }

    public void nourrirAdultes(){
        if(((utilisateur.getEcus() - VariablesGlobales.PRIX_NOURRIR_CLAPIER) >= 0) && !adultesNourris && (nbLapinsFemelles > 0 || nbLapinsMales > 0)){
            adultesNourris = true;
            utilisateur.suppEcus(VariablesGlobales.PRIX_NOURRIR_CLAPIER);
        }
    }

    public void nourrirAdultesSac(){
        if((utilisateur.getRemise().getSac_nourriture() > 0) && !adultesNourris && (nbLapinsFemelles > 0 || nbLapinsMales > 0)){
            adultesNourris = true;
            utilisateur.getRemise().decSacsNourriture();
        }
    }

    public void assoifferAdultes() {
        adultesAbreuves = false;
    }

    public void abreuveAdultes(){
        if(!adultesAbreuves && ((utilisateur.getEcus() - VariablesGlobales.PRIX_ABREUVE_CLAPIER) >= 0) && (nbLapinsFemelles > 0 || nbLapinsMales > 0)){
            adultesAbreuves = true;
            utilisateur.suppEcus(VariablesGlobales.PRIX_ABREUVE_CLAPIER);
        }
    }

    public void abreuveAdultesSeauDeau(){
        if(!adultesAbreuves && (utilisateur.getRemise().getEau() > 0) && (nbLapinsFemelles > 0 || nbLapinsMales > 0)){
            adultesAbreuves = true;
            utilisateur.getRemise().decEau();
        }
    }

    public void adultesMalades() {
        adultesMalades = true;
    }

    public void soignerAdultes() {
        if(adultesMalades && ((utilisateur.getEcus() - VariablesGlobales.PRIX_SOIGNER_CLAPIER) >= 0) && (nbLapinsFemelles > 0 || nbLapinsMales > 0)){
            adultesMalades = false;
            utilisateur.suppEcus(VariablesGlobales.PRIX_SOIGNER_CLAPIER);
        }
    }

    public void soignerAdultesSeringue() {
        if(adultesMalades && (utilisateur.getRemise().getSeringue() > 0) && (nbLapinsFemelles > 0 || nbLapinsMales > 0)){
            adultesMalades = false;
            utilisateur.getRemise().decSeringues();
        }
    }

    public void salirAdultes() {
        adultesSales = true;
    }

    public void nettoyerAdultes() {
        if(adultesSales && ((utilisateur.getEcus() - VariablesGlobales.PRIX_NETTOYER_CLAPIER) >= 0) && (nbLapinsFemelles > 0 || nbLapinsMales > 0)){
            adultesSales = false;
            utilisateur.suppEcus(VariablesGlobales.PRIX_NETTOYER_CLAPIER);
        }
    }

    public void nettoyerAdultesSavon() {
        if(adultesSales && (utilisateur.getRemise().getSavon() > 0) && (nbLapinsFemelles > 0 || nbLapinsMales > 0)){
            adultesSales = false;
            utilisateur.getRemise().decSavons();
        }
    }

    public void suppAdultesMales(int n) {
        if(n > nbLapinsMales) {
            n = nbLapinsMales;
        }
        nbLapinsMales -= n;
        utilisateur.getRemise().setLapinsMales(utilisateur.getRemise().getLapinsMales() - n);
    }

    public void suppAdultesFemelles(int n) {
        if(n > nbLapinsFemelles) {
            n = nbLapinsFemelles;
        }
        nbLapinsFemelles -= n;
        utilisateur.getRemise().setLapinsFemelles(utilisateur.getRemise().getLapinsFemelles() - n);
    }

    public void addAdultesMales(int n) {
        nbLapinsMales += n;
        utilisateur.getRemise().setLapinsMales(utilisateur.getRemise().getLapinsMales() + n);
    }

    public void addAdultesFemelles(int n) {
        nbLapinsFemelles += n;
        utilisateur.getRemise().setLapinsFemelles(utilisateur.getRemise().getLapinsFemelles() + n);
    }

    public void assoifferEnfants() {
        enfantsAbreuves = false;
    }

    public void affamerEnfants() {
        enfantsNourris = false;
    }

    public void nourrirEnfants(){
        if(((utilisateur.getEcus() - VariablesGlobales.PRIX_NOURRIR_CLAPIER) >= 0) && !enfantsNourris && (nbLapereauxBebes > 0 || nbLapereauxPetits > 0 || nbLapereauxGros > 0)){
            enfantsNourris = true;
            utilisateur.suppEcus(VariablesGlobales.PRIX_NOURRIR_CLAPIER);
        }
    }

    public void nourrirEnfantsSac(){
        if((utilisateur.getRemise().getSac_nourriture() > 0) && !enfantsNourris && (nbLapereauxBebes > 0 || nbLapereauxPetits > 0 || nbLapereauxGros > 0)){
            enfantsNourris = true;
            utilisateur.getRemise().decSacsNourriture();
        }
    }

    public void abreuveEnfants(){
        if(!enfantsAbreuves && ((utilisateur.getEcus() - VariablesGlobales.PRIX_ABREUVE_CLAPIER) >= 0) && (nbLapereauxBebes > 0 || nbLapereauxPetits > 0 || nbLapereauxGros > 0)){
            enfantsAbreuves = true;
            utilisateur.suppEcus(VariablesGlobales.PRIX_ABREUVE_CLAPIER);
        }
    }

    public void abreuveEnfantsSeauDeau(){
        if(!enfantsAbreuves && (utilisateur.getRemise().getEau() > 0) && (nbLapereauxBebes > 0 || nbLapereauxPetits > 0 || nbLapereauxGros > 0)){
            enfantsAbreuves = true;
            utilisateur.getRemise().decEau();
        }
    }

    public void enfantsMalades() {
        enfantsMalades = true;
    }

    public void soignerEnfants() {
        if(enfantsMalades && ((utilisateur.getEcus() - VariablesGlobales.PRIX_SOIGNER_CLAPIER) >= 0) && (nbLapereauxBebes > 0 || nbLapereauxPetits > 0 || nbLapereauxGros > 0)){
            enfantsMalades = false;
            utilisateur.suppEcus(VariablesGlobales.PRIX_SOIGNER_CLAPIER);
        }
    }

    public void soignerEnfantsSeringue() {
        if(enfantsMalades && (utilisateur.getRemise().getSeringue() > 0) && (nbLapereauxBebes > 0 || nbLapereauxPetits > 0 || nbLapereauxGros > 0)){
            enfantsMalades = false;
            utilisateur.getRemise().decSeringues();
        }
    }

    public void salirEnfants() {
        enfantsSales = true;
    }

    public void nettoyerEnfants() {
        if(enfantsSales && ((utilisateur.getEcus() - VariablesGlobales.PRIX_NETTOYER_CLAPIER) >= 0) && (nbLapereauxBebes > 0 || nbLapereauxPetits > 0 || nbLapereauxGros > 0)){
            enfantsSales = false;
            utilisateur.suppEcus(VariablesGlobales.PRIX_NETTOYER_CLAPIER);
        }
    }

    public void nettoyerEnfantsSavon() {
        if(enfantsSales && (utilisateur.getRemise().getSavon() > 0) && (nbLapereauxBebes > 0 || nbLapereauxPetits > 0 || nbLapereauxGros > 0)){
            enfantsSales = false;
            utilisateur.getRemise().decSavons();
        }
    }

    public void suppBebes(int n) {
        nbLapereauxBebes -= n;
        nbLapereauxBebes = Math.max(0, nbLapereauxBebes);
    }

    public void addBebes(int n) {
        nbLapereauxBebes += n;
    }

    public void suppPetits(int n) {
        nbLapereauxPetits -= n;
        nbLapereauxPetits = Math.max(0, nbLapereauxPetits);
    }

    public void addPetits(int n) {
        nbLapereauxPetits += n;
    }

    public void suppGros(int n) {
        nbLapereauxGros -= n;
        nbLapereauxGros = Math.max(0, nbLapereauxGros);
    }

    public void addGros(int n) {
        nbLapereauxGros += n;
    }

    public void remplirClapier() {
        viderClapier();
        addBebes(5);
        addPetits(5);
        addGros(5);
        addAdultesMales(5);
        addAdultesFemelles(5);
    }

    public void remplirMaxClapier() {
        viderClapier();
        addBebes(20);
        addPetits(20);
        addGros(10);
        addAdultesMales(25);
        addAdultesFemelles(25);
    }

    public void viderClapier() {
        suppBebes(nbLapereauxBebes);
        suppPetits(nbLapereauxPetits);
        suppGros(nbLapereauxGros);
        suppAdultesMales(nbLapinsMales);
        suppAdultesFemelles(nbLapinsFemelles);
    }

    public void grandir() {
        if(enfantsNourris && enfantsAbreuves) {
            int max = Math.min((VariablesGlobales.NB_CLAPIER_MAX - (nbLapinsMales + nbLapinsFemelles)), nbLapereauxGros);
            for(int i = 0; i < max; i++) {
                Random r = new Random();
                int x = r.nextInt(2);
                if(x == 0) {
                    addAdultesFemelles(1);
                } else {
                    addAdultesMales(1);
                }
                suppGros(1);
            }
            nbLapereauxGros += nbLapereauxPetits;
            nbLapereauxPetits = nbLapereauxBebes;
            nbLapereauxBebes = 0;
        }
    }

    public void reproduction() {
        int nbCouples = (int)Math.min(nbLapinsMales, nbLapinsFemelles);
        int nbNaissances = 0;
        for(int i = 0; i < nbCouples; i++) {
            Random r = new Random();
            nbNaissances += r.nextInt(2);
        }
        if(adultesNourris && !adultesAbreuves) {
            nbNaissances = (int)(nbNaissances * 1.5);
        } else if(adultesNourris && adultesAbreuves) {
            nbNaissances *= 2;
        }
        int placesDispo = VariablesGlobales.NB_CLAPIER_MAX - (nbLapereauxBebes + nbLapereauxPetits + nbLapereauxGros);
        if(placesDispo < 0) {
            placesDispo = 0;
        }
        if(nbNaissances > placesDispo) {
            nbNaissances = placesDispo;
        }
        nbLapereauxBebes += nbNaissances;
    }

    public void mort() {
        Random r = new Random();
        if(!enfantsNourris || enfantsMalades || enfantsSales) {
            if(nbLapereauxBebes > 0) {
                int bebesMorts = Math.max(r.nextInt(nbLapereauxBebes + 1), 1);
                nbLapereauxBebes -= bebesMorts;
            } else if(nbLapereauxPetits > 0) {
                int petitsMorts = Math.max(r.nextInt(nbLapereauxPetits + 1), 1);
                nbLapereauxPetits -= petitsMorts;
            } else if(nbLapereauxGros > 0) {
                int grosMorts = Math.max(r.nextInt(nbLapereauxGros + 1), 1);
                nbLapereauxGros -= grosMorts;
            }
        }
        if(!adultesNourris || adultesMalades || adultesSales) {
            int malesMorts = Math.max(r.nextInt(nbLapinsMales), 1);
            suppAdultesMales(malesMorts);
            int femellesMortes = Math.max(r.nextInt(nbLapinsFemelles), 1);
            suppAdultesFemelles(femellesMortes);
        }
    }

    public void passageJour() {
        mort();
        grandir();
        reproduction();
        enfantsAbreuves = false;
        enfantsNourris = false;
        adultesAbreuves = false;
        adultesNourris = false;
        Random r = new Random();
        int x = r.nextInt(100);
        if(x < VariablesGlobales.POURCENTAGE_MALADE_LAPIN) {
            enfantsMalades = true;
        }
        x = r.nextInt(100);
        if(x < VariablesGlobales.POURCENTAGE_MALADE_LAPIN) {
            adultesMalades = true;
        }
        x = r.nextInt(100);
        if(x < VariablesGlobales.POURCENTAGE_SALE_LAPIN) {
            enfantsSales = true;
        }
        x = r.nextInt(100);
        if(x < VariablesGlobales.POURCENTAGE_SALE_LAPIN) {
            adultesSales = true;
        }
    }
}