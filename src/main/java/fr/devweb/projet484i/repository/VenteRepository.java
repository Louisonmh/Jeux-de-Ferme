package fr.devweb.projet484i.repository;

import fr.devweb.projet484i.entity.Vente;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import org.springframework.data.jpa.repository.Query;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

import java.util.List;

@Repository
public interface VenteRepository extends JpaRepository<Vente, String> {
    Page<Vente> findAll(Pageable pageable);
    Page<Vente> findAllByVendeur(String vendeur, Pageable pageable);
    Page<Vente> findByArticlesOrderByPrixUnitaireAsc(String articles, Pageable pageable);;

    public interface MoyenneEtQuantiteParNomArticle {
        String getArticles();
        int getMoyennePonderee();
        int getQuantite();
    }

    @Query("SELECT v.articles AS articles, FLOOR(SUM(v.prixUnitaire * v.quantite) / SUM(v.quantite)) AS moyennePonderee, SUM(v.quantite) as quantite  FROM Vente v GROUP BY v.articles")
    List<MoyenneEtQuantiteParNomArticle> getMoyenneEtQuantiteParNomArticle();
}