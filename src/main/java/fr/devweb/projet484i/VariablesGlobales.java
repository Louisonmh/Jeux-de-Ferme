package fr.devweb.projet484i;

import java.sql.Timestamp;
import java.util.ArrayList;
import java.util.List;
import fr.devweb.projet484i.entity.Fermier;

import lombok.Data;

@Data
public class VariablesGlobales{

    // Valeurs d'utilisateur
    public static final  int ECUS = 500;
    public static final int MONTANT_EMPRUNT = 1500;

    // Valeurs de la vache
    public static final int AGE_VACHE = 0;
    public static final int LITRES_LAIT = 0;
    public static final int PRIX_NOURRIR_VACHE = 5;
    public static final int PRIX_ABREUVE_VACHE = 2;
    public static final int PRIX_SOIGNER_VACHE = 6;
    public static final int PRIX_NETTOYER_VACHE = 3;
    public static final int POURCENTAGE_MALADIE_VACHE = 10;  //une chance sur 10
    public static final int POURCENTAGE_SALE_VACHE = 10; 
    
    public static final float POIDS_VACHE = 1f;
    public static final float POIDS_NOURRIE_PAILLE = 3f;
    public static final float POIDS_NOURRIE_HERBE = 5f;
    public static final float POIDS_ABREUVE_VACHE = 1f;
  
    // Valeurs des clapiers
    public static final int PRIX_NOURRIR_CLAPIER = 5;
    public static final int PRIX_ABREUVE_CLAPIER = 2;
    public static final int PRIX_SOIGNER_CLAPIER = 6;
    public static final int PRIX_NETTOYER_CLAPIER = 3;
    public static final int NB_CLAPIER_MAX = 50;
    public static final int POURCENTAGE_MALADE_LAPIN = 25;
    public static final int POURCENTAGE_SALE_LAPIN = 25;

    // Valeurs volailles
    public static final int NB_VOLAILLES_MAX = 60;
  
    //valeur d'une poule
    public static final float POIDS_POULE = 2.5f;
    public static final float POIDS_MAX_POULE = 3.5f;
    public static final int AGE_POULE = 5;
    public static final float POIDS_FAMINE1J = 0.2f;
    public static final float POIDS_FAMINE2J = 0.5f;
    public static final float POIDS_FAMINE3J = 1.0f;
    public static final int PRIX_ABREUVE_POULE = 1;
    public static final int PRIX_NOURRIR_POULE = 3;
    public static final int PRIX_SOIGNER_POULE = 6;
    public static final int PRIX_NETTOYER_POULE = 3;
    public static final float POIDS_NOURRIE_POULE = 0.5f;
    public static final float POIDS_ABREUVE_POULE = 0.15f;
    public static final int POURCENTAGE_MALADE_POULE = 25;
    public static final int POURCENTAGE_SALE_POULE = 25;

    //valeur d'un coq
    public static final float POIDS_COQ = 2.5f;
    public static final float POIDS_MAX_COQ = 3.5f;
    public static final int AGE_COQ = 5;
    public static final int PRIX_ABREUVE_COQ = 1;
    public static final int PRIX_NOURRIR_COQ = 3;
    public static final int PRIX_SOIGNER_COQ = 6;
    public static final int PRIX_NETTOYER_COQ = 3;
    public static final float POIDS_NOURRIE_COQ = 0.5f;
    public static final float POIDS_ABREUVE_COQ = 0.15f;
    public static final int POURCENTAGE_MALADE_COQ = 25;
    public static final int POURCENTAGE_SALE_COQ = 25;

    //valeur d'un poussin
    public static final float POIDS_POUSSIN = 0.5f;
    public static final float POIDS_MAX_POUSSIN = 3.5f;
    public static final int AGE_POUSSIN = 0;
    public static final int PRIX_ABREUVE_POUSSIN = 1;
    public static final int PRIX_NOURRIR_POUSSIN = 3;
    public static final int PRIX_SOIGNER_POUSSIN = 6;
    public static final int PRIX_NETTOYER_POUSSIN = 3;
    public static final float POIDS_NOURRIE_POUSSIN = 0.5f;
    public static final float POIDS_ABREUVE_POUSSIN = 0.15f;
    public static final int POURCENTAGE_MALADE_POUSSIN = 25;
    public static final int POURCENTAGE_SALE_POUSSIN = 25;

    // valeur des coefs des stats
    public static final int COEF_OEUFS = 15;
    public static final int COEF_LAPINS = 30;
    public static final int COEF_VOLAILLES = 25;
    public static final int COEF_LAIT = 20;
    public static final int COEF_ACHAT_MARCHE = 10;
    public static final int COEF_VENTE_MARCHE = 15;
    public static final int COEF_ECUS = 30;

    // Définition des constantes pour les articles
    public static final String LAPINS_MALES = "LapinsMales";
    public static final String LAPINS_FEMELLES = "LapinsFemelles";
    public static final String POULE = "Poule";
    public static final String COQ = "Coq";
    public static final String OEUF = "Oeuf";
    public static final String LAIT = "Lait";
    public static final String SAVON = "Savon";
    public static final String SERINGUE = "Seringue";
    public static final String PAILLE = "Paille";
    public static final String SAC_NOURRITURE = "SacNourriture";
    public static final String EAU = "Eau";

    // stats global du jeu
    public static int oeufsVendu = 0;
    public static int lapinsVenduCoop = 0;
    public static int volaillesVenduCoop = 0;
    public static int laitVendu = 0;
    public static int achatMarche = 0;
    public static int venteMarche = 0;
    public static int solde = 0;
    

    // Valeurs de la cooperative
    public static final int PRIX_COOP_LAPIN_MALE = 50;
    public static final int PRIX_COOP_LAPIN_FEMELLE = 50;
    public static final int PRIX_COOP_POULE = 60;
    public static final int PRIX_COOP_COQ = 50;
    public static final int PRIX_COOP_OEUF = 8;
    public static final int PRIX_COOP_LAIT = 2;
    public static final int PRIX_COOP_SAVON = 10;
    public static final int PRIX_COOP_EAU = 10;
    public static final int PRIX_COOP_SAC_NOURRITURE = 10;
    public static final int PRIX_COOP_PAILLE = 10;
    public static final int PRIX_COOP_SERINGUE = 10;

    private VariablesGlobales(){
        //constructeur pas défault
    }

    public static void addOeufsVendu(int n){
        oeufsVendu += n;
    }

    public static void addLapinsVenduCoop(int n){
        lapinsVenduCoop += n;
    }

    public static void addVolaillesVenduCoop(int n){
        volaillesVenduCoop += n;
    }

    public static void addLaitVendu(int n){
        laitVendu += n;
    }
    public static void addAchatMarche(int n){
        achatMarche += n;
    }

    public static void addVenteMarche(int n){
        venteMarche += n;
    }

    public static void addSolde(int n){
        solde += n;
    }

    public static void reducSolde(int n){
        solde -= n;
    }
}