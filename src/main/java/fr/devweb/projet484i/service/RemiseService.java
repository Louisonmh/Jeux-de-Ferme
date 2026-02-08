package fr.devweb.projet484i.service;

import fr.devweb.projet484i.entity.Remise;
import fr.devweb.projet484i.entity.Fermier;
import fr.devweb.projet484i.repository.RemiseRepository;
import org.springframework.stereotype.Service;
import fr.devweb.projet484i.service.FermierService;

import java.util.Optional;
import jakarta.transaction.Transactional;

@Service
public class RemiseService{
    private final FermierService fermierService;
    private final RemiseRepository remiseRepository;

    public RemiseService(FermierService fermierService,RemiseRepository remiseRepository) {
        this.fermierService = fermierService;
        this.remiseRepository = remiseRepository;
    }

    @Transactional
    public Remise viderOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Remise remise = fermier.getRemise();

        remise.vider();
        remiseRepository.save(remise);
        return remise;
    }

    @Transactional
    public Remise remplirUnOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Remise remise = fermier.getRemise();

        remise.remplirUn();
        remiseRepository.save(remise);
        return remise;
    }

    @Transactional
    public Remise remplirPlusieursOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Remise remise = fermier.getRemise();

        remise.remplirPlusieurs();
        remiseRepository.save(remise);
        return remise;
    }

    @Transactional
    public Remise incEauOfUtilisateur(String utilisateurName, int n){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Remise remise = fermier.getRemise();

        remise.incEau(n);
        remiseRepository.save(remise);
        return remise;
    }

    @Transactional
    public Remise decEauOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Remise remise = fermier.getRemise();

        remise.decEau();
        remiseRepository.save(remise);
        return remise;
    }

    @Transactional
    public Remise incBottesPailleOfUtilisateur(String utilisateurName, int n){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Remise remise = fermier.getRemise();

        remise.incBottesPaille(n);
        remiseRepository.save(remise);
        return remise;
    }

    @Transactional
    public Remise decBottesPailleOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Remise remise = fermier.getRemise();

        remise.decBottesPaille();
        remiseRepository.save(remise);
        return remise;
    }

    @Transactional
    public Remise incSeringuesOfUtilisateur(String utilisateurName, int n){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Remise remise = fermier.getRemise();

        remise.incSeringues(n);
        remiseRepository.save(remise);
        return remise;
    }

    @Transactional
    public Remise decSeringuesOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Remise remise = fermier.getRemise();

        remise.decSeringues();
        remiseRepository.save(remise);
        return remise;
    }

    @Transactional
    public Remise incSavonsOfUtilisateur(String utilisateurName, int n){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Remise remise = fermier.getRemise();

        remise.incSavons(n);
        remiseRepository.save(remise);
        return remise;
    }

    @Transactional
    public Remise decSavonsOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Remise remise = fermier.getRemise();

        remise.decSavons();
        remiseRepository.save(remise);
        return remise;
    }

    @Transactional
    public Remise incSacsNourritureOfUtilisateur(String utilisateurName, int n){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Remise remise = fermier.getRemise();

        remise.incSacsNourriture(n);
        remiseRepository.save(remise);
        return remise;
    }

    @Transactional
    public Remise decSacsNourritureOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Remise remise = fermier.getRemise();

        remise.decSacsNourriture();
        remiseRepository.save(remise);
        return remise;
    }

    @Transactional
    public Remise incOeufsOfUtilisateur(String utilisateurName, int n){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Remise remise = fermier.getRemise();

        remise.incOeufs(n);
        remiseRepository.save(remise);
        return remise;
    }

    @Transactional
    public Remise decOeufsOfUtilisateur(String utilisateurName, int n){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Remise remise = fermier.getRemise();

        remise.decOeufs(n);
        remiseRepository.save(remise);
        return remise;
    }

    @Transactional
    public Remise incLitresLaitOfUtilisateur(String utilisateurName, int n){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Remise remise = fermier.getRemise();

        remise.incLitresLait(n);
        remiseRepository.save(remise);
        return remise;
    }

    @Transactional
    public Remise decLitresLaitOfUtilisateur(String utilisateurName, int n){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Remise remise = fermier.getRemise();

        remise.decLitresLait(n);
        remiseRepository.save(remise);
        return remise;
    }
}