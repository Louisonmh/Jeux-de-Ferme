package fr.devweb.projet484i.controller;

import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import io.jsonwebtoken.security.Keys;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.PathVariable;

import java.security.Key;
import java.util.Date;
import java.util.List;

import javax.crypto.SecretKey;

@RestController
@RequestMapping("/auth")
public class TestAuthController {

    public static final SecretKey SECRET_KEY = Keys.secretKeyFor(SignatureAlgorithm.HS256); // 🔥 Génère une clé sécurisée

    @GetMapping("/test-token/{username}")
    public String getTestToken(@PathVariable String username) {
        return Jwts.builder()
                .setSubject(username)
                .claim("authorities", List.of("ROLE_ADMIN"))
                .setIssuedAt(new Date())
                .setExpiration(new Date(System.currentTimeMillis() + 3600000)) // 1h de validité
                .signWith(SECRET_KEY)
                .compact();
    }
}
