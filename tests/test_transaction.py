import requests
import time
import pytest
import json

# Base URL for the Spring Boot application
APP_URL = "http://localhost:8080"

from test_secu import auth_token, auth_token2, headers, headers2

@pytest.fixture
def prepare_fermiers_pour_bagarre(headers, headers2):

    # === Fermier 1 ===
    assert requests.post(f"{APP_URL}/fermiers/poules/add/3", headers=headers).status_code == 200
    assert requests.post(f"{APP_URL}/fermiers/clapier/adultes/femelles/add/5", headers=headers).status_code == 200
    assert requests.post(f"{APP_URL}/fermiers/clapier/adultes/males/add/5", headers=headers).status_code == 200
    assert requests.post(f"{APP_URL}/fermiers/add1Coq", headers=headers).status_code == 200

    # === Fermier 2 ===
    assert requests.post(f"{APP_URL}/fermiers/poules/add/3", headers=headers2).status_code == 200
    assert requests.post(f"{APP_URL}/fermiers/clapier/adultes/femelles/add/4", headers=headers2).status_code == 200
    assert requests.post(f"{APP_URL}/fermiers/clapier/adultes/males/add/4", headers=headers2).status_code == 200
    assert requests.post(f"{APP_URL}/fermiers/coqs/add/2", headers=headers2).status_code == 200

    print(f"poules fermier1 {len(requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json())}") 
    print( f"coqs fermier1 {len(requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json())}")
    print( f"lapinsMales fermier1 {requests.get(f"{APP_URL}/fermiers/clapier", headers=headers).json()["nbLapinsMales"]}")
    print( f"lapinsFemelles fermier1 {requests.get(f"{APP_URL}/fermiers/clapier", headers=headers).json()["nbLapinsFemelles"]}")
    print( f"poules fermier2 {len(requests.get(f"{APP_URL}/fermiers/poules", headers=headers2).json())}")
    print( f"coqs fermier2 {len(requests.get(f"{APP_URL}/fermiers/coqs", headers=headers2).json())}")
    print( f"lapinsMales fermier2 {requests.get(f"{APP_URL}/fermiers/clapier", headers=headers2).json()["nbLapinsMales"]}")
    print( f"lapinsFemelles fermier2 {requests.get(f"{APP_URL}/fermiers/clapier", headers=headers2).json()["nbLapinsFemelles"]}")


@pytest.fixture
def fermiers_ont_vendu(prepare_fermiers_pour_bagarre, headers, headers2):

    headers_json1 = {**headers, "Content-Type": "application/json"}
    headers_json2 = {**headers2, "Content-Type": "application/json"}

    ventes_fermier1 = [
        {"articles": "Poule", "prixUnitaire": 10, "quantite": 3},
        {"articles": "LapinsMales", "prixUnitaire": 15, "quantite": 2},
        {"articles": "LapinsFemelles", "prixUnitaire": 20, "quantite": 3},
        {"articles": "Coq", "prixUnitaire": 5, "quantite": 3},
    ]

    ventes_fermier2 = [
        {"articles": "Poule", "prixUnitaire": 5, "quantite": 5},
        {"articles": "LapinsMales", "prixUnitaire": 10, "quantite": 2},
        {"articles": "LapinsFemelles", "prixUnitaire": 2, "quantite":4},
        {"articles": "Coq", "prixUnitaire": 20, "quantite": 1},
    ]

    for vente in ventes_fermier1:
        r = requests.post(f"{APP_URL}/transactions/marche/miseEnVente", headers=headers_json1, json=vente)
        assert r.status_code == 200, f"Erreur vente fermier1: {r.text}"

    for vente in ventes_fermier2:
        r = requests.post(f"{APP_URL}/transactions/marche/miseEnVente", headers=headers_json2, json=vente)
        assert r.status_code == 200, f"Erreur vente fermier2: {r.text}"


