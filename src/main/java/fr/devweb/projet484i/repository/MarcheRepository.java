package fr.devweb.projet484i.repository;

import fr.devweb.projet484i.entity.Marche;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import java.util.List;

@Repository
public interface MarcheRepository extends JpaRepository<Marche, String> {
    List<Marche> findAll();

    // Méthode pour récupérer la moyenne pondérée par article
    @Query("SELECT m.moyennePonderee FROM Marche m WHERE m.articles = :articles")
    int getMoyennePondereeParArticle(@Param("articles") String articles);
    
    // Méthode pour récupérer la quantité tt par article
    @Query("SELECT m.quantiteRestante FROM Marche m WHERE m.articles = :articles")
    int getquantiteRestanteParArticle(@Param("articles") String articles);
}
