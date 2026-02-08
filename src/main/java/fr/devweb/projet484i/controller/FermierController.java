package fr.devweb.projet484i.controller;

import fr.devweb.projet484i.entity.Fermier;
import fr.devweb.projet484i.entity.Vache;
import fr.devweb.projet484i.entity.Poule;
import fr.devweb.projet484i.entity.Coq;
import fr.devweb.projet484i.entity.Poussin;
import fr.devweb.projet484i.entity.Remise;
import fr.devweb.projet484i.entity.Clapier;
import fr.devweb.projet484i.service.FermierService;
import fr.devweb.projet484i.service.VacheService;
import fr.devweb.projet484i.service.PouleService;
import fr.devweb.projet484i.service.CoqService;
import fr.devweb.projet484i.service.PoussinService;
import fr.devweb.projet484i.service.RemiseService;
import fr.devweb.projet484i.service.ClapierService;
//import jdk.jshell.execution.Util;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;
import org.springframework.security.core.Authentication;

@RestController
@RequestMapping("/fermiers")
public class FermierController {

    private final FermierService fermierService;
    private final VacheService vacheService;
    private final ClapierService clapierService;
    private final RemiseService remiseService;
    private final PouleService pouleService;
    private final CoqService coqService;
    private final PoussinService poussinService;

    public FermierController(FermierService fermierService, VacheService vacheService, ClapierService clapierService, RemiseService remiseService, PouleService pouleService, CoqService coqService, PoussinService poussinService) {
        this.fermierService = fermierService;
        this.vacheService = vacheService;
        this.clapierService = clapierService;
        this.remiseService = remiseService;
        this.pouleService = pouleService;
        this.coqService = coqService;
        this.poussinService = poussinService;
    }

    // Fonctions liées au fermier

    @GetMapping
    public Fermier getOrCreateFermier(Authentication authentication) {
        String username = authentication.getName();
        return fermierService.getOrCreateFermierForUtilisateur(username);
    }

    @PostMapping("/suppEcus/{ecus}")
    public void suppEcus(Authentication authentication, @PathVariable("ecus") int ecus){
        fermierService.removeEcusOfUtilisateur(authentication.getName(), ecus);
    }

    @PostMapping("/addEcus/{ecus}")
    public void addEcus(Authentication authentication, @PathVariable("ecus") int ecus){
        fermierService.addEcusOfUtilisateur(authentication.getName(), ecus);
    }

    @PostMapping("/rembourserEcus/{ecus}")
    public void rembourserEcus(Authentication authentication, @PathVariable("ecus") int ecus){
        fermierService.rembourserEcusOfUtilisateur(authentication.getName(), ecus);
    }

    @PostMapping("/zeroEcus")
    public void zeroEcus(Authentication authentication){
        fermierService.voidEcusOfUtilisateur(authentication.getName());
    }

    @PostMapping("/setAchats/{n}")
    public void zeroEcus(Authentication authentication, @PathVariable("n") int n){
        fermierService.setAchatsOfUtilisateur(authentication.getName(), n);
    }

    @PostMapping("/hiberner")
    public void hiberner(Authentication authentication){
        fermierService.hiberner(authentication.getName());
    }

    @PostMapping("/sortirHibernation")
    public void sortirHibernation(Authentication authentication){
        fermierService.sortirHibernation(authentication.getName());
    }

    // Fonctions liées à la vache

    @GetMapping("/vache")
    public Vache getVache(Authentication authentication) {
        String username = authentication.getName();
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(username);
        return fermier.getVache();
    }

    @GetMapping("/vache/estNourrie")
    public boolean vacheEstNourrie(Authentication authentication) {
        return fermierService.getOrCreateFermierForUtilisateur(authentication.getName()).getVache().estNourrie();
    }
    @GetMapping("/vache/estAbreuvee")
    public boolean vacheEstAbreuvee(Authentication authentication) {
        return fermierService.getOrCreateFermierForUtilisateur(authentication.getName()).getVache().estAbreuvee();
    }

    @PostMapping("/vache/prodLait")
    public Vache prodLaitVache(Authentication authentication){
        return vacheService.prodLaitOfUtilisateur(authentication.getName());
    }

    @PostMapping("/vache/traire")
    public Vache traireVache(Authentication authentication){
        return vacheService.traireOfUtilisateur(authentication.getName());
    }

    @PostMapping("/vache/resetTraire")
    public Vache resetTraireVache(Authentication authentication){
        return vacheService.resetTraireOfUtilisateur(authentication.getName());
    }

    @PostMapping("/vache/nourrirBottePaille")
    public Vache nourrirBotteDePailleVache(Authentication authentication){
        return vacheService.nourrirBotteDePailleOfUtilisateur(authentication.getName());
    }

    @PostMapping("/vache/nourrirPaille")
    public Vache nourrirPailleVache(Authentication authentication){
        return vacheService.nourrirPailleOfUtilisateur(authentication.getName());
    }

