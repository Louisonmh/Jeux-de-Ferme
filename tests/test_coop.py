import requests
import time
import pytest
import json

# Base URL for the Spring Boot application
APP_URL = "http://localhost:8080"

from test_secu import auth_token, headers, fermier_riche, fermier_pauvre, remise_vide, remise_plusieurs

@pytest.fixture
def fermier_sous_limite_achat(headers):
    # Makes sure user has 12 purchases left
    achats_response = requests.post(f"{APP_URL}/fermiers/setAchats/0", headers=headers)
    assert achats_response.status_code == 200, f"Failed to void purchases: {achats_response.text}"

@pytest.fixture
def fermier_au_dessus_limite_achat(headers):
    # Makes sure user has 12 purchases left
    achats_response = requests.post(f"{APP_URL}/fermiers/setAchats/12", headers=headers)
    assert achats_response.status_code == 200, f"Failed to void purchases: {achats_response.text}"

@pytest.fixture
def coop_pleine(headers):
    # Makes sure the coop has stock
    coop_response = requests.post(f"{APP_URL}/transactions/cooperative/remplir", headers=headers)
    assert coop_response.status_code == 200, f"Failed to fill coop: {coop_response.text}"

@pytest.fixture
def coop_vide(headers):
    # Makes sure the coop has stock
    coop_response = requests.post(f"{APP_URL}/transactions/cooperative/vider", headers=headers)
    assert coop_response.status_code == 200, f"Failed to empty coop: {coop_response.text}"

def test_achat_savon_coop_valide(headers, fermier_riche, fermier_sous_limite_achat, coop_pleine):
    # Buy soap
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    savon_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("savon")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttSavon"]
    achat = {"articles": "Savon", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 200, f"Failed to buy: {action_response.text}"

    # Verify the purchase succeeded
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttSavon"]
    assert updated_farm_data["ecus"] == ecus_response - 30
    assert updated_farm_data["nbAchat"] == achat_response + 3
    assert updated_farm_data["remise"].get("savon") == savon_response + 3
    assert updated_coop_data == coop_response - 3

def test_achat_savon_coop_pauvre(headers, fermier_pauvre, fermier_sous_limite_achat, coop_pleine):
    # Buy soap
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    savon_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("savon")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttSavon"]
    achat = {"articles": "Savon", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 400, f"Managed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttSavon"]
    assert updated_farm_data["ecus"] == ecus_response
    assert updated_farm_data["nbAchat"] == achat_response
    assert updated_farm_data["remise"].get("savon") == savon_response
    assert updated_coop_data == coop_response

def test_achat_savon_coop_plus_d_achats(headers, fermier_riche, fermier_au_dessus_limite_achat, coop_pleine):
    # Buy soap
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    savon_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("savon")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttSavon"]
    achat = {"articles": "Savon", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 400, f"Managed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttSavon"]
    assert updated_farm_data["ecus"] == ecus_response
    assert updated_farm_data["nbAchat"] == achat_response
    assert updated_farm_data["remise"].get("savon") == savon_response
    assert updated_coop_data == coop_response

def test_achat_savon_coop_vide(headers, fermier_riche, fermier_sous_limite_achat, coop_vide):
    # Buy soap
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    savon_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("savon")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttSavon"]
    achat = {"articles": "Savon", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 200, f"Managed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttSavon"]
    assert updated_farm_data["ecus"] == ecus_response
    assert updated_farm_data["nbAchat"] == achat_response
    assert updated_farm_data["remise"].get("savon") == savon_response
    assert updated_coop_data == coop_response

def test_achat_savon_coop_insuffisante(headers, fermier_riche, fermier_sous_limite_achat, coop_pleine):
    # Buy soap
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    savon_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("savon")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttSavon"]
    achat = {"articles": "Savon", "quantite": 6}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 200, f"Managed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttSavon"]
    assert updated_farm_data["ecus"] == ecus_response - 50
    assert updated_farm_data["nbAchat"] == achat_response + 5
    assert updated_farm_data["remise"].get("savon") == savon_response + 5
    assert updated_coop_data == coop_response - 5

