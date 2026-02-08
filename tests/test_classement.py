import requests
import pytest
import datetime

# Base URL for the Spring Boot application
APP_URL = "http://localhost:8080"

from test_secu import auth_token, headers, auth_token2, headers2

def test_classement_ecus(headers, headers2):
    fermier1_response = requests.get(f"{APP_URL}/fermiers", headers=headers)
    fermier2_response = requests.get(f"{APP_URL}/fermiers", headers=headers2)
    requests.post(f"{APP_URL}/fermiers/addEcus/{500}", headers=headers)
    calcul = requests.post(f"{APP_URL}/classement/calculClassement", headers=headers)
    #assert calcul.status_code == 200, f"ta grosse mere : {calcul.text}"
    classement_ecu = requests.get(f"{APP_URL}/classement/triEcus", headers=headers)
    assert classement_ecu.status_code == 200, f"Failed to sort classement: {classement_ecu.text}"

    classement = classement_ecu.json()
    print("\n")
    for i in range(len(classement)):
        print(classement[i].get("nomUtilisateur"))
        print(f"point ecus : {classement[i].get("statistique").get("pointEcus")}")
        print(f"ecus : {classement[i].get("ecus")}")

def test_classement_prod(headers, headers2):
    fermier1_response = requests.get(f"{APP_URL}/fermiers", headers=headers)
    fermier2_response = requests.get(f"{APP_URL}/fermiers", headers=headers2)
    requests.post(f"{APP_URL}/fermiers/remise/incOeufs/{10}", headers=headers2)
    calcul = requests.post(f"{APP_URL}/classement/calculClassement", headers=headers)
    #assert calcul.status_code == 200, f"ta grosse mere : {calcul.text}"
    classement_prod = requests.get(f"{APP_URL}/classement/triProd", headers=headers)
    assert classement_prod.status_code == 200, f"Failed to sort classement: {classement_prod.text}"

    classement = classement_prod.json()
    print("\n")
    for i in range(len(classement)):
        print(classement[i].get("nomUtilisateur"))
        print(f"point prod : {classement[i].get("statistique").get("pointProd")}")

def test_classement_nego(headers, headers2):
    fermier1_response = requests.get(f"{APP_URL}/fermiers", headers=headers)
    fermier2_response = requests.get(f"{APP_URL}/fermiers", headers=headers2)
    vente = requests.post(f"{APP_URL}/classement/addVenteMarche/{20}", headers=headers2)
    assert vente.status_code == 200, f"{calcul.text}"
    calcul = requests.post(f"{APP_URL}/classement/calculClassement", headers=headers)
    #assert calcul.status_code == 200, f"ta grosse mere : {calcul.text}"
    classement_nego = requests.get(f"{APP_URL}/classement/triNego", headers=headers)
    assert classement_nego.status_code == 200, f"Failed to sort classement: {classement_nego.text}"

    classement = classement_nego.json()
    print("\n")
    for i in range(len(classement)):
        print(classement[i].get("nomUtilisateur"))
        print(f"point nego : {classement[i].get("statistique").get("pointNego")}")
        print(f"vente marche : {classement[i].get("statistique").get("venteMarche")}")

def test_classement_global(headers, headers2):
    fermier1_response = requests.get(f"{APP_URL}/fermiers", headers=headers)
    fermier2_response = requests.get(f"{APP_URL}/fermiers", headers=headers2)
    calcul = requests.post(f"{APP_URL}/classement/calculClassement", headers=headers)
    #assert calcul.status_code == 200, f"ta grosse mere : {calcul.text}"
    classement_nego = requests.get(f"{APP_URL}/classement/triGlobal", headers=headers)
    assert classement_nego.status_code == 200, f"Failed to sort classement: {classement_nego.text}"

    classement = classement_nego.json()
    print("\n")
    for i in range(len(classement)):
        print(classement[i].get("nomUtilisateur"))
        print(f"point globale : {classement[i].get("statistique").get("pointGlobal")}")