    @PostMapping("/vache/nourrirHerbe")
    public Vache nourrirHerbeVache(Authentication authentication){
        return vacheService.nourrirHerbeOfUtilisateur(authentication.getName());
    }

    @PostMapping("/vache/abreuver")
    public Vache abreuve(Authentication authentication){
        return vacheService.abreuverOfUtilisateur(authentication.getName());
    }

    @PostMapping("/vache/abreuverSeauDeau")
    public Vache abreuveSeauDeau(Authentication authentication){
        return vacheService.abreuverSeauDeauOfUtilisateur(authentication.getName());
    }

    @PostMapping("/vache/affamer")
    public Vache affamerVache(Authentication authentication){
        return vacheService.affamerOfUtilisateur(authentication.getName());
    }

    @PostMapping("/vache/assoiffer")
    public Vache assoifferVache(Authentication authentication){
        return vacheService.assoifferOfUtilisateur(authentication.getName());
    }

    @PostMapping("/vache/nettoyer")
    public Vache nettoyer(Authentication authentication){
        return vacheService.nettoyerOfUtilisateur(authentication.getName());
    }

    @PostMapping("/vache/nettoyerSavon")
    public Vache nettoyerSavon(Authentication authentication){
        return vacheService.nettoyerSavonOfUtilisateur(authentication.getName());
    }

    @PostMapping("/vache/salir")
    public Vache salirVache(Authentication authentication){
        return vacheService.salirOfUtilisateur(authentication.getName());
    }

    @PostMapping("/vache/rendreMalade")
    public Vache rendreMaladeVache(Authentication authentication){
        return vacheService.rendreMaladeOfUtilisateur(authentication.getName());
    }

    @PostMapping("/vache/rendreMalade5J")
    public Vache rendreMalade5JVache(Authentication authentication){
        return vacheService.rendreMalade5JOfUtilisateur(authentication.getName());
    }

    @PostMapping("/vache/soigner")
    public Vache soigner(Authentication authentication){
        return vacheService.soignerOfUtilisateur(authentication.getName());
    }

    @PostMapping("/vache/soignerSeringue")
    public Vache soignerSeringue(Authentication authentication){
        return vacheService.soignerSeringueOfUtilisateur(authentication.getName());
    }

    @PostMapping("/vache/grandir")
    public Vache grandirVache(Authentication authentication){
        return vacheService.grandirOfUtilisateur(authentication.getName());
    }

    @PostMapping("/vache/rajeunir")
    public Vache rajeunirVache(Authentication authentication){
        return vacheService.rajeunirOfUtilisateur(authentication.getName());
    }

    @PostMapping("/vache/maigrir")
    public Vache maigrirVache(Authentication authentication){
        return vacheService.maigrirOfUtilisateur(authentication.getName());
    }

    @PostMapping("/vache/remplir")
    public Vache remplirVache(Authentication authentication){
        return vacheService.remplirOfUtilisateur(authentication.getName());
    }

    @PostMapping("/vache/vider")
    public Vache viderVache(Authentication authentication){
        return vacheService.viderOfUtilisateur(authentication.getName());
    }

    @PostMapping("/vache/tuer")
    public Vache tuerVache(Authentication authentication){
       return vacheService.tuerOfUtilisateur(authentication.getName());
    }

    @PostMapping("/vache/ressuciter")
    public Vache ressuciterVache(Authentication authentication){
       return vacheService.ressuciterOfUtilisateur(authentication.getName());
    }

    // Fonctions liées au clapier

    @GetMapping("/clapier")
    public Clapier getClapier(Authentication authentication) {
        String username = authentication.getName();
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(username);
        return fermier.getClapier();
    }

    @PostMapping("/clapier/adultes/affamer")
    public Clapier affamerClapierAdultes(Authentication authentication){
       return clapierService.affamerAdultesOfUtilisateur(authentication.getName());
    }

    @PostMapping("/clapier/adultes/nourrir")
    public Clapier nourrirClapierAdultes(Authentication authentication){
       return clapierService.nourrirAdultesOfUtilisateur(authentication.getName());
    }

    @PostMapping("/clapier/adultes/nourrirSac")
    public Clapier nourrirSacClapierAdultes(Authentication authentication){
       return clapierService.nourrirAdultesSacOfUtilisateur(authentication.getName());
    }

    @PostMapping("/clapier/adultes/assoiffer")
    public Clapier assoifferClapierAdultes(Authentication authentication){
       return clapierService.assoifferAdultesOfUtilisateur(authentication.getName());
    }

    @PostMapping("/clapier/adultes/abreuver")
    public Clapier abreuverClapierAdultes(Authentication authentication){
       return clapierService.abreuveAdultesOfUtilisateur(authentication.getName());
    }

    @PostMapping("/clapier/adultes/abreuverEau")
    public Clapier abreuverEauClapierAdultes(Authentication authentication){
       return clapierService.abreuveAdultesSeauDeauOfUtilisateur(authentication.getName());
    }

