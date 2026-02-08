package fr.devweb.projet484i.service;

import fr.devweb.projet484i.entity.Fermier;
import fr.devweb.projet484i.entity.Vache;
import fr.devweb.projet484i.entity.Poule;
import fr.devweb.projet484i.entity.Coq;
import fr.devweb.projet484i.entity.Clapier;
import fr.devweb.projet484i.entity.Remise;
import fr.devweb.projet484i.entity.Statistique;
import fr.devweb.projet484i.repository.FermierRepository;
import org.springframework.stereotype.Service;
import fr.devweb.projet484i.VariablesGlobales;

import org.springframework.transaction.annotation.Transactional;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;


@Service
public class FermierService {
    private final FermierRepository fermierRepository;

    public FermierService(FermierRepository fermierRepository) {
        this.fermierRepository = fermierRepository;
    }

    @Transactional
    public Fermier getOrCreateFermierForUtilisateur(String username) {
        // Vérifier si la ferme existe déjà
        Optional<Fermier> existingFermier = fermierRepository.findById(username);
        if (existingFermier.isPresent()) {
            return existingFermier.get(); // Retourner la ferme existante
        }

        // Sinon, créer une nouvelle ferme
        Fermier newFermier = new Fermier(username);

        //On ajoutera les autre au fur et a mesure
        Vache vache = new Vache();
        newFermier.setVache(vache);
        Clapier clapier = new Clapier();
        newFermier.setClapier(clapier);
        Remise remise = new Remise();
        newFermier.setRemise(remise);

        List<Poule> poules = new ArrayList<Poule>();
        for(int i = 0; i < 3; i++){
            Poule poule = new Poule(VariablesGlobales.AGE_POULE, VariablesGlobales.POIDS_POULE);
            poules.add(poule);
        }
        List<Coq> coqs = new ArrayList<Coq>();
        Coq coq = new Coq(VariablesGlobales.AGE_COQ, VariablesGlobales.POIDS_COQ);
        coqs.add(coq);
        newFermier.setPoules(poules);
        newFermier.setCoqs(coqs);
        newFermier.getRemise().setOeuf(0);
        Statistique stats = new Statistique();
        stats.setSolde(newFermier.getEcus());
        newFermier.setStatistique(stats);
        VariablesGlobales.addSolde(newFermier.getEcus());
        // 
        //
        //

        return fermierRepository.save(newFermier);
    }

    @Transactional
    public void hiberner(String utilisateurName){
        Fermier fermier = getOrCreateFermierForUtilisateur(utilisateurName);
        fermier.hiberner();
        fermierRepository.save(fermier);
    }

    @Transactional
    public void sortirHibernation(String utilisateurName){
        Fermier fermier = getOrCreateFermierForUtilisateur(utilisateurName);
        fermier.sortirHibernation();
        fermierRepository.save(fermier);
    }

    @Transactional
    public void removeEcusOfUtilisateur(String utilisateurName, int ecus){
        Fermier fermier = getOrCreateFermierForUtilisateur(utilisateurName);
        fermier.suppEcus(ecus);
    
    }

    @Transactional
    public void voidEcusOfUtilisateur(String utilisateurName){
        Fermier fermier = getOrCreateFermierForUtilisateur(utilisateurName);
        fermier.zeroEcus();
    
    }

    @Transactional
    public void addEcusOfUtilisateur(String utilisateurName, int ecus){
        Fermier fermier = getOrCreateFermierForUtilisateur(utilisateurName);
        fermier.addEcus(ecus);
    }

    @Transactional
    public void rembourserEcusOfUtilisateur(String utilisateurName, int ecus){
        Fermier fermier = getOrCreateFermierForUtilisateur(utilisateurName);
        fermier.rembourserEmprunt(ecus);
    
    }

    @Transactional
    public void setAchatsOfUtilisateur(String utilisateurName, int n){
        Fermier fermier = getOrCreateFermierForUtilisateur(utilisateurName);
        fermier.setNbAchat(n);
    }

    @Transactional
    public void addLait(String utilisateurName, int lait){
        Fermier fermier = getOrCreateFermierForUtilisateur(utilisateurName);
        fermier.getStatistique().addLaitVendu(lait);
    }
}
