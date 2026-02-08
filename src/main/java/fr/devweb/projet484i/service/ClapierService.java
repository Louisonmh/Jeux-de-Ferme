package fr.devweb.projet484i.service;

import fr.devweb.projet484i.entity.Clapier;
import fr.devweb.projet484i.entity.Fermier;
import fr.devweb.projet484i.repository.ClapierRepository;
import org.springframework.stereotype.Service;
import fr.devweb.projet484i.service.FermierService;

import java.util.Optional;
import jakarta.transaction.Transactional;

@Service
public class ClapierService{
    private final FermierService fermierService;
    private final ClapierRepository clapierRepository;

    public ClapierService(FermierService fermierService, ClapierRepository clapierRepository) {
        this.fermierService = fermierService;
        this.clapierRepository = clapierRepository;
    }

    @Transactional
    public Clapier affamerAdultesOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.affamerAdultes();
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier nourrirAdultesOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.nourrirAdultes();
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier nourrirAdultesSacOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.nourrirAdultesSac();
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier assoifferAdultesOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.assoifferAdultes();
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier abreuveAdultesOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.abreuveAdultes();
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier abreuveAdultesSeauDeauOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.abreuveAdultesSeauDeau();
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier adultesMaladesOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.adultesMalades();
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier soignerAdultesOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.soignerAdultes();
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier soignerAdultesSeringueOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.soignerAdultesSeringue();
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier salirAdultesOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.salirAdultes();
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier nettoyerAdultesOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.nettoyerAdultes();
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier nettoyerAdultesSavonOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.nettoyerAdultesSavon();
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier affamerEnfantsOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.affamerEnfants();
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier nourrirEnfantsOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.nourrirEnfants();
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier nourrirEnfantsSacOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.nourrirEnfantsSac();
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier assoifferEnfantsOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.assoifferEnfants();
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier abreuveEnfantsOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.abreuveEnfants();
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier abreuveEnfantsSeauDeauOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.abreuveEnfantsSeauDeau();
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier enfantsMaladesOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.enfantsMalades();
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier soignerEnfantsOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.soignerEnfants();
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier soignerEnfantsSeringueOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.soignerEnfantsSeringue();
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier salirEnfantsOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.salirEnfants();
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier nettoyerEnfantsOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.nettoyerEnfants();
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier nettoyerEnfantsSavonOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.nettoyerEnfantsSavon();
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier suppAdultesMalesOfUtilisateur(String utilisateurName, int n){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.suppAdultesMales(n);
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier suppAdultesFemellesOfUtilisateur(String utilisateurName, int n){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.suppAdultesFemelles(n);
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier addAdultesMalesOfUtilisateur(String utilisateurName, int n){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.addAdultesMales(n);
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier addAdultesFemellesOfUtilisateur(String utilisateurName, int n){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.addAdultesFemelles(n);
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier suppBebesOfUtilisateur(String utilisateurName, int n){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.suppBebes(n);
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier addBebesOfUtilisateur(String utilisateurName, int n){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.addBebes(n);
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier suppPetitsOfUtilisateur(String utilisateurName, int n){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.suppPetits(n);
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier addPetitsOfUtilisateur(String utilisateurName, int n){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.addPetits(n);
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier suppGrosOfUtilisateur(String utilisateurName, int n){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.suppGros(n);
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier addGrosOfUtilisateur(String utilisateurName, int n){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.addGros(n);
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier remplirOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.remplirClapier();
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier remplirMaxOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.remplirMaxClapier();
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier viderOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.viderClapier();
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier grandirOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.grandir();
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier reproductionOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.reproduction();
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier mortOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.mort();
        clapierRepository.save(clapier);
        return clapier;
    }

    @Transactional
    public Clapier passageJourOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Clapier clapier = fermier.getClapier();

        clapier.passageJour();
        clapierRepository.save(clapier);
        return clapier;
    }
}