def test_get_ventes_marche(headers):
    # Tester la première page avec une taille de 2 éléments
    response = requests.get(f"{APP_URL}/transactions/ventes?page=0&size=2", headers=headers)
    assert response.status_code == 200, f"Échec de la récupération des ventes: {response.text}"

    ventes_json = response.json()
    assert isinstance(ventes_json, dict), "Les ventes doivent être renvoyées sous forme de dictionnaire."
    
    # Vérification des informations sur la page
    assert "content" in ventes_json, "La page des ventes doit contenir des informations sur le contenu."
    assert "totalElements" in ventes_json, "La page des ventes doit contenir des informations sur le nombre total d'éléments."
    
    # Vérification que le contenu est une liste
    assert isinstance(ventes_json["content"], list), "Le contenu des ventes doit être une liste."
    assert len(ventes_json["content"]) <= 2, "Le nombre d'éléments dans la page ne doit pas dépasser la taille de la page."


def test_statistiques_marche(headers, headers2, prepare_fermiers_pour_bagarre, fermiers_ont_vendu):
    time.sleep(35)

     # 1. Afficher les animaux du fermier 1
    response_animaux_1 = requests.get(f"{APP_URL}/fermiers/clapier", headers=headers)
    response_poules_1 = requests.get(f"{APP_URL}/fermiers/poules", headers=headers)
    response_coqs_1 = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers)
    print("\n [Fermier 1] Animaux restants :")
    print(f"- Clapier : {response_animaux_1.json()}")
    print(f"- Poules : {len(response_poules_1.json())} poules")
    print(f"- Coqs : {len(response_coqs_1.json())} coqs")

    # 2. Afficher les animaux du fermier 2
    response_animaux_2 = requests.get(f"{APP_URL}/fermiers/clapier", headers=headers2)
    response_poules_2 = requests.get(f"{APP_URL}/fermiers/poules", headers=headers2)
    response_coqs_2 = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers2)
    print("\n [Fermier 2] Animaux restants :")
    print(f"- Clapier : {response_animaux_2.json()}")
    print(f"- Poules : {len(response_poules_2.json())} poules")
    print(f"- Coqs : {len(response_coqs_2.json())} coqs")

    # 3. Afficher les ventes de chaque fermier
    response_ventes = requests.get(f"{APP_URL}/transactions/ventes", headers=headers)
    ventes = response_ventes.json().get("content", [])


    print("\n Total Ventes :")
    for vente in ventes:
        print(f"- {vente['quantite']}x {vente['articles']} à {vente['prixUnitaire']} ecus")

    response = requests.get(f"{APP_URL}/transactions/marche", headers=headers)
    assert response.status_code == 200, f"Échec récupération marché: {response.text}"

    marche = response.json()

    print("\n Stat du marché:")
    for item in marche:
        print(f"Article: {item['articles']}, Moyenne pondérée: {item['moyennePonderee']}")

    assert "articles" in marche[0]
    assert "moyennePonderee" in marche[0]



