package fr.devweb.projet484i.controller;

import org.springframework.security.core.Authentication;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.oauth2.core.user.OAuth2User;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import fr.devweb.projet484i.service.UserService;

import org.springframework.security.oauth2.server.resource.authentication.JwtAuthenticationToken;

import java.util.Map;

@RestController
@PreAuthorize("isAuthenticated()")
public class UserController {
    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    @GetMapping("/user")
    public Map<String, Object> user(Authentication authentication) {
        if (authentication.getPrincipal() instanceof OAuth2User) {
            OAuth2User oauthUser = (OAuth2User) authentication.getPrincipal();
            return Map.of(
                "username", userService.getUsername(authentication),
                "roles", userService.getRoles(authentication),
                "avatar_url", oauthUser.getAttribute("avatar_url") // Récupère l'URL de l'avatar
            );
        } else {
            return Map.of(
                "username", userService.getUsername(authentication),
                "roles", userService.getRoles(authentication),
                "avatar_url", "/images/default-avatar.png" // URL par défaut si non OAuth2
            );
        }
    }

    @GetMapping("/admin")
    @PreAuthorize("hasRole('ADMIN')") // ✅ Seuls les admins OAuth peuvent accéder
    public Map<String, Object> adminOnly() {
        return Map.of("message", "Admin endpoint accessible");
    }
}