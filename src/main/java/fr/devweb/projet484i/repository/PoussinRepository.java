package fr.devweb.projet484i.repository;

import fr.devweb.projet484i.entity.Poussin;
import fr.devweb.projet484i.entity.Fermier;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;

public interface PoussinRepository extends JpaRepository<Poussin, Long> {
    Page<Poussin> findAll(Pageable pageable);
    Page<Poussin> findAllByUtilisateur(Fermier utilisateur, Pageable pageable);
}
