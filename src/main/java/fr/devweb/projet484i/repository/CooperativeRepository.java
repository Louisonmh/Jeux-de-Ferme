package fr.devweb.projet484i.repository;

import fr.devweb.projet484i.entity.Cooperative;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;


public interface CooperativeRepository extends JpaRepository<Cooperative, String> {
}