def test_achat_animaux_marche(headers, headers2):

    # Récupérer l'état initial
    response_clapier_before = requests.get(f"{APP_URL}/fermiers/clapier", headers=headers2)
    response_poules_before = requests.get(f"{APP_URL}/fermiers/poules", headers=headers2)
    response_coqs_before = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers2)
    response_acheteur = requests.get(f"{APP_URL}/fermiers", headers=headers2)
    response_vendeur = requests.get(f"{APP_URL}/fermiers", headers=headers)

    nb_poules_before = len(response_poules_before.json())
    nb_coqs_before = len(response_coqs_before.json())
    nb_males_before = response_clapier_before.json()["nbLapinsMales"]
    nb_femelles_before = response_clapier_before.json()["nbLapinsFemelles"]

    argent_acheteur_before = response_acheteur.json()["ecus"]
    argent_vendeur_before = response_vendeur.json()["ecus"]

    print("\n  État avant l'achat :")
    print(f"- 🐔 Poules avant: {nb_poules_before}")
    print(f"- 🐔 Coqs avant: {nb_coqs_before}")
    print(f"- 🐇 Mâles avant: {nb_males_before}")
    print(f"- 🐇 Femelles avant: {nb_femelles_before}")
    print(f"- 🤓 Acheteur avant: {argent_acheteur_before}")
    print(f"- 🫣 Vendeur avant: {argent_vendeur_before}")


    # achat de 3 poules, 2 lapins males, 1 femelle
    achats = [
        {"articles": "Poule", "quantite": 3},
        {"articles": "LapinsMales", "quantite": 2},
        {"articles": "LapinsFemelles", "quantite": 1},
        {"articles": "Coq", "quantite": 1}
    ]

    for achat in achats:
        response = requests.post(f"{APP_URL}/transactions/marche/acheter", headers={**headers2, "Content-Type": "application/json"}, json=achat)
        assert response.status_code == 200, f"Achat échoué: {response.text}"

    # Vérifier le nouvel état
    response_clapier_after = requests.get(f"{APP_URL}/fermiers/clapier", headers=headers2)
    response_poules_after = requests.get(f"{APP_URL}/fermiers/poules", headers=headers2)
    response_coqs_after = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers2)
    response_acheteur = requests.get(f"{APP_URL}/fermiers", headers=headers2)
    response_vendeur = requests.get(f"{APP_URL}/fermiers", headers=headers)

    nb_poules_after = len(response_poules_after.json())
    nb_coqs_after = len(response_coqs_after.json())
    nb_femelles_after = response_clapier_after.json()["nbLapinsFemelles"]
    nb_males_after = response_clapier_after.json()["nbLapinsMales"]

    argent_acheteur_after = response_acheteur.json()["ecus"]
    argent_vendeur_after = response_vendeur.json()["ecus"]

    print("\n  État après l'achat :")
    print(f"- 🐔 Poules après: {nb_poules_after}")
    print(f"- 🐔 Coqs après: {nb_coqs_after}")
    print(f"- 🐇 Mâles après: {nb_males_after}")
    print(f"- 🐇 Femelles après: {nb_femelles_after}")
    print(f"- 🤓 Acheteur après: {argent_acheteur_after}")
    print(f"- 🫣 Vendeur après: {argent_vendeur_after}")


    # Vérification de la réception des animaux
    assert nb_poules_after == nb_poules_before + 3, "L'acheteur devrait avoir 3 poules de plus"
    assert nb_males_after == nb_males_before + 2, "L'acheteur devrait avoir 2 lapins mâles de plus"
    assert nb_femelles_after == nb_femelles_before + 1, "L'acheteur devrait avoir 1 lapin femelle de plus"
    assert nb_coqs_after == nb_coqs_before + 1 , "L'acheteur devrait avoir 0 coqs de plus"

    # On récupère les prix du marché
    response_marche = requests.get(f"{APP_URL}/transactions/marche", headers=headers)
    assert response_marche.status_code == 200, f"Échec récupération marché: {response_marche.text}"

    marche = {el["articles"]: el["moyennePonderee"] for el in response_marche.json()}

    montant_total = (
        achats[0]["quantite"] * marche["Poule"] +
        achats[1]["quantite"] * marche["LapinsMales"] +
        achats[2]["quantite"] * marche["LapinsFemelles"] +
        achats[3]["quantite"] * marche["Coq"]
    )

    assert argent_vendeur_after == pytest.approx(argent_vendeur_before + montant_total, 0.01), (
        f"Le vendeur aurait dû gagner {montant_total} écus. Avant: {argent_vendeur_before}, Après: {argent_vendeur_after}"
    )

    # Vérification des écus (approx permet de tolérer les petites variations dues aux arrondis)
    assert argent_acheteur_after == pytest.approx(argent_acheteur_before - montant_total, 0.01), (
        f"- Poules avant: {nb_poules_before}, après: {nb_poules_after}"
    )


    print("\n Achat vérifié avec succès.")
    print(f"- Poules avant: {nb_poules_before}, après: {nb_poules_after}")
    print(f"- Coqs avant: {nb_coqs_before}, après: {nb_coqs_after}")
    print(f"- Mâles avant: {nb_males_before}, après: {nb_males_after}")
    print(f"- Femelles avant: {nb_femelles_before}, après: {nb_femelles_after}")
    print(f"- Acheteur avant: {argent_acheteur_before}, après: {argent_acheteur_after}")
    print(f"- Vendeur avant: {argent_vendeur_before}, après: {argent_vendeur_after}")