    @PostMapping("/clapier/adultes/malades")
    public Clapier maladesClapierAdultes(Authentication authentication){
       return clapierService.adultesMaladesOfUtilisateur(authentication.getName());
    }

    @PostMapping("/clapier/adultes/soigner")
    public Clapier soignerClapierAdultes(Authentication authentication){
       return clapierService.soignerAdultesOfUtilisateur(authentication.getName());
    }

    @PostMapping("/clapier/adultes/soignerSeringue")
    public Clapier soignerSeringueClapierAdultes(Authentication authentication){
       return clapierService.soignerAdultesSeringueOfUtilisateur(authentication.getName());
    }

    @PostMapping("/clapier/adultes/salir")
    public Clapier salirClapierAdultes(Authentication authentication){
       return clapierService.salirAdultesOfUtilisateur(authentication.getName());
    }

    @PostMapping("/clapier/adultes/nettoyer")
    public Clapier nettoyerClapierAdultes(Authentication authentication){
       return clapierService.nettoyerAdultesOfUtilisateur(authentication.getName());
    }

    @PostMapping("/clapier/adultes/nettoyerSavon")
    public Clapier nettoyerSavonClapierAdultes(Authentication authentication){
       return clapierService.nettoyerAdultesSavonOfUtilisateur(authentication.getName());
    }

    @PostMapping("/clapier/enfants/affamer")
    public Clapier affamerClapierEnfants(Authentication authentication){
       return clapierService.affamerEnfantsOfUtilisateur(authentication.getName());
    }

    @PostMapping("/clapier/enfants/nourrir")
    public Clapier nourrirClapierEnfants(Authentication authentication){
       return clapierService.nourrirEnfantsOfUtilisateur(authentication.getName());
    }

    @PostMapping("/clapier/enfants/nourrirSac")
    public Clapier nourrirSacClapierEnfants(Authentication authentication){
       return clapierService.nourrirEnfantsSacOfUtilisateur(authentication.getName());
    }

    @PostMapping("/clapier/enfants/assoiffer")
    public Clapier assoifferClapierEnfants(Authentication authentication){
       return clapierService.assoifferEnfantsOfUtilisateur(authentication.getName());
    }

    @PostMapping("/clapier/enfants/abreuver")
    public Clapier abreuverClapierEnfants(Authentication authentication){
       return clapierService.abreuveEnfantsOfUtilisateur(authentication.getName());
    }

    @PostMapping("/clapier/enfants/abreuverEau")
    public Clapier abreuverEauClapierEnfants(Authentication authentication){
       return clapierService.abreuveEnfantsSeauDeauOfUtilisateur(authentication.getName());
    }

    @PostMapping("/clapier/enfants/malades")
    public Clapier maladesClapierEnfants(Authentication authentication){
       return clapierService.enfantsMaladesOfUtilisateur(authentication.getName());
    }

    @PostMapping("/clapier/enfants/soigner")
    public Clapier soignerClapierEnfants(Authentication authentication){
       return clapierService.soignerEnfantsOfUtilisateur(authentication.getName());
    }

    @PostMapping("/clapier/enfants/soignerSeringue")
    public Clapier soignerSeringueClapierEnfants(Authentication authentication){
       return clapierService.soignerEnfantsSeringueOfUtilisateur(authentication.getName());
    }

    @PostMapping("/clapier/enfants/salir")
    public Clapier salirClapierEnfants(Authentication authentication){
       return clapierService.salirEnfantsOfUtilisateur(authentication.getName());
    }

    @PostMapping("/clapier/enfants/nettoyer")
    public Clapier nettoyerClapierEnfants(Authentication authentication){
       return clapierService.nettoyerEnfantsOfUtilisateur(authentication.getName());
    }

    @PostMapping("/clapier/enfants/nettoyerSavon")
    public Clapier nettoyerSavonClapierEnfants(Authentication authentication){
       return clapierService.nettoyerEnfantsSavonOfUtilisateur(authentication.getName());
    }

    @PostMapping("/clapier/adultes/males/add/{n}")
    public Clapier addMalesClapier(Authentication authentication, @PathVariable("n") int n){
       return clapierService.addAdultesMalesOfUtilisateur(authentication.getName(), n);
    }

    @PostMapping("/clapier/adultes/males/supp/{n}")
    public Clapier suppMalesClapier(Authentication authentication, @PathVariable("n") int n){
       return clapierService.suppAdultesMalesOfUtilisateur(authentication.getName(), n);
    }

    @PostMapping("/clapier/adultes/femelles/add/{n}")
    public Clapier addFemellesClapier(Authentication authentication, @PathVariable("n") int n){
       return clapierService.addAdultesFemellesOfUtilisateur(authentication.getName(), n);
    }

    @PostMapping("/clapier/adultes/femelles/supp/{n}")
    public Clapier suppFemellesClapier(Authentication authentication, @PathVariable("n") int n){
       return clapierService.suppAdultesFemellesOfUtilisateur(authentication.getName(), n);
    }