def test_achat_seringue_coop_valide(headers, fermier_riche, fermier_sous_limite_achat, coop_pleine):
    # Buy syringe
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    seringue_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("seringue")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttSeringue"]
    achat = {"articles": "Seringue", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 200, f"Failed to buy: {action_response.text}"

    # Verify the purchase succeeded
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttSeringue"]
    assert updated_farm_data["ecus"] == ecus_response - 30
    assert updated_farm_data["nbAchat"] == achat_response + 3
    assert updated_farm_data["remise"].get("seringue") == seringue_response + 3
    assert updated_coop_data == coop_response - 3

def test_achat_seringue_coop_pauvre(headers, fermier_pauvre, fermier_sous_limite_achat, coop_pleine):
    # Buy syringe
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    seringue_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("seringue")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttSeringue"]
    achat = {"articles": "Seringue", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 400, f"Managed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttSeringue"]
    assert updated_farm_data["ecus"] == ecus_response
    assert updated_farm_data["nbAchat"] == achat_response
    assert updated_farm_data["remise"].get("seringue") == seringue_response
    assert updated_coop_data == coop_response

def test_achat_seringue_coop_plus_d_achats(headers, fermier_riche, fermier_au_dessus_limite_achat, coop_pleine):
    # Buy syringe
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    seringue_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("seringue")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttSeringue"]
    achat = {"articles": "Seringue", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 400, f"Managed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttSeringue"]
    assert updated_farm_data["ecus"] == ecus_response
    assert updated_farm_data["nbAchat"] == achat_response
    assert updated_farm_data["remise"].get("seringue") == seringue_response
    assert updated_coop_data == coop_response

def test_achat_seringue_coop_vide(headers, fermier_riche, fermier_sous_limite_achat, coop_vide):
    # Buy syringe
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    seringue_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("seringue")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttSeringue"]
    achat = {"articles": "Seringue", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 200, f"Managed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttSeringue"]
    assert updated_farm_data["ecus"] == ecus_response
    assert updated_farm_data["nbAchat"] == achat_response
    assert updated_farm_data["remise"].get("seringue") == seringue_response
    assert updated_coop_data == coop_response

def test_achat_seringue_coop_insuffisante(headers, fermier_riche, fermier_sous_limite_achat, coop_pleine):
    # Buy syringe
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    seringue_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("seringue")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttSeringue"]
    achat = {"articles": "Seringue", "quantite": 6}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 200, f"Managed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttSeringue"]
    assert updated_farm_data["ecus"] == ecus_response - 50
    assert updated_farm_data["nbAchat"] == achat_response + 5
    assert updated_farm_data["remise"].get("seringue") == seringue_response + 5
    assert updated_coop_data == coop_response - 5

def test_achat_paille_coop_valide(headers, fermier_riche, fermier_sous_limite_achat, coop_pleine):
    # Buy straw
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    paille_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("bottes_de_paille")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttPaille"]
    achat = {"articles": "Paille", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 200, f"Failed to buy: {action_response.text}"

    # Verify the purchase succeeded
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttPaille"]
    assert updated_farm_data["ecus"] == ecus_response - 30
    assert updated_farm_data["nbAchat"] == achat_response + 3
    assert updated_farm_data["remise"].get("bottes_de_paille") == paille_response + 3
    assert updated_coop_data == coop_response - 3

def test_achat_paille_coop_pauvre(headers, fermier_pauvre, fermier_sous_limite_achat, coop_pleine):
    # Buy straw
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    paille_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("bottes_de_paille")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttPaille"]
    achat = {"articles": "Paille", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 400, f"Managed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttPaille"]
    assert updated_farm_data["ecus"] == ecus_response
    assert updated_farm_data["nbAchat"] == achat_response
    assert updated_farm_data["remise"].get("bottes_de_paille") == paille_response
    assert updated_coop_data == coop_response

def test_achat_paille_coop_plus_d_achats(headers, fermier_riche, fermier_au_dessus_limite_achat, coop_pleine):
    # Buy straw
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    paille_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("bottes_de_paille")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttPaille"]
    achat = {"articles": "Paille", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 400, f"Managed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttPaille"]
    assert updated_farm_data["ecus"] == ecus_response
    assert updated_farm_data["nbAchat"] == achat_response
    assert updated_farm_data["remise"].get("bottes_de_paille") == paille_response
    assert updated_coop_data == coop_response

def test_achat_paille_coop_vide(headers, fermier_riche, fermier_sous_limite_achat, coop_vide):
    # Buy straw
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    paille_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("bottes_de_paille")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttPaille"]
    achat = {"articles": "Paille", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 200, f"Managed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttPaille"]
    assert updated_farm_data["ecus"] == ecus_response
    assert updated_farm_data["nbAchat"] == achat_response
    assert updated_farm_data["remise"].get("bottes_de_paille") == paille_response
    assert updated_coop_data == coop_response

def test_achat_paille_coop_insuffisante(headers, fermier_riche, fermier_sous_limite_achat, coop_pleine):
    # Buy straw
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    paille_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("bottes_de_paille")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttPaille"]
    achat = {"articles": "Paille", "quantite": 6}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 200, f"Managed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttPaille"]
    assert updated_farm_data["ecus"] == ecus_response - 50
    assert updated_farm_data["nbAchat"] == achat_response + 5
    assert updated_farm_data["remise"].get("bottes_de_paille") == paille_response + 5
    assert updated_coop_data == coop_response - 5

