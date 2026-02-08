package fr.devweb.projet484i.repository;

import fr.devweb.projet484i.entity.Coq;
import fr.devweb.projet484i.entity.Fermier;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CoqRepository extends JpaRepository<Coq, Long> {
    Page<Coq> findAll(Pageable pageable);
    Page<Coq> findAllByUtilisateur(Fermier utilisateur, Pageable pageable);
}
