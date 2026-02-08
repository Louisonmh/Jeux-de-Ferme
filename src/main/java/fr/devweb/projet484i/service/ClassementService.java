package fr.devweb.projet484i.service;

import fr.devweb.projet484i.entity.Fermier;
import org.springframework.stereotype.Service;
import fr.devweb.projet484i.repository.FermierRepository;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.scheduling.annotation.Scheduled;

import java.util.Optional;
import jakarta.transaction.Transactional;
import java.util.ArrayList;
import java.util.List;

import fr.devweb.projet484i.VariablesGlobales;

import org.springframework.boot.context.event.ApplicationReadyEvent;
import org.springframework.context.event.EventListener;

@Service
public class ClassementService{
    private final FermierRepository fermierRepository;
    private final FermierService fermierService;

    public ClassementService(FermierRepository fermierRepository, FermierService fermierService) {
        this.fermierRepository = fermierRepository;
        this.fermierService = fermierService;
    }

    @EventListener(ApplicationReadyEvent.class)
    @Scheduled(cron = "0 0,30 * * * *")
    @Transactional
    public List<Fermier> calculClassement(){
        List<Fermier> fermiers = fermierRepository.findAll();
        int pointEcus = 0;
        int pointOeufsVendus = 0;
        int pointLapinsVendusCoop = 0;
        int pointVenteLait = 0;
        int pointAchatsMarche = 0;
        int pointVentesMarche = 0;
        int nbJ = fermiers.size();

        for(Fermier fermier : fermiers){
            if(VariablesGlobales.solde != 0){pointEcus = (int)(((float)(fermier.getStatistique().getSolde() * 100 / VariablesGlobales.solde) / 100) * (nbJ * VariablesGlobales.COEF_ECUS));}

            if(VariablesGlobales.oeufsVendu != 0){pointOeufsVendus = (int)(((float)(fermier.getStatistique().getOeufsVendu() * 100 / VariablesGlobales.oeufsVendu) / 100) * (nbJ * VariablesGlobales.COEF_OEUFS));}
            
            if(VariablesGlobales.lapinsVenduCoop != 0){pointLapinsVendusCoop = (int)(((float)(fermier.getStatistique().getLapinsVenduCoop() * 100 / VariablesGlobales.lapinsVenduCoop) / 100) * (nbJ * VariablesGlobales.COEF_LAPINS));}
             
            if(VariablesGlobales.laitVendu != 0){pointVenteLait = (int)(((float)(fermier.getStatistique().getLaitVendu() * 100 / VariablesGlobales.laitVendu) / 100) * (nbJ * VariablesGlobales.COEF_LAIT));}
            
            if(VariablesGlobales.achatMarche != 0){pointAchatsMarche = (int)(((float)(fermier.getStatistique().getAchatMarche() * 100 / VariablesGlobales.achatMarche) / 100) * (nbJ * VariablesGlobales.COEF_ACHAT_MARCHE));}

            if(VariablesGlobales.venteMarche != 0){pointVentesMarche = (int)(((float)(fermier.getStatistique().getVenteMarche() * 100 / VariablesGlobales.venteMarche) / 100) * (nbJ * VariablesGlobales.COEF_VENTE_MARCHE));}

            fermier.getStatistique().setPointEcus(pointEcus);
            fermier.getStatistique().setPointProd(pointOeufsVendus + pointLapinsVendusCoop + pointVenteLait);
            fermier.getStatistique().setPointNego(pointAchatsMarche + pointVentesMarche);
            fermier.getStatistique().setPointGlobal();

            fermierRepository.save(fermier);
        }
        return fermiers;
    }

    @Transactional
    public List<Fermier> triParEcus(){
        List<Fermier> classement = new ArrayList<>();
        List<Fermier> fermiers = fermierRepository.findAll();

        for(Fermier fermier : fermiers){
            if(classement.size() == 0){
                classement.add(fermier);
            }
            else{
                for(int i = 0; i < classement.size(); i++){
                    if(fermier.getStatistique().getPointEcus() >= classement.get(i).getStatistique().getPointEcus()){
                        classement.add(i, fermier);
                        i = classement.size() - 1;
                    }
                    else{
                        if(i == classement.size() - 1){
                            classement.add(classement.size(), fermier);
                            i = classement.size() - 1;
                        }   
                    }
                }
            }
            fermierRepository.save(fermier);
        }
        return classement;
    }

    @Transactional
    public List<Fermier> triParProd(){
        List<Fermier> classement = new ArrayList<>();
        List<Fermier> fermiers = fermierRepository.findAll();

        for(Fermier fermier : fermiers){
            if(classement.size() == 0){
                classement.add(fermier);
            }
            else{
                for(int i = 0; i < classement.size(); i++){
                    if(fermier.getStatistique().getPointProd() >= classement.get(i).getStatistique().getPointProd()){
                        classement.add(i, fermier);
                        i = classement.size() - 1;
                    }
                    else{
                        if(i == classement.size() - 1){
                            classement.add(classement.size(), fermier);
                            i = classement.size() - 1;
                        }   
                    }
                }
            }
            fermierRepository.save(fermier);
        }
        return classement;
    }

    @Transactional
    public List<Fermier> triParNego(){
        List<Fermier> classement = new ArrayList<>();
        List<Fermier> fermiers = fermierRepository.findAll();

        for(Fermier fermier : fermiers){
            if(classement.size() == 0){
                classement.add(fermier);
            }
            else{
                for(int i = 0; i < classement.size(); i++){
                    if(fermier.getStatistique().getPointNego() >= classement.get(i).getStatistique().getPointNego()){
                        classement.add(i, fermier);
                        i = classement.size() - 1;
                    }
                    else{
                        if(i == classement.size() - 1){
                            classement.add(classement.size(), fermier);
                            i = classement.size() - 1;
                        }   
                    }
                }
            }
            fermierRepository.save(fermier);
        }
        return classement;
    }

    @Transactional
    public List<Fermier> triParGlobal(){
        List<Fermier> classement = new ArrayList<>();
        List<Fermier> fermiers = fermierRepository.findAll();

        for(Fermier fermier : fermiers){
            if(classement.size() == 0){
                classement.add(fermier);
            }
            else{
                for(int i = 0; i < classement.size(); i++){
                    if(fermier.getStatistique().getPointGlobal() >= classement.get(i).getStatistique().getPointGlobal()){
                        classement.add(i, fermier);
                        i = classement.size() - 1;
                    }
                    else{
                        if(i == classement.size() - 1){
                            classement.add(classement.size(), fermier);
                            i = classement.size() - 1;
                        }   
                    }
                }
            }
            fermierRepository.save(fermier);
        }
        return classement;
    }

    public void addVenteMarche(String utilisateurName, int n){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        fermier.getStatistique().addVenteMarche(n);
        fermierRepository.save(fermier);
    }
}