def test_achat_eau_coop_valide(headers, fermier_riche, fermier_sous_limite_achat, coop_pleine):
    # Buy water
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    eau_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("eau")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttEau"]
    achat = {"articles": "Eau", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 200, f"Failed to buy: {action_response.text}"

    # Verify the purchase succeeded
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttEau"]
    assert updated_farm_data["ecus"] == ecus_response - 30
    assert updated_farm_data["nbAchat"] == achat_response + 3
    assert updated_farm_data["remise"].get("eau") == eau_response + 3
    assert updated_coop_data == coop_response - 3

def test_achat_eau_coop_pauvre(headers, fermier_pauvre, fermier_sous_limite_achat, coop_pleine):
    # Buy water
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    eau_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("eau")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttEau"]
    achat = {"articles": "Eau", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 400, f"Managed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttEau"]
    assert updated_farm_data["ecus"] == ecus_response
    assert updated_farm_data["nbAchat"] == achat_response
    assert updated_farm_data["remise"].get("eau") == eau_response
    assert updated_coop_data == coop_response

def test_achat_eau_coop_plus_d_achats(headers, fermier_riche, fermier_au_dessus_limite_achat, coop_pleine):
    # Buy water
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    eau_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("eau")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttEau"]
    achat = {"articles": "Eau", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 400, f"Managed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttEau"]
    assert updated_farm_data["ecus"] == ecus_response
    assert updated_farm_data["nbAchat"] == achat_response
    assert updated_farm_data["remise"].get("eau") == eau_response
    assert updated_coop_data == coop_response

def test_achat_eau_coop_vide(headers, fermier_riche, fermier_sous_limite_achat, coop_vide):
    # Buy water
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    eau_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("eau")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttEau"]
    achat = {"articles": "Eau", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 200, f"Managed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttEau"]
    assert updated_farm_data["ecus"] == ecus_response
    assert updated_farm_data["nbAchat"] == achat_response
    assert updated_farm_data["remise"].get("eau") == eau_response
    assert updated_coop_data == coop_response

def test_achat_eau_coop_insuffisante(headers, fermier_riche, fermier_sous_limite_achat, coop_pleine):
    # Buy water
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    eau_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("eau")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttEau"]
    achat = {"articles": "Eau", "quantite": 6}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 200, f"Managed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttEau"]
    assert updated_farm_data["ecus"] == ecus_response - 50
    assert updated_farm_data["nbAchat"] == achat_response + 5
    assert updated_farm_data["remise"].get("eau") == eau_response + 5
    assert updated_coop_data == coop_response - 5

