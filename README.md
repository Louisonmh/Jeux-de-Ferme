# A faire pour que le serveur se lance
export MY_GITHUB_PAT=tagada\
export BASE_URL="https://${CODESPACE_NAME}-8080.app.github.dev"

# Compiler
mvn clean install

# Lancer le serveur
mvn spring-boot:run

# Lancer tous les tests
pytest tests

# Lancer les tests d'un fichier en particulier
pytest tests/nomFichier.py

# Lancer un seul test
pytest tests/nomFichier.py::nomTest

# Créer une branche
git checkout -b nomBranche

# Voir sur quelle branche on est
git branch

# Changer la branche sur laquelle on est
git checkout nomBranche

# Commit sur la branche voulue
git stage et git commit normalement
git push origin nomBranche