    @PostMapping("/clapier/enfants/bebes/add/{n}")
    public Clapier addBebesClapier(Authentication authentication, @PathVariable("n") int n){
       return clapierService.addBebesOfUtilisateur(authentication.getName(), n);
    }

    @PostMapping("/clapier/enfants/bebes/supp/{n}")
    public Clapier suppBebesClapier(Authentication authentication, @PathVariable("n") int n){
       return clapierService.suppBebesOfUtilisateur(authentication.getName(), n);
    }

    @PostMapping("/clapier/enfants/petits/add/{n}")
    public Clapier addPetitsClapier(Authentication authentication, @PathVariable("n") int n){
       return clapierService.addPetitsOfUtilisateur(authentication.getName(), n);
    }

    @PostMapping("/clapier/enfants/petits/supp/{n}")
    public Clapier suppPetitsClapier(Authentication authentication, @PathVariable("n") int n){
       return clapierService.suppPetitsOfUtilisateur(authentication.getName(), n);
    }

    @PostMapping("/clapier/enfants/gros/add/{n}")
    public Clapier addGrosClapier(Authentication authentication, @PathVariable("n") int n){
       return clapierService.addGrosOfUtilisateur(authentication.getName(), n);
    }

    @PostMapping("/clapier/enfants/gros/supp/{n}")
    public Clapier suppGrosClapier(Authentication authentication, @PathVariable("n") int n){
       return clapierService.suppGrosOfUtilisateur(authentication.getName(), n);
    }

    @PostMapping("/clapier/remplir")
    public Clapier remplirClapier(Authentication authentication){
       return clapierService.remplirOfUtilisateur(authentication.getName());
    }

    @PostMapping("/clapier/remplirMax")
    public Clapier remplirMaxClapier(Authentication authentication){
       return clapierService.remplirMaxOfUtilisateur(authentication.getName());
    }

    @PostMapping("/clapier/vider")
    public Clapier viderClapier(Authentication authentication){
       return clapierService.viderOfUtilisateur(authentication.getName());
    }

    @PostMapping("/clapier/grandir")
    public Clapier grandirClapier(Authentication authentication){
       return clapierService.grandirOfUtilisateur(authentication.getName());
    }

    @PostMapping("/clapier/reproduction")
    public Clapier reproductionClapier(Authentication authentication){
       return clapierService.reproductionOfUtilisateur(authentication.getName());
    }

    @PostMapping("/clapier/mort")
    public Clapier mortClapier(Authentication authentication){
       return clapierService.mortOfUtilisateur(authentication.getName());
    }

    @PostMapping("/clapier/passageJour")
    public Clapier passageJourClapier(Authentication authentication){
       return clapierService.passageJourOfUtilisateur(authentication.getName());
    }

    // Fonctions liées à la remise

    @GetMapping("/remise")
    public Remise getRemise(Authentication authentication) {
        String username = authentication.getName();
        Fermier fermier = fermierService.getOrCreateFermierForUtilisateur(username);
        return fermier.getRemise();
    }

    @PostMapping("/remise/vider")
    public Remise viderRemise(Authentication authentication){
        return remiseService.viderOfUtilisateur(authentication.getName());
    }

    @PostMapping("/remise/remplirUn")
    public Remise remplirUnRemise(Authentication authentication){
        return remiseService.remplirUnOfUtilisateur(authentication.getName());
    }

    @PostMapping("/remise/remplirPlusieurs")
    public Remise remplirPlusieursRemise(Authentication authentication){
        return remiseService.remplirPlusieursOfUtilisateur(authentication.getName());
    }

    @PostMapping("/remise/incEau/{n}")
    public Remise incEauRemise(Authentication authentication,@PathVariable("n") int n){
        return remiseService.incEauOfUtilisateur(authentication.getName(), n);
    }

    @PostMapping("/remise/decEau")
    public Remise decEauRemise(Authentication authentication){
        return remiseService.decEauOfUtilisateur(authentication.getName());
    }

    @PostMapping("/remise/incBottesPaille/{n}")
    public Remise incBottesPailleRemise(Authentication authentication,@PathVariable("n") int n){
        return remiseService.incBottesPailleOfUtilisateur(authentication.getName(), n);
    }

    @PostMapping("/remise/decBottesPaille")
    public Remise decBottesPailleRemise(Authentication authentication){
        return remiseService.decBottesPailleOfUtilisateur(authentication.getName());
    }

    @PostMapping("/remise/incSeringues/{n}")
    public Remise incSeringuesRemise(Authentication authentication,@PathVariable("n") int n){
        return remiseService.incSeringuesOfUtilisateur(authentication.getName(), n);
    }

    @PostMapping("/remise/decSeringues")
    public Remise decSeringuesRemise(Authentication authentication){
        return remiseService.decSeringuesOfUtilisateur(authentication.getName());
    }

    @PostMapping("/remise/incSavons/{n}")
    public Remise incSavonsRemise(Authentication authentication,@PathVariable("n") int n){
        return remiseService.incSavonsOfUtilisateur(authentication.getName(), n);
    }