def test_achat_sacNourriture_coop_valide(headers, fermier_riche, fermier_sous_limite_achat, coop_pleine):
    # Buy food bag
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    sacNourriture_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("sac_nourriture")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttSacNourriture"]
    achat = {"articles": "SacNourriture", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 200, f"Failed to buy: {action_response.text}"

    # Verify the purchase succeeded
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttSacNourriture"]
    assert updated_farm_data["ecus"] == ecus_response - 30
    assert updated_farm_data["nbAchat"] == achat_response + 3
    assert updated_farm_data["remise"].get("sac_nourriture") == sacNourriture_response + 3
    assert updated_coop_data == coop_response - 3

def test_achat_sacNourriture_coop_pauvre(headers, fermier_pauvre, fermier_sous_limite_achat, coop_pleine):
    # Buy food bag
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    sacNourriture_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("sac_nourriture")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttSacNourriture"]
    achat = {"articles": "SacNourriture", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 400, f"Managed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttSacNourriture"]
    assert updated_farm_data["ecus"] == ecus_response
    assert updated_farm_data["nbAchat"] == achat_response
    assert updated_farm_data["remise"].get("sac_nourriture") == sacNourriture_response
    assert updated_coop_data == coop_response

def test_achat_sacNourriture_coop_plus_d_achats(headers, fermier_riche, fermier_au_dessus_limite_achat, coop_pleine):
    # Buy food bag
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    sacNourriture_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("sac_nourriture")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttSacNourriture"]
    achat = {"articles": "SacNourriture", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 400, f"Managed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttSacNourriture"]
    assert updated_farm_data["ecus"] == ecus_response
    assert updated_farm_data["nbAchat"] == achat_response
    assert updated_farm_data["remise"].get("sac_nourriture") == sacNourriture_response
    assert updated_coop_data == coop_response

def test_achat_sacNourriture_coop_vide(headers, fermier_riche, fermier_sous_limite_achat, coop_vide):
    # Buy food bag
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    sacNourriture_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("sac_nourriture")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttSacNourriture"]
    achat = {"articles": "SacNourriture", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 200, f"Managed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttSacNourriture"]
    assert updated_farm_data["ecus"] == ecus_response
    assert updated_farm_data["nbAchat"] == achat_response
    assert updated_farm_data["remise"].get("sac_nourriture") == sacNourriture_response
    assert updated_coop_data == coop_response

def test_achat_sacNourriture_coop_insuffisante(headers, fermier_riche, fermier_sous_limite_achat, coop_pleine):
    # Buy food bag
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    sacNourriture_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("sac_nourriture")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttSacNourriture"]
    achat = {"articles": "SacNourriture", "quantite": 6}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 200, f"Managed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttSacNourriture"]
    assert updated_farm_data["ecus"] == ecus_response - 50
    assert updated_farm_data["nbAchat"] == achat_response + 5
    assert updated_farm_data["remise"].get("sac_nourriture") == sacNourriture_response + 5
    assert updated_coop_data == coop_response - 5

def test_achat_lapinMale_coop_valide(headers, fermier_riche, fermier_sous_limite_achat, coop_pleine):
    # Buy male bunny
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    lapinMale_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("lapinsMales")
    clapier_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"].get("nbLapinsMales")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttLapinMale"]
    achat = {"articles": "LapinsMales", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 200, f"Failed to buy: {action_response.text}"

    # Verify the purchase succeeded
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttLapinMale"]
    assert updated_farm_data["ecus"] == ecus_response - 150
    assert updated_farm_data["nbAchat"] == achat_response + 3
    assert updated_farm_data["remise"].get("lapinsMales") == lapinMale_response + 3
    assert updated_farm_data["clapier"].get("nbLapinsMales") == clapier_response + 3
    assert updated_coop_data == coop_response - 3

def test_achat_lapinMale_coop_pauvre(headers, fermier_pauvre, fermier_sous_limite_achat, coop_pleine):
    # Buy male bunny
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    lapinMale_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("lapinsMales")
    clapier_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"].get("nbLapinsMales")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttLapinMale"]
    achat = {"articles": "LapinsMales", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 400, f"Managed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttLapinMale"]
    assert updated_farm_data["ecus"] == ecus_response
    assert updated_farm_data["nbAchat"] == achat_response
    assert updated_farm_data["remise"].get("lapinsMales") == lapinMale_response
    assert updated_farm_data["clapier"].get("nbLapinsMales") == clapier_response
    assert updated_coop_data == coop_response

def test_achat_lapinMale_coop_plus_d_achats(headers, fermier_riche, fermier_au_dessus_limite_achat, coop_pleine):
    # Buy male bunny
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    lapinMale_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("lapinsMales")
    clapier_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"].get("nbLapinsMales")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttLapinMale"]
    achat = {"articles": "LapinsMales", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 400, f"Managed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttLapinMale"]
    assert updated_farm_data["ecus"] == ecus_response
    assert updated_farm_data["nbAchat"] == achat_response
    assert updated_farm_data["remise"].get("lapinsMales") == lapinMale_response
    assert updated_farm_data["clapier"].get("nbLapinsMales") == clapier_response
    assert updated_coop_data == coop_response

