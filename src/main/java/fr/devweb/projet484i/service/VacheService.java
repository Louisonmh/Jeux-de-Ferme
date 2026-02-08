package fr.devweb.projet484i.service;

import fr.devweb.projet484i.entity.Vache;
import fr.devweb.projet484i.entity.Fermier;
import fr.devweb.projet484i.repository.VacheRepository;
import fr.devweb.projet484i.repository.FermierRepository;
import org.springframework.stereotype.Service;
import fr.devweb.projet484i.service.FermierService;

import java.util.Optional;
import jakarta.transaction.Transactional;

@Service
public class VacheService{
    private final FermierService fermierService;
    private final FermierRepository fermierRepository;

    public VacheService(FermierService fermierService, FermierRepository fermierRepository) {
        this.fermierService = fermierService;
        this.fermierRepository = fermierRepository;
    }

    @Transactional
    public Vache prodLaitOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Vache vache = fermier.getVache();

        vache.prodLait();
        fermierRepository.save(fermier);
        return vache;
    }

    @Transactional
    public Vache traireOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Vache vache = fermier.getVache();

        vache.traire();
        fermierRepository.save(fermier);
        return vache;
    }

    @Transactional
    public Vache resetTraireOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Vache vache = fermier.getVache();

        vache.resetTraire();
        fermierRepository.save(fermier);
        return vache;
    }

    @Transactional
    public Vache nourrirBotteDePailleOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Vache vache = fermier.getVache();

        vache.nourrirBotteDePaille();
        fermierRepository.save(fermier);
        return vache;
    }

    @Transactional
    public Vache nourrirPailleOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Vache vache = fermier.getVache();

        vache.nourrirPaille();
        fermierRepository.save(fermier);
        return vache;
    }

    @Transactional
    public Vache nourrirHerbeOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Vache vache = fermier.getVache();

        vache.nourrirHerbe();
        fermierRepository.save(fermier);
        return vache;
    }

    @Transactional
    public Vache abreuverOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Vache vache = fermier.getVache();

        vache.abreuve();
        fermierRepository.save(fermier);
        return vache;
    }

    @Transactional 
    public Vache abreuverSeauDeauOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Vache vache = fermier.getVache();

        vache.abreuveSeauDeau();
        fermierRepository.save(fermier);
        return vache;
    }

    @Transactional
    public Vache affamerOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Vache vache = fermier.getVache();

        vache.affamerVache();
        fermierRepository.save(fermier);
        return vache;
    }

    @Transactional
    public Vache assoifferOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Vache vache = fermier.getVache();

        vache.assoifferVache();
        fermierRepository.save(fermier);
        return vache;
    }

    @Transactional
    public Vache nettoyerOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Vache vache = fermier.getVache();

        vache.nettoyer();
        fermierRepository.save(fermier);
        return vache;
    }

    @Transactional
    public Vache nettoyerSavonOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Vache vache = fermier.getVache();

        vache.nettoyerSavon();
        fermierRepository.save(fermier);
        return vache;
    }

    @Transactional
    public Vache salirOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Vache vache = fermier.getVache();

        vache.seSalir();
        fermierRepository.save(fermier);
        return vache;
    }

    @Transactional
    public Vache rendreMaladeOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Vache vache = fermier.getVache();

        vache.tomberMalade();
        fermierRepository.save(fermier);
        return vache;
    }

    @Transactional
    public Vache rendreMalade5JOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Vache vache = fermier.getVache();

        vache.tomberMalade5Jours();
        fermierRepository.save(fermier);
        return vache;
    }

    @Transactional
    public Vache soignerOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Vache vache = fermier.getVache();

        vache.soigner();
        fermierRepository.save(fermier);
        return vache;
    }

    @Transactional
    public Vache soignerSeringueOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Vache vache = fermier.getVache();

        vache.soignerSeringue();
        fermierRepository.save(fermier);
        return vache;
    }

    @Transactional
    public Vache grandirOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Vache vache = fermier.getVache();

        vache.grandir();
        fermierRepository.save(fermier);
        return vache;
    }

    @Transactional
    public Vache rajeunirOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Vache vache = fermier.getVache();

        vache.rajeunir();
        fermierRepository.save(fermier);
        return vache;
    }

    @Transactional
    public Vache maigrirOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Vache vache = fermier.getVache();

        vache.maigrir();
        fermierRepository.save(fermier);
        return vache;
    }

    @Transactional
    public Vache remplirOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Vache vache = fermier.getVache();

        vache.remplir();
        fermierRepository.save(fermier);
        return vache;
    }

    @Transactional
    public Vache viderOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Vache vache = fermier.getVache();

        vache.vider();
        fermierRepository.save(fermier);
        return vache;
    }

    @Transactional
    public Vache tuerOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Vache vache = fermier.getVache();

        vache.mourir();
        fermierRepository.save(fermier);
        return vache;
    }

    @Transactional
    public Vache ressuciterOfUtilisateur(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Vache vache = fermier.getVache();

        vache.ressuciter();
        fermierRepository.save(fermier);
        return vache;
    }

    @Transactional
    public Vache passageJour(String utilisateurName){
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(utilisateurName);
        Vache vache = fermier.getVache();

        vache.passageJour();
        fermierRepository.save(fermier);
        return vache;
    }
}