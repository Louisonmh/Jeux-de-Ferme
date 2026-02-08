package fr.devweb.projet484i.service;


import fr.devweb.projet484i.entity.*;
import fr.devweb.projet484i.repository.*;
import fr.devweb.projet484i.service.PouleService;
import fr.devweb.projet484i.service.CoqService;
import fr.devweb.projet484i.service.PoussinService;
import fr.devweb.projet484i.VariablesGlobales;

import org.springframework.stereotype.Service;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.boot.context.event.ApplicationReadyEvent;
import org.springframework.context.event.EventListener;


import java.util.List;
import java.util.Optional;
import java.util.Random;

@Service
public class NightService {

    @Autowired
    private final VacheRepository vacheRepository;
    @Autowired
    private final ClapierRepository clapierRepository;
    @Autowired
    private final FermierRepository fermierRepository;
    @Autowired
    private final PouleService pouleService;
    @Autowired
    private final CoqService coqService;
    @Autowired
    private final PoussinService poussinService;
    @Autowired
    private final VenteRepository venteRepository;
    
    @Autowired
    private final CooperativeRepository cooperativeRepository;

    public NightService(VacheRepository vacheRepository, VenteRepository venteRepository, CooperativeRepository cooperativeRepository,FermierRepository fermierRepository, ClapierRepository clapierRepository, PouleService pouleService, CoqService coqService, PoussinService poussinService){
        this.vacheRepository = vacheRepository;
        this.fermierRepository = fermierRepository;
        this.clapierRepository = clapierRepository;
        this.pouleService = pouleService;
        this.coqService = coqService;
        this.poussinService = poussinService;
        this.venteRepository = venteRepository;
        this.cooperativeRepository = cooperativeRepository;
    }

    @Scheduled(cron = "0 0 22 * * *") // UTC TIME
    public void passerJour() {
        List<Fermier> fermiers = fermierRepository.findAll();
        evolutionVache(fermiers);
        evolutionClapier(fermiers);
        evolutionVolailles(fermiers);
        evolutionMarche();
        evolutionCoop(fermiers);
    }

    public void evolutionVache(List<Fermier> fermiers){
        for (Fermier fermier : fermiers) {
            if(fermier.isEnHibernation() == false) {
                Vache vache = fermier.getVache();
                if (vache.isEstVivante()) {
                    vache.passageJour();
                    vacheRepository.save(vache);
                }
            }
        }
    }

    public void evolutionClapier(List<Fermier> fermiers){
        for (Fermier fermier : fermiers) {
            if(fermier.isEnHibernation() == false) {
                Clapier clapier = fermier.getClapier();
                clapier.passageJour();
                clapierRepository.save(clapier);
            }
        }
    }

    public void evolutionVolailles(List<Fermier> fermiers){
        for (Fermier fermier : fermiers) {
            if(fermier.isEnHibernation() == false) {
                pouleService.passageJourOfUtilisateur(fermier.getNomUtilisateur());
                coqService.passageJourOfUtilisateur(fermier.getNomUtilisateur());
                poussinService.passageJourOfUtilisateur(fermier.getNomUtilisateur());
            }
        }
    }

    public void evolutionMarche(){
        List<Vente> ventes = venteRepository.findAll();
        for(Vente vente : ventes) {
            venteRepository.delete(vente);
        }
    }

    public void evolutionCoop(List<Fermier> fermiers){
        Cooperative coop = cooperativeRepository.findAll().get(0);
        //Cooperative coop = cooperativeRepository.findById("coop_").orElseThrow(() -> new IllegalArgumentException("Coop non trouvée"));
        coop.resetQttArticles(fermiers.size());
        cooperativeRepository.save(coop);
    }

    public void evolutionFermier(List<Fermier> fermiers) {
        for (Fermier fermier : fermiers) {
            if(fermier.isEnHibernation() == false) {
                fermier.setNbAchat(0);
            }
        }
    }
}