    @PostMapping("/remise/decSavons")
    public Remise decSavonsRemise(Authentication authentication){
        return remiseService.decSavonsOfUtilisateur(authentication.getName());
    }

    @PostMapping("/remise/incSacsNourriture/{n}")
    public Remise incSacsNourritureRemise(Authentication authentication,@PathVariable("n") int n){
        return remiseService.incSacsNourritureOfUtilisateur(authentication.getName(), n);
    }

    @PostMapping("/remise/decSacsNourriture")
    public Remise decSacsNourritureRemise(Authentication authentication){
        return remiseService.decSacsNourritureOfUtilisateur(authentication.getName());
    }

    @PostMapping("/remise/incOeufs/{n}")
    public Remise incOeufsRemise(Authentication authentication,@PathVariable("n") int n){
        return remiseService.incOeufsOfUtilisateur(authentication.getName(), n);
    }

    @PostMapping("/remise/decOeufs/{n}")
    public Remise decOeufsRemise(Authentication authentication,@PathVariable("n") int n){
        return remiseService.decOeufsOfUtilisateur(authentication.getName(), n);
    }

    @PostMapping("/remise/incLitresLait/{n}")
    public Remise incLitresLaitRemise(Authentication authentication,@PathVariable("n") int n){
        return remiseService.incLitresLaitOfUtilisateur(authentication.getName(), n);
    }

    @PostMapping("/remise/decLitresLait/{n}")
    public Remise decLitresLaitRemise(Authentication authentication,@PathVariable("n") int n){
        return remiseService.decLitresLaitOfUtilisateur(authentication.getName(), n);
    }

    // methode pour les poules

    @GetMapping("/poules")
    public List<Poule> getPoules(Authentication authentication) {
        return pouleService.getPoulesOfUser(authentication.getName());
    }

    @PostMapping("/poules/add/{n}")
    public List<Poule> addNPoules(Authentication authentication, @PathVariable("n") int n){
        return pouleService.addNPoulesOfUtilisateur(authentication.getName(), n);
    }

    @PostMapping("/poules/nourrir/{id}")
    public Poule nourrirPoule(Authentication authentication, @PathVariable("id") Long id){
        return pouleService.nourrirPouleOfUtilisateur(authentication.getName(), id);
    }

