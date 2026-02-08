package fr.devweb.projet484i.entity;

import fr.devweb.projet484i.VariablesGlobales;

import com.fasterxml.jackson.annotation.JsonBackReference;

import jakarta.persistence.*;
import lombok.Data;

import java.sql.Timestamp;
import java.time.LocalDate;
import java.time.ZoneId;
import java.util.Random;


import org.springframework.scheduling.annotation.Scheduled;

@Entity
@Table(name = "vaches")
@Data
public class Vache {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @OneToOne
    @JoinColumn(name = "nomUtilisateur", nullable = false)
    @JsonBackReference
    private Fermier utilisateur;

    @Column(nullable = false)
    private float poids;

    @Column(nullable = false)
    private int age;

    private Timestamp nourris;
    private Timestamp abreuve;
    private Timestamp sale;
    private Timestamp malade;

    @Column(nullable = false)
    private Timestamp traite;

    @Column(nullable = false)
    private int litresLait;

    @Column(nullable = false)
    private boolean estVivante;

    public Vache() {
        estVivante = true;
        poids = VariablesGlobales.POIDS_VACHE;
        age = VariablesGlobales.AGE_VACHE;
        litresLait = VariablesGlobales.LITRES_LAIT;
        nourris = new Timestamp(System.currentTimeMillis() - (86400 * 1000));
        abreuve = new Timestamp(System.currentTimeMillis() - (86400 * 1000));
        sale = null;
        malade = null;
        traite = new Timestamp(System.currentTimeMillis() - (86400 * 1000));
    }

    @Scheduled(cron = "0 0 4,16 * * *") // UTC TIME
    public void prodLait(){
        if(estAdulte() && estPropre() && estSaine() && estNourrie()) {

            Timestamp now = new Timestamp(System.currentTimeMillis());

            LocalDate traiteDate = traite.toInstant().atZone(ZoneId.systemDefault()).toLocalDate();
            LocalDate nowDate = now.toInstant().atZone(ZoneId.systemDefault()).toLocalDate();

            if(traiteDate.getDayOfMonth() == nowDate.getDayOfMonth()) {
                litresLait += 8;
            } else {
                litresLait += 4;
            }
            litresLait = Math.min(litresLait, 16);
        }
    }

    public void traire(){
        utilisateur.getRemise().incLitresLait(litresLait);
        litresLait = VariablesGlobales.LITRES_LAIT;
        traite = new Timestamp(System.currentTimeMillis());
    }

    public void resetTraire(){
        traite = new Timestamp(System.currentTimeMillis() - (86400 * 1000));
    }

    public void nourrirBotteDePaille(){
        if(utilisateur.getRemise().getBottes_de_paille() > 0){
            nourris = new Timestamp(System.currentTimeMillis());
            poids += VariablesGlobales.POIDS_NOURRIE_PAILLE;
            utilisateur.getRemise().decBottesPaille();
        }
    }

    public void nourrirPaille(){
        if((utilisateur.getEcus() - VariablesGlobales.PRIX_NOURRIR_VACHE) >= 0){
            nourris = new Timestamp(System.currentTimeMillis());
            poids += VariablesGlobales.POIDS_NOURRIE_PAILLE;
            utilisateur.suppEcus(VariablesGlobales.PRIX_NOURRIR_VACHE);
        }
    }

    public void nourrirHerbe(){
        Timestamp now = new Timestamp(System.currentTimeMillis());

        LocalDate nourrisDate = nourris.toInstant().atZone(ZoneId.systemDefault()).toLocalDate();
        LocalDate nowDate = now.toInstant().atZone(ZoneId.systemDefault()).toLocalDate();

        if(nourrisDate.getDayOfMonth() != nowDate.getDayOfMonth()){
            nourris = now;
            poids += VariablesGlobales.POIDS_NOURRIE_HERBE;
            LocalDate abreuveDate = abreuve.toInstant().atZone(ZoneId.systemDefault()).toLocalDate();
            if(abreuveDate.getDayOfMonth() == nowDate.getDayOfMonth()) {
                poids += VariablesGlobales.POIDS_ABREUVE_VACHE;
            }
        }
    }

    public void abreuve(){
        Timestamp now = new Timestamp(System.currentTimeMillis());
        LocalDate abreuveDate = abreuve.toInstant().atZone(ZoneId.systemDefault()).toLocalDate();
        LocalDate nourrisDate = nourris.toInstant().atZone(ZoneId.systemDefault()).toLocalDate();
        LocalDate nowDate = now.toInstant().atZone(ZoneId.systemDefault()).toLocalDate();

        if(abreuveDate.getDayOfMonth() != nowDate.getDayOfMonth() && ((utilisateur.getEcus() - VariablesGlobales.PRIX_ABREUVE_VACHE) >= 0)){
            abreuve = now;
            if(nourrisDate.getDayOfMonth() == nowDate.getDayOfMonth()) {
                poids += VariablesGlobales.POIDS_ABREUVE_VACHE;
            }
            utilisateur.suppEcus(VariablesGlobales.PRIX_ABREUVE_VACHE);
        }
    }