def test_achat_lapinMale_coop_vide(headers, fermier_riche, fermier_sous_limite_achat, coop_vide):
    # Buy male bunny
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    lapinMale_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("lapinsMales")
    clapier_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"].get("nbLapinsMales")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttLapinMale"]
    achat = {"articles": "LapinsMales", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 200, f"Managed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttLapinMale"]
    assert updated_farm_data["ecus"] == ecus_response
    assert updated_farm_data["nbAchat"] == achat_response
    assert updated_farm_data["remise"].get("lapinsMales") == lapinMale_response
    assert updated_farm_data["clapier"].get("nbLapinsMales") == clapier_response
    assert updated_coop_data == coop_response

def test_achat_lapinMale_coop_insuffisante(headers, fermier_riche, fermier_sous_limite_achat, coop_pleine):
    # Buy male bunny
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    lapinMale_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("lapinsMales")
    clapier_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"].get("nbLapinsMales")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttLapinMale"]
    achat = {"articles": "LapinsMales", "quantite": 6}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 200, f"Managed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttLapinMale"]
    assert updated_farm_data["ecus"] == ecus_response - 250
    assert updated_farm_data["nbAchat"] == achat_response + 5
    assert updated_farm_data["remise"].get("lapinsMales") == lapinMale_response + 5
    assert updated_farm_data["clapier"].get("nbLapinsMales") == clapier_response + 5
    assert updated_coop_data == coop_response - 5

def test_achat_lapinFemelle_coop_valide(headers, fermier_riche, fermier_sous_limite_achat, coop_pleine):
    # Buy female bunny
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    lapinFemelle_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("lapinsFemelles")
    clapier_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"].get("nbLapinsFemelles")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttLapinFemelle"]
    achat = {"articles": "LapinsFemelles", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 200, f"Failed to buy: {action_response.text}"

    # Verify the purchase succeeded
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttLapinFemelle"]
    assert updated_farm_data["ecus"] == ecus_response - 150
    assert updated_farm_data["nbAchat"] == achat_response + 3
    assert updated_farm_data["remise"].get("lapinsFemelles") == lapinFemelle_response + 3
    assert updated_farm_data["clapier"].get("nbLapinsFemelles") == clapier_response + 3
    assert updated_coop_data == coop_response - 3

def test_achat_lapinFemelle_coop_pauvre(headers, fermier_pauvre, fermier_sous_limite_achat, coop_pleine):
    # Buy female bunny
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    lapinFemelle_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("lapinsFemelles")
    clapier_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"].get("nbLapinsFemelles")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttLapinFemelle"]
    achat = {"articles": "LapinsFemelles", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 400, f"Managed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttLapinFemelle"]
    assert updated_farm_data["ecus"] == ecus_response
    assert updated_farm_data["nbAchat"] == achat_response
    assert updated_farm_data["remise"].get("lapinsFemelles") == lapinFemelle_response
    assert updated_farm_data["clapier"].get("nbLapinsFemelles") == clapier_response
    assert updated_coop_data == coop_response

def test_achat_lapinFemelle_coop_plus_d_achats(headers, fermier_riche, fermier_au_dessus_limite_achat, coop_pleine):
    # Buy female bunny
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    lapinFemelle_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("lapinsFemelles")
    clapier_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"].get("nbLapinsFemelles")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttLapinFemelle"]
    achat = {"articles": "LapinsFemelles", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 400, f"Managed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttLapinFemelle"]
    assert updated_farm_data["ecus"] == ecus_response
    assert updated_farm_data["nbAchat"] == achat_response
    assert updated_farm_data["remise"].get("lapinsFemelles") == lapinFemelle_response
    assert updated_farm_data["clapier"].get("nbLapinsFemelles") == clapier_response
    assert updated_coop_data == coop_response

def test_achat_lapinFemelle_coop_vide(headers, fermier_riche, fermier_sous_limite_achat, coop_vide):
    # Buy female bunny
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    lapinFemelle_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("lapinsFemelles")
    clapier_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"].get("nbLapinsFemelles")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttLapinFemelle"]
    achat = {"articles": "LapinsFemelles", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 200, f"Managed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttLapinFemelle"]
    assert updated_farm_data["ecus"] == ecus_response
    assert updated_farm_data["nbAchat"] == achat_response
    assert updated_farm_data["remise"].get("lapinsFemelles") == lapinFemelle_response
    assert updated_farm_data["clapier"].get("nbLapinsFemelles") == clapier_response
    assert updated_coop_data == coop_response

