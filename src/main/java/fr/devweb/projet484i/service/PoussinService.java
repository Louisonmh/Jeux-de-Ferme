package fr.devweb.projet484i.service;

import fr.devweb.projet484i.entity.Poussin;
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
public class PoussinService{
    private final FermierService fermierService;
    private final FermierRepository fermierRepository;

    public PoussinService(FermierService fermierService, FermierRepository fermierRepository) {
        this.fermierService = fermierService;
        this.fermierRepository = fermierRepository;
    }

    @Transactional
    public List<Poussin> getPoussinsOfUser(String utilisateurName) {
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        return fermier.getPoussins();
    }

    @Transactional
    public Poussin addPoussinToFermier(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);

        Poussin poussin = new Poussin(VariablesGlobales.AGE_POUSSIN, VariablesGlobales.POIDS_POUSSIN);
        fermier.addPoussin(poussin);
        
        fermierRepository.save(fermier);
        return poussin;
    }

    @Transactional
    public List<Poussin> add3PoussinToFermier(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poussin> poussins = fermier.getPoussins();
        while(poussins.size() != 0){
            poussins.remove(0);
        }
        for(int i = 0; i < 3; i++){
            Poussin poussin = new Poussin(VariablesGlobales.AGE_POUSSIN, VariablesGlobales.POIDS_POUSSIN);
            fermier.addPoussin(poussin);
        }
        
        fermierRepository.save(fermier);
        return poussins;
    }

    @Transactional
    public Poussin nourrirPoussinOfUtilisateur(String utilisateurName, Long id){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poussin> poussins = fermier.getPoussins();
        Poussin poussin = poussins.get(0);
        for(Poussin p : poussins){
            if(p.getId().equals(id)){
                poussin = p;
                poussin.nourrir();
            }
        }
        fermierRepository.save(fermier);
        return poussin;
    }

    @Transactional
    public List<Poussin> nourrirAllOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poussin> poussins = fermier.getPoussins();

        for(Poussin poussin : poussins){
            poussin.nourrir();
        }
        fermierRepository.save(fermier);
        return poussins;
    }

    @Transactional
    public List<Poussin> nourrirAllSacNourritureOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poussin> poussins = fermier.getPoussins();
        if(poussins.get(0).getUtilisateur().getRemise().getSac_nourriture() > 0){
            for(Poussin poussin : poussins){
                poussin.nourrirSacNourriture();
            }
            poussins.get(0).getUtilisateur().getRemise().decSacsNourriture();
        }
        
        fermierRepository.save(fermier);
        return poussins;
    }

    @Transactional
    public Poussin abreuvePoussinOfUtilisateur(String utilisateurName, Long id){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poussin> poussins = fermier.getPoussins();
        Poussin poussin = poussins.get(0);
        for(Poussin p : poussins){
            if(p.getId().equals(id)){
                poussin = p;
                poussin.abreuve();
            }
        }
        fermierRepository.save(fermier);
        return poussin;
    }

    @Transactional
    public List<Poussin> abreuveAllOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poussin> poussins = fermier.getPoussins();

        for(Poussin poussin : poussins){
            poussin.abreuve();
        }
        fermierRepository.save(fermier);
        return poussins;
    }

    @Transactional
    public List<Poussin> abreuveAllSeauDeauOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poussin> poussins = fermier.getPoussins();
        if(poussins.get(0).getUtilisateur().getRemise().getEau() > 0){
            for(Poussin poussin : poussins){
                poussin.abreuveSeauDeau();
            }
            poussins.get(0).getUtilisateur().getRemise().decEau();
        }

        fermierRepository.save(fermier);
        return poussins;
    }

    @Transactional
    public List<Poussin> affamerOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poussin> poussins = fermier.getPoussins();

        for(Poussin poussin : poussins){
            poussin.affamerPoussin();
        }
        fermierRepository.save(fermier);
        return poussins;
    }

    @Transactional
    public List<Poussin> affamer2OfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poussin> poussins = fermier.getPoussins();

        for(Poussin poussin : poussins){
            poussin.affamerPoussin2();
        }
        fermierRepository.save(fermier);
        return poussins;
    }

    @Transactional
    public List<Poussin> affamer3OfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poussin> poussins = fermier.getPoussins();

        for(Poussin poussin : poussins){
            poussin.affamerPoussin3();
        }
        fermierRepository.save(fermier);
        return poussins;
    }

    @Transactional
    public List<Poussin> affamer4OfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poussin> poussins = fermier.getPoussins();

        for(Poussin poussin : poussins){
            poussin.affamerPoussin4();
        }
        fermierRepository.save(fermier);
        return poussins;
    }

    @Transactional
    public List<Poussin> assoifferOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poussin> poussins = fermier.getPoussins();

        for(Poussin poussin : poussins){
            poussin.assoifferPoussin();
        }
        fermierRepository.save(fermier);
        return poussins;
    }

    @Transactional
    public List<Poussin> abreuverOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poussin> poussins = fermier.getPoussins();

        for(Poussin poussin : poussins){
            poussin.abreuve();
        }
        fermierRepository.save(fermier);
        return poussins;
    }

    @Transactional
    public List<Poussin> salirOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poussin> poussins = fermier.getPoussins();

        for(Poussin poussin : poussins){
            poussin.salePoussin();
        }
        fermierRepository.save(fermier);
        return poussins;
    }

    @Transactional
    public Poussin nettoyerPoussinOfUtilisateur(String utilisateurName, Long id){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poussin> poussins = fermier.getPoussins();
        Poussin poussin = poussins.get(0);
        for(Poussin p : poussins){
            if(p.getId().equals(id)){
                poussin = p;
                poussin.nettoyer();
            }
        }
        fermierRepository.save(fermier);
        return poussin;
    }

    @Transactional
    public List<Poussin> nettoyerAllOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poussin> poussins = fermier.getPoussins();

        for(Poussin poussin : poussins){
            poussin.nettoyer();
        }
        fermierRepository.save(fermier);
        return poussins;
    }

    @Transactional
    public List<Poussin> nettoyerAllSavonOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poussin> poussins = fermier.getPoussins();

        if(poussins.get(0).getUtilisateur().getRemise().getSavon() > 0){
            for(Poussin poussin : poussins){
                poussin.nettoyerSavon();
            }
            poussins.get(0).getUtilisateur().getRemise().decSavons();
        }
        
        fermierRepository.save(fermier);
        return poussins;
    }

    @Transactional
    public List<Poussin> maladeOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poussin> poussins = fermier.getPoussins();

        for(Poussin poussin : poussins){
            poussin.maladePoussin();
        }
        fermierRepository.save(fermier);
        return poussins;
    }

    @Transactional
    public List<Poussin> malade4OfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poussin> poussins = fermier.getPoussins();

        for(Poussin poussin : poussins){
            poussin.maladePoussin4();
        }
        fermierRepository.save(fermier);
        return poussins;
    }

    @Transactional
    public Poussin soignerPoussinOfUtilisateur(String utilisateurName, Long id){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poussin> poussins = fermier.getPoussins();
        Poussin poussin = poussins.get(0);
        for(Poussin p : poussins){
            if(p.getId().equals(id)){
                poussin = p;
                poussin.soigner();
            }
        }
        fermierRepository.save(fermier);
        return poussin;
    }

    @Transactional
    public List<Poussin> soignerAllOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poussin> poussins = fermier.getPoussins();

        for(Poussin poussin : poussins){
            poussin.soigner();
        }
        fermierRepository.save(fermier);
        return poussins;
    }

    @Transactional
    public List<Poussin> soignerAllSeringueOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poussin> poussins = fermier.getPoussins();
        if(poussins.get(0).getUtilisateur().getRemise().getSeringue() > 0){
            for(Poussin poussin : poussins){
                poussin.soignerSeringue();
            }
            poussins.get(0).getUtilisateur().getRemise().decSeringues();
        }
        
        fermierRepository.save(fermier);
        return poussins;
    }

    @Transactional
    public List<Poussin> famineOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poussin> poussins = fermier.getPoussins();

        for(int i = 0; i < poussins.size(); i++){
            if(poussins.get(i).famine()){
                i--;
            }
        }
        fermierRepository.save(fermier);
        return poussins;
    }

    @Transactional
    public List<Poussin> tuerOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poussin> poussins = fermier.getPoussins();

        for(int i = 0; i < poussins.size(); i++){
            if(poussins.get(i).tuer()){
                i--;
            }
        }
        fermierRepository.save(fermier);
        return poussins;
    }

    @Transactional
    public List<Poussin> maigrirOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poussin> poussins = fermier.getPoussins();

        for(Poussin poussin : poussins){
            poussin.maigrir();
        }
        fermierRepository.save(fermier);
        return poussins;
    }

    @Transactional
    public List<Poussin> grandirOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poussin> poussins = fermier.getPoussins();
        for(int i = 0; i < poussins.size(); i++){
            if(poussins.get(i).grandir()){
                i--;
            }
        }
        fermierRepository.save(fermier);
        return poussins;
    }

    @Transactional
    public List<Poussin> adultesOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poussin> poussins = fermier.getPoussins();

        for(Poussin poussin : poussins){
            poussin.adultes();
        }
        fermierRepository.save(fermier);
        return poussins;
    }

    @Transactional
    public List<Poussin> nourrirHierAllOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poussin> poussins = fermier.getPoussins();

        for(Poussin poussin : poussins){
            poussin.nourrirHier();
        }
        fermierRepository.save(fermier);
        return poussins;
    }

    @Transactional
    public List<Poussin> abreuveHierAllOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poussin> poussins = fermier.getPoussins();

        for(Poussin poussin : poussins){
            poussin.abreuveHier();
        }
        fermierRepository.save(fermier);
        return poussins;
    }

    @Transactional
    public List<Poussin> passageJourOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        List<Poussin> poussins = fermier.getPoussins();
        
        for(int i = 0; i < poussins.size(); i++){
            if(poussins.get(i).famine()){ // si true alors le poussin est supprimer et la boucle de passage ne doit pas avancer
                i--;
            }
            else if(poussins.get(i).grandir()){
                i--;
            }
            else if(poussins.get(i).tuer()){
                i--;
            }
            else{
                Random r = new Random();
                if(r.nextInt(100) < VariablesGlobales.POURCENTAGE_MALADE_POUSSIN){
                    poussins.get(i).setMalade(new Timestamp(System.currentTimeMillis()));
                }
                if(r.nextInt(100) < VariablesGlobales.POURCENTAGE_SALE_POUSSIN){
                    poussins.get(i).setSale(new Timestamp(System.currentTimeMillis()));
                }
                poussins.get(i).incAge();
            }
        }
        
        fermierRepository.save(fermier);
        return poussins;
    }
}