    public void abreuveSeauDeau(){
        Timestamp now = new Timestamp(System.currentTimeMillis());
        
        LocalDate abreuveDate = abreuve.toInstant().atZone(ZoneId.systemDefault()).toLocalDate();
        LocalDate nourrisDate = nourris.toInstant().atZone(ZoneId.systemDefault()).toLocalDate();
        LocalDate nowDate = now.toInstant().atZone(ZoneId.systemDefault()).toLocalDate();
        
        if(abreuveDate.getDayOfMonth() != nowDate.getDayOfMonth() && (utilisateur.getRemise().getEau() > 0)){
            abreuve = now;
            if(nourrisDate.getDayOfMonth() == nowDate.getDayOfMonth()) {
                poids += VariablesGlobales.POIDS_ABREUVE_VACHE;
            }
            utilisateur.getRemise().decEau();
        }
    }

    public void affamerVache() {
        nourris = new Timestamp(System.currentTimeMillis() - (86400 * 1000));
    }

    public void assoifferVache() {
        abreuve = new Timestamp(System.currentTimeMillis() - (86400 * 1000));
    }

    public boolean estAdulte() {
        return age >= 10 && poids >= 80;
    }

    public void grandir() {
        age = 10;
        poids = 80;
    }

    public void rajeunir() {
        poids = 10;
    }

    public void maigrir() {
        poids = 0;
    }

    public void tomberMalade() {
        malade = new Timestamp(System.currentTimeMillis());
    }

    public void tomberMalade5Jours() { // Rend la vache malade depuis 5 jours à des fins de tests
        malade = new Timestamp(System.currentTimeMillis() - (86400 * 1000)*5);
    }

    public void soigner() {
        if(malade != null && ((utilisateur.getEcus() - VariablesGlobales.PRIX_SOIGNER_VACHE) >= 0)){
            malade = null;
            utilisateur.suppEcus(VariablesGlobales.PRIX_SOIGNER_VACHE);
        }
    }

    public void soignerSeringue() {
        if(malade != null && (utilisateur.getRemise().getSeringue() > 0)){
            malade = null;
            utilisateur.getRemise().decSeringues();
        }
    }

    public void seSalir() {
        sale = new Timestamp(System.currentTimeMillis());
    }

    public void nettoyer() {
        if(sale != null && ((utilisateur.getEcus() - VariablesGlobales.PRIX_NETTOYER_VACHE) >= 0)){
            sale = null;
            utilisateur.suppEcus(VariablesGlobales.PRIX_NETTOYER_VACHE);
        }
    }

    public void nettoyerSavon() {
        if(sale != null && (utilisateur.getRemise().getSavon() > 0)){
            sale = null;
            utilisateur.getRemise().decSavons();
        }
    }

    public boolean estPropre() {
        return sale == null;
    }

    public boolean estSaine() {
        return malade == null;
    }

    public boolean estNourrie() {
        Timestamp now = new Timestamp(System.currentTimeMillis());

        LocalDate nourrisDate = nourris.toInstant().atZone(ZoneId.systemDefault()).toLocalDate();
        LocalDate nowDate = now.toInstant().atZone(ZoneId.systemDefault()).toLocalDate();
        return nourrisDate.getDayOfMonth() == nowDate.getDayOfMonth();
    }

    public boolean estAbreuvee() {
        Timestamp now = new Timestamp(System.currentTimeMillis());

        LocalDate abreuveDate = abreuve.toInstant().atZone(ZoneId.systemDefault()).toLocalDate();
        LocalDate nowDate = now.toInstant().atZone(ZoneId.systemDefault()).toLocalDate();

        return abreuveDate.getDayOfMonth() == nowDate.getDayOfMonth();
    }

    public void remplir() {
        litresLait = 16;
    }

    public void vider() {
        litresLait = 0;
    }

    public void mourir() {
        if(poids <= 0) {
            estVivante = false;
        }
        if(malade != null) {
            Timestamp now = new Timestamp(System.currentTimeMillis());

            LocalDate maladeDate = malade.toInstant().atZone(ZoneId.systemDefault()).toLocalDate();
            LocalDate nowDate = now.toInstant().atZone(ZoneId.systemDefault()).toLocalDate();

            if(nowDate.getDayOfMonth() - maladeDate.getDayOfMonth() >= 4) {
                estVivante = false;
            }
        }
    }

    public void ressuciter() {
        estVivante = true;
    }

    public void passageJour() {
        Random r = new Random();
        int x = r.nextInt(100);
        if(x < VariablesGlobales.POURCENTAGE_MALADIE_VACHE && malade == null) {tomberMalade();}

        x = r.nextInt(100);
        if(x < VariablesGlobales.POURCENTAGE_SALE_VACHE && sale == null) {seSalir();}
        age += 1;        
        mourir(); //tue si condition remplie dans mourir
    }
}