    @PostMapping("/poules/nourrirAll")
    public List<Poule> nourrirAll(Authentication authentication){
        return pouleService.nourrirAllOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poules/nourrirAllSacNourriture")
    public List<Poule> nourrirAllSacNourriture(Authentication authentication){
        return pouleService.nourrirAllSacNourritureOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poules/abreuve/{id}")
    public Poule abreuvePoule(Authentication authentication, @PathVariable("id") Long id){
        return pouleService.abreuvePouleOfUtilisateur(authentication.getName(), id);
    }

    @PostMapping("/poules/abreuveAll")
    public List<Poule> abreuveAll(Authentication authentication){
        return pouleService.abreuveAllOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poules/abreuveAllSeauDeau")
    public List<Poule> abreuveAllSeauDeau(Authentication authentication){
        return pouleService.abreuveAllSeauDeauOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poules/affamer")
    public List<Poule> affamerPoules(Authentication authentication){
        return pouleService.affamerOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poules/affamer2")
    public List<Poule> affamer2Poules(Authentication authentication){
        return pouleService.affamer2OfUtilisateur(authentication.getName());
    }

    @PostMapping("/poules/affamer3")
    public List<Poule> affamer3Poules(Authentication authentication){
        return pouleService.affamer3OfUtilisateur(authentication.getName());
    }

    @PostMapping("/poules/affamer4")
    public List<Poule> affamer4Poules(Authentication authentication){
        return pouleService.affamer4OfUtilisateur(authentication.getName());
    }

    @PostMapping("/poules/assoiffer")
    public List<Poule> assoifferPoules(Authentication authentication){
        return pouleService.assoifferOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poules/abreuver")
    public List<Poule> abreuverPoules(Authentication authentication){
        return pouleService.abreuver2OfUtilisateur(authentication.getName());
    }

    @PostMapping("/poules/salir")
    public List<Poule> salirPoules(Authentication authentication){
        return pouleService.salirOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poules/nettoyer/{id}")
    public Poule nettoyerPoule(Authentication authentication, @PathVariable("id") Long id){
        return pouleService.nettoyerPouleOfUtilisateur(authentication.getName(), id);
    }

    @PostMapping("/poules/nettoyerAll")
    public List<Poule> nettoyerAllPoules(Authentication authentication){
        return pouleService.nettoyerAllOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poules/nettoyerAllSavon")
    public List<Poule> nettoyerAllSavonPoules(Authentication authentication){
        return pouleService.nettoyerAllSavonOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poules/malade")
    public List<Poule> maladePoules(Authentication authentication){
        return pouleService.maladeOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poules/malade4")
    public List<Poule> malade4Poules(Authentication authentication){
        return pouleService.malade4OfUtilisateur(authentication.getName());
    }

    @PostMapping("/poules/soigner/{id}")
    public Poule soignerPoule(Authentication authentication, @PathVariable("id") Long id){
        return pouleService.soignerPouleOfUtilisateur(authentication.getName(), id);
    }

    @PostMapping("/poules/soignerAll")
    public List<Poule> soignerAllPoules(Authentication authentication){
        return pouleService.soignerAllOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poules/soignerAllSeringue")
    public List<Poule> soignerAllSeringuePoules(Authentication authentication){
        return pouleService.soignerAllSeringueOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poules/couver/{nbo}")
    public List<Poule> couverOeufs(Authentication authentication, @PathVariable("nbo") int nbo){
        return pouleService.couverOfUtilisateur(authentication.getName(), nbo);
    }

    @PostMapping("/poules/couvaison")
    public List<Poule> couvaison(Authentication authentication){
        return pouleService.couvaisonOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poules/arreterCouver")
    public List<Poule> arreterCouver(Authentication authentication){
        return pouleService.arreterCouverOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poules/pondre")
    public List<Poule> pondreOeufs(Authentication authentication){
        return pouleService.pondreOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poules/famine")
    public List<Poule> faminePoules(Authentication authentication){
        return pouleService.famineOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poules/tuer")
    public List<Poule> tuerPoules(Authentication authentication){
        return pouleService.tuerOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poules/maigrir")
    public List<Poule> maigrirPoules(Authentication authentication){
        return pouleService.maigrirOfUtilisateur(authentication.getName());
    }
    
    @PostMapping("/add3Poule")
    public List<Poule> add3Poule(Authentication authentication){
        return pouleService.add3PouleToFermier(authentication.getName());
    }

    @PostMapping("/poules/regression")
    public List<Poule> regressionPoule(Authentication authentication){
        return pouleService.regressionOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poules/enfant")
    public List<Poule> enfantPoule(Authentication authentication){
        return pouleService.enfantOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poules/passageJour")
    public List<Poule> passageJourPoule(Authentication authentication){
        return pouleService.passageJourOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poules/nourrirHier")
    public List<Poule> nourrirHierPoule(Authentication authentication){
        return pouleService.nourrirHierPouleOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poules/abreuveHier")
    public List<Poule> abreuveHierPoule(Authentication authentication){
        return pouleService.abreuveHierPouleOfUtilisateur(authentication.getName());
    }

    // methode pour les coqs

    @GetMapping("/coqs")
    public List<Coq> getCoqs(Authentication authentication) {
        return coqService.getCoqsOfUser(authentication.getName());
    }

    @PostMapping("/coqs/add/{n}")
    public List<Coq> addNCoqs(Authentication authentication, @PathVariable("n") int n){
        return coqService.addNCoqsOfUtilisateur(authentication.getName(), n);
    }

    @PostMapping("/coqs/nourrir/{id}")
    public Coq nourrirCoq(Authentication authentication, @PathVariable("id") Long id){
        return coqService.nourrirCoqOfUtilisateur(authentication.getName(), id);
    }

    @PostMapping("/coqs/nourrirAll")
    public List<Coq> nourrirAllCoqs(Authentication authentication){
        return coqService.nourrirAllOfUtilisateur(authentication.getName());
    }

    @PostMapping("/coqs/nourrirAllSacNourriture")
    public List<Coq> nourrirAllCoqsSacNourriture(Authentication authentication){
        return coqService.nourrirAllSacNourritureOfUtilisateur(authentication.getName());
    }

    @PostMapping("/coqs/abreuve/{id}")
    public Coq abreuveCoq(Authentication authentication, @PathVariable("id") Long id){
        return coqService.abreuveCoqOfUtilisateur(authentication.getName(), id);
    }

    @PostMapping("/coqs/abreuveAll")
    public List<Coq> abreuveAllCoq(Authentication authentication){
        return coqService.abreuveAllOfUtilisateur(authentication.getName());
    }

    @PostMapping("/coqs/abreuveAllSeauDeau")
    public List<Coq> abreuveAllCoqSeauDeau(Authentication authentication){
        return coqService.abreuveAllSeauDeauOfUtilisateur(authentication.getName());
    }

    @PostMapping("/coqs/affamer")
    public List<Coq> affamerCoqs(Authentication authentication){
        return coqService.affamerOfUtilisateur(authentication.getName());
    }

    @PostMapping("/coqs/affamer2")
    public List<Coq> affamer2Coqs(Authentication authentication){
        return coqService.affamer2OfUtilisateur(authentication.getName());
    }

    @PostMapping("/coqs/affamer3")
    public List<Coq> affamer3Coqs(Authentication authentication){
        return coqService.affamer3OfUtilisateur(authentication.getName());
    }

    @PostMapping("/coqs/affamer4")
    public List<Coq> affamer4Coqs(Authentication authentication){
        return coqService.affamer4OfUtilisateur(authentication.getName());
    }

    @PostMapping("/coqs/assoiffer")
    public List<Coq> assoifferCoqs(Authentication authentication){
        return coqService.assoifferOfUtilisateur(authentication.getName());
    }

    @PostMapping("/coqs/abreuver")
    public List<Coq> abreuverCoqs(Authentication authentication){
        return coqService.abreuverOfUtilisateur(authentication.getName());
    }

    @PostMapping("/coqs/salir")
    public List<Coq> salirCoqs(Authentication authentication){
        return coqService.salirOfUtilisateur(authentication.getName());
    }

    @PostMapping("/coqs/nettoyer/{id}")
    public Coq nettoyerCoq(Authentication authentication, @PathVariable("id") Long id){
        return coqService.nettoyerCoqOfUtilisateur(authentication.getName(), id);
    }

    @PostMapping("/coqs/nettoyerAll")
    public List<Coq> nettoyerAllCoqs(Authentication authentication){
        return coqService.nettoyerAllOfUtilisateur(authentication.getName());
    }

    @PostMapping("/coqs/nettoyerAllSavon")
    public List<Coq> nettoyerAllSavonCoqs(Authentication authentication){
        return coqService.nettoyerAllSavonOfUtilisateur(authentication.getName());
    }

    @PostMapping("/coqs/malade")
    public List<Coq> maladeCoqs(Authentication authentication){
        return coqService.maladeOfUtilisateur(authentication.getName());
    }

    @PostMapping("/coqs/malade4")
    public List<Coq> malade4Coqs(Authentication authentication){
        return coqService.malade4OfUtilisateur(authentication.getName());
    }

    @PostMapping("/coqs/soigner/{id}")
    public Coq soignerCoq(Authentication authentication, @PathVariable("id") Long id){
        return coqService.soignerCoqOfUtilisateur(authentication.getName(), id);
    }

    @PostMapping("/coqs/soignerAll")
    public List<Coq> soignerAllCoqs(Authentication authentication){
        return coqService.soignerAllOfUtilisateur(authentication.getName());
    }

    @PostMapping("/coqs/soignerAllSeringue")
    public List<Coq> soignerAllSeringueCoqs(Authentication authentication){
        return coqService.soignerAllSeringueOfUtilisateur(authentication.getName());
    }

    @PostMapping("/coqs/famine")
    public List<Coq> famineCoqs(Authentication authentication){
        return coqService.famineOfUtilisateur(authentication.getName());
    }

    @PostMapping("/coqs/tuer")
    public List<Coq> tuerCoqs(Authentication authentication){
        return coqService.tuerOfUtilisateur(authentication.getName());
    }

    @PostMapping("/coqs/maigrir")
    public List<Coq> maigrirCoqs(Authentication authentication){
        return coqService.maigrirOfUtilisateur(authentication.getName());
    }
    
    @PostMapping("/add1Coq")
    public void add1Coq(Authentication authentication){
        coqService.add1CoqToFermier(authentication.getName());
    }

    @PostMapping("/coqs/regression")
    public void regressionCoq(Authentication authentication){
        coqService.regressionOfUtilisateur(authentication.getName());
    }

    @PostMapping("/coqs/enfant")
    public void enfantCoq(Authentication authentication){
        coqService.enfantOfUtilisateur(authentication.getName());
    }

    @PostMapping("/coqs/nourrirHier")
    public List<Coq> nourrirHierAllCoqs(Authentication authentication){
        return coqService.nourrirHierAllOfUtilisateur(authentication.getName());
    }

    @PostMapping("/coqs/abreuveHier")
    public List<Coq> abreuveHierAllCoqs(Authentication authentication){
        return coqService.abreuveHierAllOfUtilisateur(authentication.getName());
    }

    @PostMapping("/coqs/passageJour")
    public List<Coq> passageJourCoqs(Authentication authentication){
        return coqService.passageJourOfUtilisateur(authentication.getName());
    }

    // methode pour les coqs

    @GetMapping("/poussins")
    public List<Poussin> getPoussins(Authentication authentication) {
        return poussinService.getPoussinsOfUser(authentication.getName());
    }

    @PostMapping("/poussins/nourrir/{id}")
    public Poussin nourrirPoussin(Authentication authentication, @PathVariable("id") Long id){
        return poussinService.nourrirPoussinOfUtilisateur(authentication.getName(), id);
    }

    @PostMapping("/poussins/nourrirAll")
    public List<Poussin> nourrirAllPoussins(Authentication authentication){
        return poussinService.nourrirAllOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poussins/nourrirAllSacNourriture")
    public List<Poussin> nourrirAllPoussinsSacNourriture(Authentication authentication){
        return poussinService.nourrirAllSacNourritureOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poussins/abreuve/{id}")
    public Poussin abreuvePoussin(Authentication authentication, @PathVariable("id") Long id){
        return poussinService.abreuvePoussinOfUtilisateur(authentication.getName(), id);
    }

    @PostMapping("/poussins/abreuveAll")
    public List<Poussin> abreuveAllPoussin(Authentication authentication){
        return poussinService.abreuveAllOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poussins/abreuveAllSeauDeau")
    public List<Poussin> abreuveAllPoussinSeauDeau(Authentication authentication){
        return poussinService.abreuveAllSeauDeauOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poussins/affamer")
    public List<Poussin> affamerPoussins(Authentication authentication){
        return poussinService.affamerOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poussins/affamer2")
    public List<Poussin> affamer2Poussins(Authentication authentication){
        return poussinService.affamer2OfUtilisateur(authentication.getName());
    }

    @PostMapping("/poussins/affamer3")
    public List<Poussin> affamer3Poussins(Authentication authentication){
        return poussinService.affamer3OfUtilisateur(authentication.getName());
    }

    @PostMapping("/poussins/affamer4")
    public List<Poussin> affamer4Poussins(Authentication authentication){
        return poussinService.affamer4OfUtilisateur(authentication.getName());
    }

    @PostMapping("/poussins/assoiffer")
    public List<Poussin> assoifferPoussins(Authentication authentication){
        return poussinService.assoifferOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poussins/abreuver")
    public List<Poussin> abreuverPoussins(Authentication authentication){
        return poussinService.abreuverOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poussins/salir")
    public List<Poussin> salirPoussins(Authentication authentication){
        return poussinService.salirOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poussins/nettoyer/{id}")
    public Poussin nettoyerPoussin(Authentication authentication, @PathVariable("id") Long id){
        return poussinService.nettoyerPoussinOfUtilisateur(authentication.getName(), id);
    }

    @PostMapping("/poussins/nettoyerAll")
    public List<Poussin> nettoyerAllPoussins(Authentication authentication){
        return poussinService.nettoyerAllOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poussins/nettoyerAllSavon")
    public List<Poussin> nettoyerAllSavonPoussins(Authentication authentication){
        return poussinService.nettoyerAllSavonOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poussins/malade")
    public List<Poussin> maladePoussins(Authentication authentication){
        return poussinService.maladeOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poussins/malade4")
    public List<Poussin> malade4Poussins(Authentication authentication){
        return poussinService.malade4OfUtilisateur(authentication.getName());
    }

    @PostMapping("/poussins/soigner/{id}")
    public Poussin soignerPoussin(Authentication authentication, @PathVariable("id") Long id){
        return poussinService.soignerPoussinOfUtilisateur(authentication.getName(), id);
    }

    @PostMapping("/poussins/soignerAll")
    public List<Poussin> soignerAllPoussins(Authentication authentication){
        return poussinService.soignerAllOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poussins/soignerAllSeringue")
    public List<Poussin> soignerAllSeringuePoussins(Authentication authentication){
        return poussinService.soignerAllSeringueOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poussins/famine")
    public List<Poussin> faminePoussins(Authentication authentication){
        return poussinService.famineOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poussins/tuer")
    public List<Poussin> tuerPoussins(Authentication authentication){
        return poussinService.tuerOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poussins/maigrir")
    public List<Poussin> maigrirPoussins(Authentication authentication){
        return poussinService.maigrirOfUtilisateur(authentication.getName());
    }

    @PostMapping("/add3Poussin")
    public void add3Poussin(Authentication authentication){
        poussinService.add3PoussinToFermier(authentication.getName());
    }

    @PostMapping("/poussins/grandir")
    public void grandirPoussin(Authentication authentication){
        poussinService.grandirOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poussins/adultes")
    public void adultesPoussin(Authentication authentication){
        poussinService.adultesOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poussins/nourrirHier")
    public List<Poussin> nourrirHierAllPoussins(Authentication authentication){
        return poussinService.nourrirHierAllOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poussins/abreuveHier")
    public List<Poussin> abreuveHierAllPoussins(Authentication authentication){
        return poussinService.abreuveHierAllOfUtilisateur(authentication.getName());
    }

    @PostMapping("/poussins/passageJour")
    public List<Poussin> passageJourPoussins(Authentication authentication){
        return poussinService.passageJourOfUtilisateur(authentication.getName());
    }



    /*
    @GetMapping("/{id}")
    public ResponseEntity<Fermier> getFermierById(@PathVariable Long id) {
        Optional<Fermier> fermier = fermierService.getFermierById(id);
        return fermier.map(ResponseEntity::ok).orElseGet(() -> ResponseEntity.notFound().build());
    }

    @PostMapping
    public ResponseEntity<Fermier> createFermier(@RequestBody Fermier fermier) {
        Fermier createdFermier = fermierService.createFermier(fermier);
        return ResponseEntity.ok(createdFermier);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteFermier(@PathVariable Long id) {
        if (fermierService.getFermierById(id).isPresent()) {
            fermierService.deleteFermier(id);
            return ResponseEntity.noContent().build();
        } else {
            return ResponseEntity.notFound().build();
        }
    }
         */
}
