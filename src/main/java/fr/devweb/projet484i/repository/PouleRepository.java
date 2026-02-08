package fr.devweb.projet484i.repository;

import fr.devweb.projet484i.entity.Poule;
import fr.devweb.projet484i.entity.Fermier;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;

public interface PouleRepository extends JpaRepository<Poule, Long> {
    Page<Poule> findAll(Pageable pageable);
    Page<Poule> findAllByUtilisateur(Fermier utilisateur, Pageable pageable);
}
