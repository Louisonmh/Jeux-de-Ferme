package fr.devweb.projet484i.service;

import fr.devweb.projet484i.entity.Poule;
import fr.devweb.projet484i.entity.Coq;
import fr.devweb.projet484i.entity.Fermier;
import fr.devweb.projet484i.repository.VacheRepository;
import org.springframework.stereotype.Service;
import fr.devweb.projet484i.service.FermierService;
import fr.devweb.projet484i.repository.FermierRepository;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

import java.util.Optional;
import jakarta.transaction.Transactional;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.sql.Timestamp;

import fr.devweb.projet484i.VariablesGlobales;

@Service
public class PouleService{
    private final FermierService fermierService;
    private final FermierRepository fermierRepository;

    public PouleService(FermierService fermierService, FermierRepository fermierRepository) {
        this.fermierService = fermierService;
        this.fermierRepository = fermierRepository;
    }

    @Transactional
    public List<Poule> getPoulesOfUser(String utilisateurName) {
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        return fermier.getPoules();
    }

    @Transactional
    public Poule addPouleToFermier(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);

        Poule poule = new Poule(VariablesGlobales.AGE_POULE, VariablesGlobales.POIDS_POULE);
        fermier.addPoule(poule);
        
        fermierRepository.save(fermier);
        return poule;
    }

    @Transactional
    public List<Poule> add3PouleToFermier(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();
        while(poules.size() != 0){
            poules.remove(0);
        }
        for(int i = 0; i < 3; i++){
            Poule poule = new Poule(VariablesGlobales.AGE_POULE, VariablesGlobales.POIDS_POULE);
            fermier.addPoule(poule);
        }
        
        fermierRepository.save(fermier);
        return poules;
    }

    @Transactional
    public List<Poule> addNPoulesOfUtilisateur(String utilisateurName, int n){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();
        for(int i = 0; i < n; i++){
            if(poules.size() + fermier.getCoqs().size() + fermier.getPoussins().size() >= VariablesGlobales.NB_VOLAILLES_MAX){
                break;
            }
            Poule poule = new Poule(VariablesGlobales.AGE_POULE, VariablesGlobales.POIDS_POULE);
            fermier.addPoule(poule);
        }
        
        fermierRepository.save(fermier);
        return poules;
    }

    @Transactional
    public Poule nourrirPouleOfUtilisateur(String utilisateurName, Long id){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();
        Poule poule = poules.get(0);
        for(Poule p : poules){
            if(p.getId().equals(id)){
                poule = p;
                poule.nourrir();
            }
        }
        fermierRepository.save(fermier);
        return poule;
    }

    @Transactional
    public List<Poule> nourrirAllOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();

        for(Poule poule : poules){
            poule.nourrir();
        }
        fermierRepository.save(fermier);
        return poules;
    }

    @Transactional
    public List<Poule> nourrirAllSacNourritureOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();
        if(poules.get(0).getUtilisateur().getRemise().getSac_nourriture() > 0){
            for(Poule poule : poules){
                poule.nourrirSacNourriture();
            }
            poules.get(0).getUtilisateur().getRemise().decSacsNourriture();
        }
        
        fermierRepository.save(fermier);
        return poules;
    }

    @Transactional
    public Poule abreuvePouleOfUtilisateur(String utilisateurName, Long id){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();
        Poule poule = poules.get(0);
        for(Poule p : poules){
            if(p.getId().equals(id)){
                poule = p;
                poule.abreuve();
            }
        }
        fermierRepository.save(fermier);
        return poule;
    }

    @Transactional
    public List<Poule> abreuveAllOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();

        for(Poule poule : poules){
            poule.abreuve();
        }
        fermierRepository.save(fermier);
        return poules;
    }

    @Transactional
    public List<Poule> abreuveAllSeauDeauOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();
        if(poules.get(0).getUtilisateur().getRemise().getEau() > 0){
            for(Poule poule : poules){
                poule.abreuveSeauDeau();
            }
            poules.get(0).getUtilisateur().getRemise().decEau();
        }
        
        fermierRepository.save(fermier);
        return poules;
    }

    @Transactional
    public List<Poule> affamerOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();

        for(Poule poule : poules){
            poule.affamerPoule();
        }
        fermierRepository.save(fermier);
        return poules;
    }

    @Transactional
    public List<Poule> affamer2OfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();

        for(Poule poule : poules){
            poule.affamerPoule2();
        }
        fermierRepository.save(fermier);
        return poules;
    }

    @Transactional
    public List<Poule> affamer3OfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();

        for(Poule poule : poules){
            poule.affamerPoule3();
        }
        fermierRepository.save(fermier);
        return poules;
    }

    @Transactional
    public List<Poule> affamer4OfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();

        for(Poule poule : poules){
            poule.affamerPoule4();
        }
        fermierRepository.save(fermier);
        return poules;
    }

    @Transactional
    public List<Poule> assoifferOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();

        for(Poule poule : poules){
            poule.assoifferPoule();
        }
        fermierRepository.save(fermier);
        return poules;
    }

    @Transactional
    public List<Poule> abreuverOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();

        for(Poule poule : poules){
            poule.abreuve();
        }
        fermierRepository.save(fermier);
        return poules;
    }

    @Transactional
    public List<Poule> abreuver2OfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();

        for(Poule poule : poules){
            poule.abreuver();
        }
        fermierRepository.save(fermier);
        return poules;
    }

    @Transactional
    public List<Poule> salirOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();

        for(Poule poule : poules){
            poule.salePoule();
        }
        fermierRepository.save(fermier);
        return poules;
    }

    @Transactional
    public Poule nettoyerPouleOfUtilisateur(String utilisateurName, Long id){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();
        Poule poule = poules.get(0);
        for(Poule p : poules){
            if(p.getId().equals(id)){
                poule = p;
                poule.nettoyer();
            }
        }
        fermierRepository.save(fermier);
        return poule;
    }

    @Transactional
    public List<Poule> nettoyerAllOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();

        for(Poule poule : poules){
            poule.nettoyer();
        }
        fermierRepository.save(fermier);
        return poules;
    }

    @Transactional
    public List<Poule> nettoyerAllSavonOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();
        if(poules.get(0).getUtilisateur().getRemise().getSavon() > 0){
            for(Poule poule : poules){
                poule.nettoyerSavon();
            }
            poules.get(0).getUtilisateur().getRemise().decSavons();
        }
        
        fermierRepository.save(fermier);
        return poules;
    }

    @Transactional
    public List<Poule> maladeOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();

        for(Poule poule : poules){
            poule.maladePoule();
        }
        fermierRepository.save(fermier);
        return poules;
    }

    @Transactional
    public List<Poule> malade4OfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();

        for(Poule poule : poules){
            poule.maladePoule4();
        }
        fermierRepository.save(fermier);
        return poules;
    }

    @Transactional
    public Poule soignerPouleOfUtilisateur(String utilisateurName, Long id){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();
        Poule poule = poules.get(0);
        for(Poule p : poules){
            if(p.getId().equals(id)){
                poule = p;
                poule.soigner();
            }
        }
        fermierRepository.save(fermier);
        return poule;
    }

    @Transactional
    public List<Poule> soignerAllOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();

        for(Poule poule : poules){
            poule.soigner();
        }
        fermierRepository.save(fermier);
        return poules;
    }

    @Transactional
    public List<Poule> soignerAllSeringueOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();
        if(poules.get(0).getUtilisateur().getRemise().getSeringue() > 0){
            for(Poule poule : poules){
                poule.soignerSeringue();
            }
            poules.get(0).getUtilisateur().getRemise().decSeringues();
        }
        
        fermierRepository.save(fermier);
        return poules;
    }

    @Transactional
    public List<Poule> couverOfUtilisateur(String utilisateurName, int nbo){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();

        int i = 0;
        // limite le nombre de couvaison pour ne pas depasser les 60 volaille le lendemain
        int nbVolaille = poules.size() + fermier.getCoqs().size() + fermier.getPoussins().size();
        nbo = Math.min(nbo, (60 - nbVolaille));
        while(i < poules.size() && nbo != 0){
            if(!poules.get(i).isEnCouvaison()){
                poules.get(i).couver();
                nbo--;
            }
            i++;
        }
        fermierRepository.save(fermier);
        return poules;
    }

    @Transactional
    public List<Poule> couvaisonOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();
        
        for(Poule poule : poules){
            poule.couvaison();
        }
        fermierRepository.save(fermier);
        return poules;
    }

    @Transactional
    public List<Poule> arreterCouverOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();
        
        for(Poule poule : poules){
            poule.arreterCouver();
        }
        fermierRepository.save(fermier);
        return poules;
    }

    @Transactional
    public List<Poule> pondreOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();
        List<Coq> coqs = fermier.getCoqs();
        int pouleFeconder = 0;
        for(Coq coq : coqs){
            if(coq.estNourrie() && coq.estPropre() && coq.estSain() && coq.estAdulte()){
                pouleFeconder += 5;
            }
        }
        int i = 0;
        while(i < poules.size() && pouleFeconder != 0){
            if(poules.get(i).pondre()){
                pouleFeconder--;
            }
            i++;
        }
        fermierRepository.save(fermier);
        return poules;
    }

    @Transactional
    public List<Poule> famineOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();

        for(int i = 0; i < poules.size(); i++){
            if(poules.get(i).famine()){
                i--;
            }
        }
        fermierRepository.save(fermier);
        return poules;
    }

    @Transactional
    public List<Poule> tuerOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();

        for(int i = 0; i < poules.size(); i++){
            if(poules.get(i).tuer()){
                i--;
            }
        }
        fermierRepository.save(fermier);
        return poules;
    }

    @Transactional
    public List<Poule> maigrirOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();

        for(Poule poule : poules){
            poule.maigrir();
        }
        fermierRepository.save(fermier);
        return poules;
    }

    @Transactional
    public List<Poule> regressionOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();

        for(int i = 0; i < poules.size(); i++){
            if(poules.get(i).regression()){
                i--;
            }
        }
        fermierRepository.save(fermier);
        return poules;
    }

    @Transactional
    public List<Poule> enfantOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();

        for(Poule poule : poules){
            poule.enfant();
        }
        fermierRepository.save(fermier);
        return poules;
    }

    @Transactional
    public List<Poule> passageJourOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();
        List<Coq> coqs = fermier.getCoqs();

        poules.get(0).getUtilisateur().getRemise().setOeuf(0);

        int pouleFeconder = 0;
        for(Coq coq : coqs){
            if(coq.estNourrie() && coq.estPropre() && coq.estSain() && coq.estAdulte()){
                pouleFeconder += 5;
            }
        }
        
        for(int i = 0; i < poules.size(); i++){
            if(poules.get(i).famine()){ // si true alors la poule est supprimer et la boucle de passage ne doit pas avancer
                i--;
            }
            else if(poules.get(i).regression()){
                i--;
            }
            else if(poules.get(i).tuer()){
                i--;
            }
            else{
                if(pouleFeconder != 0){
                    if(poules.get(i).pondre()){
                        pouleFeconder--;
                    }
                }
                Random r = new Random();
                if(r.nextInt(100) < VariablesGlobales.POURCENTAGE_MALADE_POULE){
                    poules.get(i).setMalade(new Timestamp(System.currentTimeMillis()));
                }
                if(r.nextInt(100) < VariablesGlobales.POURCENTAGE_SALE_POULE){
                    poules.get(i).setSale(new Timestamp(System.currentTimeMillis()));
                }
                poules.get(i).incAge();
            }
        }
        
        fermierRepository.save(fermier);
        return poules;
    }
    
    @Transactional
    public List<Poule> nourrirHierPouleOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();
        for(Poule poule : poules){
            poule.nourrirHier();
        }
        fermierRepository.save(fermier);
        return poules;
    }

    @Transactional
    public List<Poule> abreuveHierPouleOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poule> poules = fermier.getPoules();
        for(Poule poule : poules){
            poule.abreuveHier();
        }
        fermierRepository.save(fermier);
        return poules;
    }
}