def test_achat_lapinFemelle_coop_insuffisante(headers, fermier_riche, fermier_sous_limite_achat, coop_pleine):
    # Buy female bunny
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    lapinFemelle_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("lapinsFemelles")
    clapier_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"].get("nbLapinsFemelles")
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttLapinFemelle"]
    achat = {"articles": "LapinsFemelles", "quantite": 6}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 200, f"Managed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttLapinFemelle"]
    assert updated_farm_data["ecus"] == ecus_response - 250
    assert updated_farm_data["nbAchat"] == achat_response + 5
    assert updated_farm_data["remise"].get("lapinsFemelles") == lapinFemelle_response + 5
    assert updated_farm_data["clapier"].get("nbLapinsFemelles") == clapier_response + 5
    assert updated_coop_data == coop_response - 5

def test_achat_poule_coop_valide(headers, fermier_riche, fermier_sous_limite_achat, coop_pleine):
    # Buy hen
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    poule_response = len(requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json())
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttPoule"]
    achat = {"articles": "Poule", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 200, f"Failed to buy: {action_response.text}"

    # Verify the purchase succeeded
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttPoule"]
    assert updated_farm_data["ecus"] == ecus_response - 180
    assert updated_farm_data["nbAchat"] == achat_response + 3
    assert len(requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()) == poule_response + 3
    assert updated_coop_data == coop_response - 3

def test_achat_poule_coop_pauvre(headers, fermier_pauvre, fermier_sous_limite_achat, coop_pleine):
    # Buy hen
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    poule_response = len(requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json())
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttPoule"]
    achat = {"articles": "Poule", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 400, f"Failed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttPoule"]
    assert updated_farm_data["ecus"] == ecus_response
    assert updated_farm_data["nbAchat"] == achat_response
    assert len(requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()) == poule_response
    assert updated_coop_data == coop_response

def test_achat_poule_coop_plus_d_achats(headers, fermier_riche, fermier_au_dessus_limite_achat, coop_pleine):
    # Buy hen
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    poule_response = len(requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json())
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttPoule"]
    achat = {"articles": "Poule", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 400, f"Failed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttPoule"]
    assert updated_farm_data["ecus"] == ecus_response
    assert updated_farm_data["nbAchat"] == achat_response
    assert len(requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()) == poule_response
    assert updated_coop_data == coop_response

def test_achat_poule_coop_vide(headers, fermier_riche, fermier_sous_limite_achat, coop_vide):
    # Buy hen
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    poule_response = len(requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json())
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttPoule"]
    achat = {"articles": "Poule", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 200, f"Failed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttPoule"]
    assert updated_farm_data["ecus"] == ecus_response
    assert updated_farm_data["nbAchat"] == achat_response
    assert len(requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()) == poule_response
    assert updated_coop_data == coop_response

def test_achat_poule_coop_insuffisante(headers, fermier_riche, fermier_sous_limite_achat, coop_pleine):
    # Buy hen
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    poule_response = len(requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json())
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttPoule"]
    achat = {"articles": "Poule", "quantite": 6}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 200, f"Failed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttLapinFemelle"]
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttPoule"]
    assert updated_farm_data["ecus"] == ecus_response - 300
    assert updated_farm_data["nbAchat"] == achat_response + 5
    assert len(requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()) == poule_response + 5
    assert updated_coop_data == coop_response - 5

