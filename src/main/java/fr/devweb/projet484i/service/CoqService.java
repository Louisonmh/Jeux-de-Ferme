package fr.devweb.projet484i.service;

import fr.devweb.projet484i.entity.Coq;
import fr.devweb.projet484i.entity.Fermier;
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
public class CoqService{
    private final FermierService fermierService;
    private final FermierRepository fermierRepository;

    public CoqService(FermierService fermierService, FermierRepository fermierRepository) {
        this.fermierService = fermierService;
        this.fermierRepository = fermierRepository;
    }

    @Transactional
    public List<Coq> getCoqsOfUser(String utilisateurName) {
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        return fermier.getCoqs();
    }

    @Transactional
    public Coq addCoqToFermier(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);

        Coq coq = new Coq(VariablesGlobales.AGE_COQ, VariablesGlobales.POIDS_COQ);
        fermier.addCoq(coq);
        
        fermierRepository.save(fermier);
        return coq;
    }

    @Transactional
    public List<Coq> add1CoqToFermier(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Coq> coqs = fermier.getCoqs();
        while(coqs.size() != 0){
            coqs.remove(0);
        }
        for(int i = 0; i < 1; i++){
            Coq coq = new Coq(VariablesGlobales.AGE_COQ, VariablesGlobales.POIDS_COQ);
            fermier.addCoq(coq);
        }
        
        fermierRepository.save(fermier);
        return coqs;
    }

    @Transactional
    public List<Coq> addNCoqsOfUtilisateur(String utilisateurName, int n){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Coq> coqs = fermier.getCoqs();
        for(int i = 0; i < n; i++){
            if(coqs.size() + fermier.getPoules().size() + fermier.getPoussins().size() >= VariablesGlobales.NB_VOLAILLES_MAX){
                break;
            }
            Coq coq = new Coq(VariablesGlobales.AGE_COQ, VariablesGlobales.POIDS_COQ);
            fermier.addCoq(coq);
        }
        
        fermierRepository.save(fermier);
        return coqs;
    }

    @Transactional
    public Coq nourrirCoqOfUtilisateur(String utilisateurName, Long id){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Coq> coqs = fermier.getCoqs();
        Coq coq = coqs.get(0);
        for(Coq c : coqs){
            if(c.getId().equals(id)){
                coq = c;
                coq.nourrir();
            }
        }
        fermierRepository.save(fermier);
        return coq;
    }

    @Transactional
    public List<Coq> nourrirAllOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Coq> coqs = fermier.getCoqs();

        for(Coq coq : coqs){
            coq.nourrir();
        }
        fermierRepository.save(fermier);
        return coqs;
    }

    @Transactional
    public List<Coq> nourrirAllSacNourritureOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Coq> coqs = fermier.getCoqs();
        if(coqs.get(0).getUtilisateur().getRemise().getSac_nourriture() > 0){
            for(Coq coq : coqs){
                coq.nourrirSacNourriture();
            }
            coqs.get(0).getUtilisateur().getRemise().decSacsNourriture();
        }
        
        fermierRepository.save(fermier);
        return coqs;
    }

    @Transactional
    public Coq abreuveCoqOfUtilisateur(String utilisateurName, Long id){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Coq> coqs = fermier.getCoqs();
        Coq coq = coqs.get(0);
        for(Coq c : coqs){
            if(c.getId().equals(id)){
                coq = c;
                coq.abreuve();
            }
        }
        fermierRepository.save(fermier);
        return coq;
    }

    @Transactional
    public List<Coq> abreuveAllOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Coq> coqs = fermier.getCoqs();

        for(Coq coq : coqs){
            coq.abreuve();
        }
        fermierRepository.save(fermier);
        return coqs;
    }

    @Transactional
    public List<Coq> abreuveAllSeauDeauOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Coq> coqs = fermier.getCoqs();
        if(coqs.get(0).getUtilisateur().getRemise().getEau() > 0){
            for(Coq coq : coqs){
                coq.abreuveSeauDeau();
            }
            coqs.get(0).getUtilisateur().getRemise().decEau();
        }
        
        fermierRepository.save(fermier);
        return coqs;
    }

    @Transactional
    public List<Coq> affamerOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Coq> coqs = fermier.getCoqs();

        for(Coq coq : coqs){
            coq.affamerCoq();
        }
        fermierRepository.save(fermier);
        return coqs;
    }

    @Transactional
    public List<Coq> affamer2OfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Coq> coqs = fermier.getCoqs();

        for(Coq coq : coqs){
            coq.affamerCoq2();
        }
        fermierRepository.save(fermier);
        return coqs;
    }

    @Transactional
    public List<Coq> affamer3OfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Coq> coqs = fermier.getCoqs();

        for(Coq coq : coqs){
            coq.affamerCoq3();
        }
        fermierRepository.save(fermier);
        return coqs;
    }

    @Transactional
    public List<Coq> affamer4OfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Coq> coqs = fermier.getCoqs();

        for(Coq coq : coqs){
            coq.affamerCoq4();
        }
        fermierRepository.save(fermier);
        return coqs;
    }

    @Transactional
    public List<Coq> assoifferOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Coq> coqs = fermier.getCoqs();

        for(Coq coq : coqs){
            coq.assoifferCoq();
        }
        fermierRepository.save(fermier);
        return coqs;
    }

    @Transactional
    public List<Coq> abreuverOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Coq> coqs = fermier.getCoqs();

        for(Coq coq : coqs){
            coq.abreuve();
        }
        fermierRepository.save(fermier);
        return coqs;
    }

    @Transactional
    public List<Coq> salirOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Coq> coqs = fermier.getCoqs();

        for(Coq coq : coqs){
            coq.saleCoq();
        }
        fermierRepository.save(fermier);
        return coqs;
    }

    @Transactional
    public Coq nettoyerCoqOfUtilisateur(String utilisateurName, Long id){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Coq> coqs = fermier.getCoqs();
        Coq coq = coqs.get(0);
        for(Coq c : coqs){
            if(c.getId().equals(id)){
                coq = c;
                coq.nettoyer();
            }
        }
        fermierRepository.save(fermier);
        return coq;
    }

    @Transactional
    public List<Coq> nettoyerAllOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Coq> coqs = fermier.getCoqs();

        for(Coq coq : coqs){
            coq.nettoyer();
        }
        fermierRepository.save(fermier);
        return coqs;
    }

    @Transactional
    public List<Coq> nettoyerAllSavonOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Coq> coqs = fermier.getCoqs();
        if(coqs.get(0).getUtilisateur().getRemise().getSavon() > 0){
            for(Coq coq : coqs){
                coq.nettoyerSavon();
            }
            coqs.get(0).getUtilisateur().getRemise().decSavons();
        }
        
        fermierRepository.save(fermier);
        return coqs;
    }

    @Transactional
    public List<Coq> maladeOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Coq> coqs = fermier.getCoqs();

        for(Coq coq : coqs){
            coq.maladeCoq();
        }
        fermierRepository.save(fermier);
        return coqs;
    }

    @Transactional
    public List<Coq> malade4OfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Coq> coqs = fermier.getCoqs();

        for(Coq coq : coqs){
            coq.maladeCoq4();
        }
        fermierRepository.save(fermier);
        return coqs;
    }

    @Transactional
    public Coq soignerCoqOfUtilisateur(String utilisateurName, Long id){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Coq> coqs = fermier.getCoqs();
        Coq coq = coqs.get(0);
        for(Coq c : coqs){
            if(c.getId().equals(id)){
                coq = c;
                coq.soigner();
            }
        }
        fermierRepository.save(fermier);
        return coq;
    }

    @Transactional
    public List<Coq> soignerAllOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Coq> coqs = fermier.getCoqs();

        for(Coq coq : coqs){
            coq.soigner();
        }
        fermierRepository.save(fermier);
        return coqs;
    }

    @Transactional
    public List<Coq> soignerAllSeringueOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Coq> coqs = fermier.getCoqs();
        if(coqs.get(0).getUtilisateur().getRemise().getSeringue() > 0){
            for(Coq coq : coqs){
                coq.soignerSeringue();
            }
            coqs.get(0).getUtilisateur().getRemise().decSeringues();
        }
        
        fermierRepository.save(fermier);
        return coqs;
    }

    @Transactional
    public List<Coq> famineOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Coq> coqs = fermier.getCoqs();

        for(int i = 0; i < coqs.size(); i++){
            if(coqs.get(i).famine()){
                i--;
            }
        }
        fermierRepository.save(fermier);
        return coqs;
    }

    @Transactional
    public List<Coq> tuerOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Coq> coqs = fermier.getCoqs();

        for(int i = 0; i < coqs.size(); i++){
            if(coqs.get(i).tuer()){
                i--;
            }
        }
        fermierRepository.save(fermier);
        return coqs;
    }

    @Transactional
    public List<Coq> maigrirOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Coq> coqs = fermier.getCoqs();

        for(Coq coq : coqs){
            coq.maigrir();
        }
        fermierRepository.save(fermier);
        return coqs;
    }

    @Transactional
    public List<Coq> regressionOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Coq> coqs = fermier.getCoqs();

        for(int i = 0; i < coqs.size(); i++){
            if(coqs.get(i).regression()){
                i--;
            }
        }
        fermierRepository.save(fermier);
        return coqs;
    }

    @Transactional
    public List<Coq> enfantOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Coq> coqs = fermier.getCoqs();

        for(Coq coq : coqs){
            coq.enfant();
        }
        fermierRepository.save(fermier);
        return coqs;
    }

    @Transactional
    public List<Coq> nourrirHierAllOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Coq> coqs = fermier.getCoqs();

        for(Coq coq : coqs){
            coq.nourrirHier();
        }
        fermierRepository.save(fermier);
        return coqs;
    }

    @Transactional
    public List<Coq> abreuveHierAllOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Coq> coqs = fermier.getCoqs();

        for(Coq coq : coqs){
            coq.abreuveHier();
        }
        fermierRepository.save(fermier);
        return coqs;
    }

    @Transactional
    public List<Coq> passageJourOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Coq> coqs = fermier.getCoqs();
        
        for(int i = 0; i < coqs.size(); i++){
            if(coqs.get(i).famine()){ // si true alors la poule est supprimer et la boucle de passage ne doit pas avancer
                i--;
            }
            else if(coqs.get(i).regression()){
                i--;
            }
            else if(coqs.get(i).tuer()){
                i--;
            }
            else{
                Random r = new Random();
                if(r.nextInt(100) < VariablesGlobales.POURCENTAGE_MALADE_COQ){
                    coqs.get(i).setMalade(new Timestamp(System.currentTimeMillis()));
                }
                if(r.nextInt(100) < VariablesGlobales.POURCENTAGE_SALE_COQ){
                    coqs.get(i).setSale(new Timestamp(System.currentTimeMillis()));
                }
                coqs.get(i).incAge();
            }
        }
        
        fermierRepository.save(fermier);
        return coqs;
    }
}