package fr.devweb.projet484i.repository;

import fr.devweb.projet484i.entity.Fermier;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;


public interface FermierRepository extends JpaRepository<Fermier, String> {
}