def test_achat_coq_coop_valide(headers, fermier_riche, fermier_sous_limite_achat, coop_pleine):
    # Buy rooster
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    coq_response = len(requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json())
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttCoq"]
    achat = {"articles": "Coq", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 200, f"Failed to buy: {action_response.text}"

    # Verify the purchase succeeded
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttCoq"]
    assert updated_farm_data["ecus"] == ecus_response - 150
    assert updated_farm_data["nbAchat"] == achat_response + 3
    assert len(requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()) == coq_response + 3
    assert updated_coop_data == coop_response - 3

def test_achat_coq_coop_pauvre(headers, fermier_pauvre, fermier_sous_limite_achat, coop_pleine):
    # Buy rooster
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    coq_response = len(requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json())
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttCoq"]
    achat = {"articles": "Coq", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 400, f"Failed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttCoq"]
    assert updated_farm_data["ecus"] == ecus_response
    assert updated_farm_data["nbAchat"] == achat_response
    assert len(requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()) == coq_response
    assert updated_coop_data == coop_response

def test_achat_coq_coop_plus_d_achats(headers, fermier_riche, fermier_au_dessus_limite_achat, coop_pleine):
    # Buy rooster
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    coq_response = len(requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json())
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttCoq"]
    achat = {"articles": "Coq", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 400, f"Failed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttCoq"]
    assert updated_farm_data["ecus"] == ecus_response
    assert updated_farm_data["nbAchat"] == achat_response
    assert len(requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()) == coq_response
    assert updated_coop_data == coop_response

def test_achat_coq_coop_vide(headers, fermier_riche, fermier_sous_limite_achat, coop_vide):
    # Buy rooster
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    coq_response = len(requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json())
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttCoq"]
    achat = {"articles": "Coq", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 200, f"Failed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttCoq"]
    assert updated_farm_data["ecus"] == ecus_response
    assert updated_farm_data["nbAchat"] == achat_response
    assert len(requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()) == coq_response
    assert updated_coop_data == coop_response

def test_achat_coq_coop_insuffisante(headers, fermier_riche, fermier_sous_limite_achat, coop_pleine):
    # Buy rooster
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    achat_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["nbAchat"]
    coq_response = len(requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json())
    coop_response = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttCoq"]
    achat = {"articles": "Coq", "quantite": 6}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/acheter", headers=headers, json=achat)
    assert action_response.status_code == 200, f"Failed to buy: {action_response.text}"

    # Verify the purchase failed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttLapinFemelle"]
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    updated_coop_data = requests.get(f"{APP_URL}/transactions/cooperative", headers=headers).json()["qttCoq"]
    assert updated_farm_data["ecus"] == ecus_response - 250
    assert updated_farm_data["nbAchat"] == achat_response + 5
    assert len(requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()) == coq_response + 5
    assert updated_coop_data == coop_response - 5

def test_vente_oeuf_coop_valide(headers, remise_plusieurs):
    # Sell egg
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    oeuf_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("oeuf")
    vente = {"articles": "Oeuf", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/vendre", headers=headers, json=vente)
    assert action_response.status_code == 200, f"Failed to sell: {action_response.text}"

    # Verify the sale succeeded
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["ecus"] == ecus_response + 24
    assert updated_farm_data["remise"].get("oeuf") == oeuf_response - 3

def test_vente_oeuf_coop_remise_vide(headers, remise_vide):
    # Sell egg
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    oeuf_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("oeuf")
    vente = {"articles": "Oeuf", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/vendre", headers=headers, json=vente)
    assert action_response.status_code == 200, f"Failed to sell: {action_response.text}"

    # Verify the sale succeeded
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["ecus"] == ecus_response
    assert updated_farm_data["remise"].get("oeuf") == oeuf_response

def test_vente_oeuf_coop_plus_que_possedes(headers, remise_plusieurs):
    # Sell egg
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    oeuf_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("oeuf")
    vente = {"articles": "Oeuf", "quantite": 6}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/vendre", headers=headers, json=vente)
    assert action_response.status_code == 200, f"Failed to sell: {action_response.text}"

    # Verify the sale succeeded
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["ecus"] == ecus_response + 40
    assert updated_farm_data["remise"].get("oeuf") == oeuf_response - 5

def test_vente_lait_coop_valide(headers, remise_plusieurs):
    # Sell milk
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    lait_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("litresLait")
    vente = {"articles": "Lait", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/vendre", headers=headers, json=vente)
    assert action_response.status_code == 200, f"Failed to sell: {action_response.text}"

    # Verify the sale succeeded
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["ecus"] == ecus_response + 6
    assert updated_farm_data["remise"].get("litresLait") == lait_response - 3

def test_vente_lait_coop_remise_vide(headers, remise_vide):
    # Sell milk
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    lait_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("litresLait")
    vente = {"articles": "Lait", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/vendre", headers=headers, json=vente)
    assert action_response.status_code == 200, f"Failed to sell: {action_response.text}"

    # Verify the sale succeeded
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["ecus"] == ecus_response
    assert updated_farm_data["remise"].get("litresLait") == lait_response

def test_vente_lait_coop_plus_que_possedes(headers, remise_plusieurs):
    # Sell milk
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    lait_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("litresLait")
    vente = {"articles": "Lait", "quantite": 6}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/vendre", headers=headers, json=vente)
    assert action_response.status_code == 200, f"Failed to sell: {action_response.text}"

    # Verify the sale succeeded
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["ecus"] == ecus_response + 10
    assert updated_farm_data["remise"].get("litresLait") == lait_response - 5

def test_vente_lapinMale_coop_valide(headers, remise_plusieurs):
    # Sell male bunny
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    lapin_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("lapinsMales")
    clapier_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"].get("nbLapinsMales")
    vente = {"articles": "LapinsMales", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/vendre", headers=headers, json=vente)
    assert action_response.status_code == 200, f"Failed to sell: {action_response.text}"

    # Verify the sale succeeded
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["ecus"] == ecus_response + 150
    assert updated_farm_data["remise"].get("lapinsMales") == lapin_response - 3
    assert updated_farm_data["clapier"].get("nbLapinsMales") == clapier_response - 3

def test_vente_lapinMale_coop_remise_vide(headers, remise_vide):
    # Sell male bunny
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    lapin_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("lapinsMales")
    clapier_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"].get("nbLapinsMales")
    vente = {"articles": "LapinsMales", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/vendre", headers=headers, json=vente)
    assert action_response.status_code == 200, f"Failed to sell: {action_response.text}"

    # Verify the sale succeeded
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["ecus"] == ecus_response
    assert updated_farm_data["remise"].get("lapinsMales") == lapin_response
    assert updated_farm_data["clapier"].get("nbLapinsMales") == clapier_response

def test_vente_lapinMale_coop_plus_que_possedes(headers, remise_plusieurs):
    # Sell male bunny
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    lapin_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("lapinsMales")
    clapier_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"].get("nbLapinsMales")
    vente = {"articles": "LapinsMales", "quantite": 6}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/vendre", headers=headers, json=vente)
    assert action_response.status_code == 200, f"Failed to sell: {action_response.text}"

    # Verify the sale succeeded
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["ecus"] == ecus_response + 250
    assert updated_farm_data["remise"].get("lapinsMales") == lapin_response - 5
    assert updated_farm_data["clapier"].get("nbLapinsMales") == clapier_response - 5

def test_vente_lapinFemelle_coop_valide(headers, remise_plusieurs):
    # Sell female bunny
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    lapin_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("lapinsFemelles")
    clapier_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"].get("nbLapinsFemelles")
    vente = {"articles": "LapinsFemelles", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/vendre", headers=headers, json=vente)
    assert action_response.status_code == 200, f"Failed to sell: {action_response.text}"

    # Verify the sale succeeded
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["ecus"] == ecus_response + 150
    assert updated_farm_data["remise"].get("lapinsFemelles") == lapin_response - 3
    assert updated_farm_data["clapier"].get("nbLapinsFemelles") == clapier_response - 3

def test_vente_lapinFemelle_coop_remise_vide(headers, remise_vide):
    # Sell female bunny
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    lapin_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("lapinsFemelles")
    clapier_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"].get("nbLapinsFemelles")
    vente = {"articles": "LapinsFemelles", "quantite": 3}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/vendre", headers=headers, json=vente)
    assert action_response.status_code == 200, f"Failed to sell: {action_response.text}"

    # Verify the sale succeeded
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["ecus"] == ecus_response
    assert updated_farm_data["remise"].get("lapinsFemelles") == lapin_response
    assert updated_farm_data["clapier"].get("nbLapinsFemelles") == clapier_response

def test_vente_lapinFemelle_coop_plus_que_possedes(headers, remise_plusieurs):
    # Sell female bunny
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["ecus"]
    lapin_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("lapinsFemelles")
    clapier_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"].get("nbLapinsFemelles")
    vente = {"articles": "LapinsFemelles", "quantite": 6}
    action_response = requests.post(f"{APP_URL}/transactions/cooperative/vendre", headers=headers, json=vente)
    assert action_response.status_code == 200, f"Failed to sell: {action_response.text}"

    # Verify the sale succeeded
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["ecus"] == ecus_response + 250
    assert updated_farm_data["remise"].get("lapinsFemelles") == lapin_response - 5
    assert updated_farm_data["clapier"].get("nbLapinsFemelles") == clapier_response - 5
