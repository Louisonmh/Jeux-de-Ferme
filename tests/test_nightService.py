import requests
import time

# Base URL for the Spring Boot application
APP_URL = "http://localhost:8080"

from test_secu import auth_token, auth_token2, headers, headers2, get_fermier, get_fermier2

def test_changement_de_jour(headers, get_fermier):

    #On récupe les donnée avant mise à jour
    initial_vache_data = get_fermier["vache"]
    assert initial_vache_data["estVivante"] is True, f"Erreur pas de vache pour l'utilisateur: {get_fermier}"

    initial_vache = initial_vache_data
    initial_vache_age = initial_vache["age"]

    #attend un peu plus au cas ou
    time.sleep(60) 

    # Re-récupère les données après passage du jour
    response = requests.get(f"{APP_URL}/fermiers", headers=headers)
    assert response.status_code == 200, "Échec récupération fermier après passage du jour"

    fermier_apres = response.json()

    vache_apres = fermier_apres["vache"]
    assert initial_vache_age+1 == vache_apres["age"], "L'age n'a pas changé après évolution"


def test_changement_de_jour_2_joueur(headers, headers2, get_fermier, get_fermier2):

    #On récupe les donnée avant mise à jour
    initial_vache_data = get_fermier["vache"]
    assert initial_vache_data["estVivante"] is True, f"Erreur pas de vache pour l'utilisateur: {get_fermier}"

    initial_vache_data2 = get_fermier2["vache"]
    assert initial_vache_data2["estVivante"] is True, f"Erreur pas de vache pour l'utilisateur: {get_fermier}"

    initial_vache = initial_vache_data
    initial_vache_age = initial_vache["age"]

    initial_vache2 = initial_vache_data2
    initial_vache_age2 = initial_vache2["age"]

    #attend un peu plus au cas ou
    time.sleep(60) 

    # Re-récupère les données après passage du jour
    response = requests.get(f"{APP_URL}/fermiers", headers=headers)
    assert response.status_code == 200, "Échec récupération fermier après passage du jour"

    response2 = requests.get(f"{APP_URL}/fermiers", headers=headers2)
    assert response2.status_code == 200, "Échec récupération fermier après passage du jour"

    fermier_apres = response.json()
    fermier2_apres = response2.json()

    vache_apres = fermier_apres["vache"]
    vache2_apres = fermier2_apres["vache"]

    assert initial_vache_age+1 == vache_apres["age"], "L'age n'a pas changé après évolution"
    assert initial_vache_age2+1 == vache2_apres["age"], "L'age n'a pas changé après évolution"

    assert fermier_apres["vache"] != fermier2_apres["vache"], "Erreur"
    assert vache_apres["id"] != vache2_apres["id"], "Erreur"
    assert vache_apres != vache2_apres, "Erreur"


