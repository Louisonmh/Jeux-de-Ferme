package fr.devweb.projet484i.repository;

import fr.devweb.projet484i.entity.Statistique;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;


public interface StatistiqueRepository extends JpaRepository<Statistique, Long> {
}