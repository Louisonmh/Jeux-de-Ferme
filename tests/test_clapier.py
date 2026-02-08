import requests
import pytest

# Base URL for the Spring Boot application
APP_URL = "http://localhost:8080"

from test_secu import auth_token, headers, fermier_pauvre, fermier_riche, remise_pleine, remise_vide

@pytest.fixture
def clapier_plein(headers):
    remplir_response = requests.post(f"{APP_URL}/fermiers/clapier/remplir", headers=headers)
    assert remplir_response.status_code == 200, f"Failed to fill: {remplir_response.text}"

@pytest.fixture
def clapier_max(headers):
    remplir_response = requests.post(f"{APP_URL}/fermiers/clapier/remplirMax", headers=headers)
    assert remplir_response.status_code == 200, f"Failed to fill: {remplir_response.text}"

@pytest.fixture
def clapier_vide(headers):
    vider_response = requests.post(f"{APP_URL}/fermiers/clapier/vider", headers=headers)
    assert vider_response.status_code == 200, f"Failed to empty: {vider_response.text}"

@pytest.fixture
def adultes_assoiffes(headers):
    assoiffer_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/assoiffer", headers=headers)
    assert assoiffer_response.status_code == 200, f"Failed to starve: {assoiffer_response.text}"

@pytest.fixture
def adultes_abreuves(headers, fermier_riche):
    abreuver_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/abreuver", headers=headers)
    assert abreuver_response.status_code == 200, f"Failed to starve: {abreuver_response.text}"

@pytest.fixture
def adultes_affames(headers):
    affamer_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/affamer", headers=headers)
    assert affamer_response.status_code == 200, f"Failed to starve: {affamer_response.text}"

@pytest.fixture
def adultes_nourris(headers, fermier_riche):
    nourrir_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/nourrir", headers=headers)
    assert nourrir_response.status_code == 200, f"Failed to starve: {nourrir_response.text}"

@pytest.fixture
def adultes_sales(headers):
    salir_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/salir", headers=headers)
    assert salir_response.status_code == 200, f"Failed to starve: {salir_response.text}"

@pytest.fixture
def adultes_propres(headers, fermier_riche):
    propres_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/nettoyer", headers=headers)
    assert propres_response.status_code == 200, f"Failed to starve: {propres_response.text}"

@pytest.fixture
def adultes_malades(headers):
    malades_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/malades", headers=headers)
    assert malades_response.status_code == 200, f"Failed to starve: {malades_response.text}"

@pytest.fixture
def adultes_sains(headers, fermier_riche):
    soigner_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/soigner", headers=headers)
    assert soigner_response.status_code == 200, f"Failed to starve: {soigner_response.text}"

@pytest.fixture
def enfants_assoiffes(headers):
    assoiffer_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/assoiffer", headers=headers)
    assert assoiffer_response.status_code == 200, f"Failed to starve: {assoiffer_response.text}"

@pytest.fixture
def enfants_abreuves(headers, fermier_riche):
    abreuver_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/abreuver", headers=headers)
    assert abreuver_response.status_code == 200, f"Failed to starve: {abreuver_response.text}"

@pytest.fixture
def enfants_affames(headers):
    affamer_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/affamer", headers=headers)
    assert affamer_response.status_code == 200, f"Failed to starve: {affamer_response.text}"

@pytest.fixture
def enfants_nourris(headers, fermier_riche):
    nourrir_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/nourrir", headers=headers)
    assert nourrir_response.status_code == 200, f"Failed to starve: {nourrir_response.text}"

@pytest.fixture
def enfants_sales(headers):
    salir_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/salir", headers=headers)
    assert salir_response.status_code == 200, f"Failed to starve: {salir_response.text}"

@pytest.fixture
def enfants_propres(headers, fermier_riche):
    propres_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/nettoyer", headers=headers)
    assert propres_response.status_code == 200, f"Failed to starve: {propres_response.text}"

@pytest.fixture
def enfants_malades(headers):
    malades_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/malades", headers=headers)
    assert malades_response.status_code == 200, f"Failed to starve: {malades_response.text}"

@pytest.fixture
def enfants_sains(headers, fermier_riche):
    soigner_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/soigner", headers=headers)
    assert soigner_response.status_code == 200, f"Failed to starve: {soigner_response.text}"

def test_nourrir_adultes(headers, adultes_affames, fermier_riche, clapier_plein):
    # Feed bunnies
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    nourrir_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/nourrir", headers=headers)
    assert nourrir_response.status_code == 200, f"Failed to feed: {nourrir_response.text}"

    # Verify the bunnies are fed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("adultesNourris") == True
    assert updated_farm_data["ecus"] == ecus_response.get("ecus") - 5

def test_nourrir_adultes_deja_nourris(headers, adultes_nourris, fermier_riche, clapier_plein):
    # Feed bunnies
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    nourrir_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/nourrir", headers=headers)
    assert nourrir_response.status_code == 200, f"Failed to starve: {nourrir_response.text}"

    # Verify the bunnies are fed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["ecus"] == ecus_response.get("ecus")

def test_nourrir_adultes_pauvre(headers, adultes_affames, fermier_pauvre, clapier_plein):
    # Feed bunnies
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    nourrir_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/nourrir", headers=headers)
    assert nourrir_response.status_code == 200, f"Failed to starve: {nourrir_response.text}"

    # Verify the bunnies are fed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("adultesNourris") == False
    assert updated_farm_data["ecus"] == ecus_response.get("ecus")

def test_nourrir_sac_adultes(headers, adultes_affames, remise_pleine, clapier_plein):
    # Feed bunnies
    remise_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
    nourrir_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/nourrirSac", headers=headers)
    assert nourrir_response.status_code == 200, f"Failed to feed: {nourrir_response.text}"

    # Verify the bunnies are fed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("adultesNourris") == True
    assert updated_farm_data["remise"].get("sac_nourriture") == remise_response.get("sac_nourriture") - 1

def test_nourrir_adultes_deja_nourris_sac(headers, adultes_nourris, remise_pleine, clapier_plein):
    # Feed bunnies
    remise_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
    nourrir_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/nourrirSac", headers=headers)
    assert nourrir_response.status_code == 200, f"Failed to starve: {nourrir_response.text}"

    # Verify the bunnies are fed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["remise"].get("sac_nourriture") == remise_response.get("sac_nourriture")

def test_nourrir_adultes_sac_pauvre(headers, adultes_affames, remise_vide, clapier_plein):
    # Feed bunnies
    remise_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
    nourrir_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/nourrirSac", headers=headers)
    assert nourrir_response.status_code == 200, f"Failed to starve: {nourrir_response.text}"

    # Verify the bunnies are fed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("adultesNourris") == False
    assert updated_farm_data["remise"].get("sac_nourriture") == remise_response.get("sac_nourriture")

def test_abreuver_adultes(headers, adultes_assoiffes, fermier_riche, clapier_plein):
    # Give bunnies water
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    abreuver_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/abreuver", headers=headers)
    assert abreuver_response.status_code == 200, f"Failed: {abreuver_response.text}"

    # Verify the bunnies drank
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("adultesAbreuves") == True
    assert updated_farm_data["ecus"] == ecus_response.get("ecus") - 2

def test_abreuver_adultes_deja_abreuves(headers, adultes_abreuves, fermier_riche, clapier_plein):
    # Give bunnies water
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    abreuver_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/abreuver", headers=headers)
    assert abreuver_response.status_code == 200, f"Failed: {abreuver_response.text}"

    # Verify the bunnies drank
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["ecus"] == ecus_response.get("ecus")

def test_abreuver_adultes_pauvre(headers, adultes_assoiffes, fermier_pauvre, clapier_plein):
    # Give bunnies water
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    abreuver_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/abreuver", headers=headers)
    assert abreuver_response.status_code == 200, f"Failed: {abreuver_response.text}"

    # Verify the bunnies drank
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("adultesAbreuves") == False
    assert updated_farm_data["ecus"] == ecus_response.get("ecus")

def test_abreuver_seau_adultes(headers, adultes_assoiffes, remise_pleine, clapier_plein):
    # Give bunnies water
    remise_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
    abreuver_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/abreuverEau", headers=headers)
    assert abreuver_response.status_code == 200, f"Failed: {abreuver_response.text}"

    # Verify the bunnies drank
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("adultesAbreuves") == True
    assert updated_farm_data["remise"].get("eau") == remise_response.get("eau") - 1

def test_abreuver_adultes_deja_abreuves_seau(headers, adultes_abreuves, remise_pleine, clapier_plein):
    # Give bunnies water
    remise_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
    abreuver_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/abreuverEau", headers=headers)
    assert abreuver_response.status_code == 200, f"Failed: {abreuver_response.text}"

    # Verify the bunnies drank
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["remise"].get("eau") == remise_response.get("eau")

def test_abreuver_adultes_seau_pauvre(headers, adultes_assoiffes, remise_vide, clapier_plein):
    # Give bunnies water
    remise_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
    abreuver_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/abreuverEau", headers=headers)
    assert abreuver_response.status_code == 200, f"Failed: {abreuver_response.text}"

    # Verify the bunnies drank
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("adultesAbreuves") == False
    assert updated_farm_data["remise"].get("eau") == remise_response.get("eau")

def test_soigner_adultes(headers, adultes_malades, fermier_riche, clapier_plein):
    # Heal bunnies
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    soigner_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/soigner", headers=headers)
    assert soigner_response.status_code == 200, f"Failed: {soigner_response.text}"

    # Verify the bunnies are healed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("adultesMalades") == False
    assert updated_farm_data["ecus"] == ecus_response.get("ecus") - 6

def test_soigner_adultes_deja_soignes(headers, adultes_sains, fermier_riche, clapier_plein):
    # Heal bunnies
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    soigner_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/soigner", headers=headers)
    assert soigner_response.status_code == 200, f"Failed: {soigner_response.text}"

    # Verify the bunnies are healed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["ecus"] == ecus_response.get("ecus")

def test_soigner_adultes_pauvre(headers, adultes_malades, fermier_pauvre, clapier_plein):
    # Heal bunnies
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    soigner_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/soigner", headers=headers)
    assert soigner_response.status_code == 200, f"Failed: {soigner_response.text}"

    # Verify the bunnies are healed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("adultesMalades") == True
    assert updated_farm_data["ecus"] == ecus_response.get("ecus")

def test_soigner_seringue_adultes(headers, adultes_malades, remise_pleine, clapier_plein):
    # Heal bunnies
    remise_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
    soigner_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/soignerSeringue", headers=headers)
    assert soigner_response.status_code == 200, f"Failed: {soigner_response.text}"

    # Verify the bunnies are healed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("adultesMalades") == False
    assert updated_farm_data["remise"].get("seringue") == remise_response.get("seringue") - 1

def test_soigner_adultes_deja_soignes_seringue(headers, adultes_sains, remise_pleine, clapier_plein):
    # Heal bunnies
    remise_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
    soigner_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/soignerSeringue", headers=headers)
    assert soigner_response.status_code == 200, f"Failed: {soigner_response.text}"

    # Verify the bunnies are healed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["remise"].get("seringue") == remise_response.get("seringue")

def test_soigner_adultes_seringue_pauvre(headers, adultes_malades, remise_vide, clapier_plein):
    # Heal bunnies
    remise_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
    soigner_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/soignerSeringue", headers=headers)
    assert soigner_response.status_code == 200, f"Failed: {soigner_response.text}"

    # Verify the bunnies are healed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("adultesMalades") == True
    assert updated_farm_data["remise"].get("seringue") == remise_response.get("seringue")

def test_nettoyer_adultes(headers, adultes_sales, fermier_riche, clapier_plein):
    # Clean bunnies
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    nettoyer_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/nettoyer", headers=headers)
    assert nettoyer_response.status_code == 200, f"Failed: {nettoyer_response.text}"

    # Verify the bunnies are clean
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("adultesSales") == False
    assert updated_farm_data["ecus"] == ecus_response.get("ecus") - 3

def test_nettoyer_adultes_deja_nettoyes(headers, adultes_propres, fermier_riche, clapier_plein):
    # Clean bunnies
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    nettoyer_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/nettoyer", headers=headers)
    assert nettoyer_response.status_code == 200, f"Failed: {nettoyer_response.text}"

    # Verify the bunnies are clean
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["ecus"] == ecus_response.get("ecus")

def test_nettoyer_adultes_pauvre(headers, adultes_sales, fermier_pauvre, clapier_plein):
    # Clean bunnies
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    nettoyer_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/nettoyer", headers=headers)
    assert nettoyer_response.status_code == 200, f"Failed: {nettoyer_response.text}"

    # Verify the bunnies are clean
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("adultesSales") == True
    assert updated_farm_data["ecus"] == ecus_response.get("ecus")

def test_nettoyer_savon_adultes(headers, adultes_sales, remise_pleine, clapier_plein):
    # Clean bunnies
    remise_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
    nettoyer_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/nettoyerSavon", headers=headers)
    assert nettoyer_response.status_code == 200, f"Failed: {nettoyer_response.text}"

    # Verify the bunnies are clean
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("adultesSales") == False
    assert updated_farm_data["remise"].get("savon") == remise_response.get("savon") - 1

def test_nettoyer_adultes_deja_nettoyes_savon(headers, adultes_propres, remise_pleine, clapier_plein):
    # Clean bunnies
    remise_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
    nettoyer_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/nettoyerSavon", headers=headers)
    assert nettoyer_response.status_code == 200, f"Failed: {nettoyer_response.text}"

    # Verify the bunnies are clean
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["remise"].get("savon") == remise_response.get("savon")

def test_nettoyer_adultes_savon_pauvre(headers, adultes_sales, remise_vide, clapier_plein):
    # Clean bunnies
    remise_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
    nettoyer_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/nettoyerSavon", headers=headers)
    assert nettoyer_response.status_code == 200, f"Failed: {nettoyer_response.text}"

    # Verify the bunnies are clean
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("adultesMalades") == True
    assert updated_farm_data["remise"].get("savon") == remise_response.get("savon")

def test_nourrir_enfants(headers, enfants_affames, fermier_riche, clapier_plein):
    # Feed bunnies
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    nourrir_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/nourrir", headers=headers)
    assert nourrir_response.status_code == 200, f"Failed to feed: {nourrir_response.text}"

    # Verify the bunnies are fed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("enfantsNourris") == True
    assert updated_farm_data["ecus"] == ecus_response.get("ecus") - 5

def test_nourrir_enfants_deja_nourris(headers, enfants_nourris, fermier_riche, clapier_plein):
    # Feed bunnies
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    nourrir_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/nourrir", headers=headers)
    assert nourrir_response.status_code == 200, f"Failed to starve: {nourrir_response.text}"

    # Verify the bunnies are fed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["ecus"] == ecus_response.get("ecus")

def test_nourrir_enfants_pauvre(headers, enfants_affames, fermier_pauvre, clapier_plein):
    # Feed bunnies
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    nourrir_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/nourrir", headers=headers)
    assert nourrir_response.status_code == 200, f"Failed to starve: {nourrir_response.text}"

    # Verify the bunnies are fed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("enfantsNourris") == False
    assert updated_farm_data["ecus"] == ecus_response.get("ecus")

def test_nourrir_sac_enfants(headers, enfants_affames, remise_pleine, clapier_plein):
    # Feed bunnies
    remise_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
    nourrir_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/nourrirSac", headers=headers)
    assert nourrir_response.status_code == 200, f"Failed to feed: {nourrir_response.text}"

    # Verify the bunnies are fed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("enfantsNourris") == True
    assert updated_farm_data["remise"].get("sac_nourriture") == remise_response.get("sac_nourriture") - 1

def test_nourrir_enfants_deja_nourris_sac(headers, enfants_nourris, remise_pleine, clapier_plein):
    # Feed bunnies
    remise_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
    nourrir_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/nourrirSac", headers=headers)
    assert nourrir_response.status_code == 200, f"Failed to starve: {nourrir_response.text}"

    # Verify the bunnies are fed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["remise"].get("sac_nourriture") == remise_response.get("sac_nourriture")

def test_nourrir_enfants_sac_pauvre(headers, enfants_affames, remise_vide, clapier_plein):
    # Feed bunnies
    remise_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
    nourrir_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/nourrirSac", headers=headers)
    assert nourrir_response.status_code == 200, f"Failed to starve: {nourrir_response.text}"

    # Verify the bunnies are fed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("enfantsNourris") == False
    assert updated_farm_data["remise"].get("sac_nourriture") == remise_response.get("sac_nourriture")

def test_abreuver_enfants(headers, enfants_assoiffes, fermier_riche, clapier_plein):
    # Give bunnies water
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    abreuver_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/abreuver", headers=headers)
    assert abreuver_response.status_code == 200, f"Failed: {abreuver_response.text}"

    # Verify the bunnies drank
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("enfantsAbreuves") == True
    assert updated_farm_data["ecus"] == ecus_response.get("ecus") - 2

def test_abreuver_enfants_deja_abreuves(headers, enfants_abreuves, fermier_riche, clapier_plein):
    # Give bunnies water
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    abreuver_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/abreuver", headers=headers)
    assert abreuver_response.status_code == 200, f"Failed: {abreuver_response.text}"

    # Verify the bunnies drank
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["ecus"] == ecus_response.get("ecus")

def test_abreuver_enfants_pauvre(headers, enfants_assoiffes, fermier_pauvre, clapier_plein):
    # Give bunnies water
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    abreuver_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/abreuver", headers=headers)
    assert abreuver_response.status_code == 200, f"Failed: {abreuver_response.text}"

    # Verify the bunnies drank
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("enfantsAbreuves") == False
    assert updated_farm_data["ecus"] == ecus_response.get("ecus")

def test_abreuver_seau_enfants(headers, enfants_assoiffes, remise_pleine, clapier_plein):
    # Give bunnies water
    remise_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
    abreuver_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/abreuverEau", headers=headers)
    assert abreuver_response.status_code == 200, f"Failed: {abreuver_response.text}"

    # Verify the bunnies drank
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("enfantsAbreuves") == True
    assert updated_farm_data["remise"].get("eau") == remise_response.get("eau") - 1

def test_abreuver_enfants_deja_abreuves_seau(headers, enfants_abreuves, remise_pleine, clapier_plein):
    # Give bunnies water
    remise_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
    abreuver_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/abreuverEau", headers=headers)
    assert abreuver_response.status_code == 200, f"Failed: {abreuver_response.text}"

    # Verify the bunnies drank
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["remise"].get("eau") == remise_response.get("eau")

def test_abreuver_enfants_seau_pauvre(headers, enfants_assoiffes, remise_vide, clapier_plein):
    # Give bunnies water
    remise_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
    abreuver_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/abreuverEau", headers=headers)
    assert abreuver_response.status_code == 200, f"Failed: {abreuver_response.text}"

    # Verify the bunnies drank
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("enfantsAbreuves") == False
    assert updated_farm_data["remise"].get("eau") == remise_response.get("eau")

def test_soigner_enfants(headers, enfants_malades, fermier_riche, clapier_plein):
    # Heal bunnies
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    soigner_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/soigner", headers=headers)
    assert soigner_response.status_code == 200, f"Failed: {soigner_response.text}"

    # Verify the bunnies are healed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("enfantsMalades") == False
    assert updated_farm_data["ecus"] == ecus_response.get("ecus") - 6

def test_soigner_enfants_deja_soignes(headers, enfants_sains, fermier_riche, clapier_plein):
    # Heal bunnies
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    soigner_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/soigner", headers=headers)
    assert soigner_response.status_code == 200, f"Failed: {soigner_response.text}"

    # Verify the bunnies are healed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["ecus"] == ecus_response.get("ecus")

def test_soigner_enfants_pauvre(headers, enfants_malades, fermier_pauvre, clapier_plein):
    # Heal bunnies
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    soigner_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/soigner", headers=headers)
    assert soigner_response.status_code == 200, f"Failed: {soigner_response.text}"

    # Verify the bunnies are healed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("enfantsMalades") == True
    assert updated_farm_data["ecus"] == ecus_response.get("ecus")

def test_soigner_seringue_enfants(headers, enfants_malades, remise_pleine, clapier_plein):
    # Heal bunnies
    remise_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
    soigner_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/soignerSeringue", headers=headers)
    assert soigner_response.status_code == 200, f"Failed: {soigner_response.text}"

    # Verify the bunnies are healed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("enfantsMalades") == False
    assert updated_farm_data["remise"].get("seringue") == remise_response.get("seringue") - 1

def test_soigner_enfants_deja_soignes_seringue(headers, enfants_sains, remise_pleine, clapier_plein):
    # Heal bunnies
    remise_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
    soigner_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/soignerSeringue", headers=headers)
    assert soigner_response.status_code == 200, f"Failed: {soigner_response.text}"

    # Verify the bunnies are healed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["remise"].get("seringue") == remise_response.get("seringue")

def test_soigner_enfants_seringue_pauvre(headers, enfants_malades, remise_vide, clapier_plein):
    # Heal bunnies
    remise_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
    soigner_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/soignerSeringue", headers=headers)
    assert soigner_response.status_code == 200, f"Failed: {soigner_response.text}"

    # Verify the bunnies are healed
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("enfantsMalades") == True
    assert updated_farm_data["remise"].get("seringue") == remise_response.get("seringue")

def test_nettoyer_enfants(headers, enfants_sales, fermier_riche, clapier_plein):
    # Clean bunnies
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    nettoyer_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/nettoyer", headers=headers)
    assert nettoyer_response.status_code == 200, f"Failed: {nettoyer_response.text}"

    # Verify the bunnies are clean
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("enfantsSales") == False
    assert updated_farm_data["ecus"] == ecus_response.get("ecus") - 3

def test_nettoyer_enfants_deja_nettoyes(headers, enfants_propres, fermier_riche, clapier_plein):
    # Clean bunnies
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    nettoyer_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/nettoyer", headers=headers)
    assert nettoyer_response.status_code == 200, f"Failed: {nettoyer_response.text}"

    # Verify the bunnies are clean
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["ecus"] == ecus_response.get("ecus")

def test_nettoyer_enfants_pauvre(headers, enfants_sales, fermier_pauvre, clapier_plein):
    # Clean bunnies
    ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    nettoyer_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/nettoyer", headers=headers)
    assert nettoyer_response.status_code == 200, f"Failed: {nettoyer_response.text}"

    # Verify the bunnies are clean
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("enfantsSales") == True
    assert updated_farm_data["ecus"] == ecus_response.get("ecus")

def test_nettoyer_savon_enfants(headers, enfants_sales, remise_pleine, clapier_plein):
    # Clean bunnies
    remise_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
    nettoyer_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/nettoyerSavon", headers=headers)
    assert nettoyer_response.status_code == 200, f"Failed: {nettoyer_response.text}"

    # Verify the bunnies are clean
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("enfantsSales") == False
    assert updated_farm_data["remise"].get("savon") == remise_response.get("savon") - 1

def test_nettoyer_enfants_deja_nettoyes_savon(headers, enfants_propres, remise_pleine, clapier_plein):
    # Clean bunnies
    remise_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
    nettoyer_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/nettoyerSavon", headers=headers)
    assert nettoyer_response.status_code == 200, f"Failed: {nettoyer_response.text}"

    # Verify the bunnies are clean
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["remise"].get("savon") == remise_response.get("savon")

def test_nettoyer_enfants_savon_pauvre(headers, enfants_sales, remise_vide, clapier_plein):
    # Clean bunnies
    remise_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
    nettoyer_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/nettoyerSavon", headers=headers)
    assert nettoyer_response.status_code == 200, f"Failed: {nettoyer_response.text}"

    # Verify the bunnies are clean
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("enfantsMalades") == True
    assert updated_farm_data["remise"].get("savon") == remise_response.get("savon")

def test_reproduction_nourris_abreuves(headers, clapier_plein, adultes_nourris, adultes_abreuves):
    # Breed bunnies
    babies_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"].get("nbLapereauxBebes")
    reproduction_response = requests.post(f"{APP_URL}/fermiers/clapier/reproduction", headers=headers)
    assert reproduction_response.status_code == 200, f"Failed: {reproduction_response.text}"

    # Verify the bunnies bred
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("nbLapereauxBebes") >= babies_response

def test_reproduction_nourris_assoiffes(headers, clapier_plein, adultes_nourris, adultes_assoiffes):
    # Breed bunnies
    babies_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"].get("nbLapereauxBebes")
    reproduction_response = requests.post(f"{APP_URL}/fermiers/clapier/reproduction", headers=headers)
    assert reproduction_response.status_code == 200, f"Failed: {reproduction_response.text}"

    # Verify the bunnies bred
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("nbLapereauxBebes") >= babies_response

def test_reproduction_affames_abreuves(headers, clapier_plein, adultes_affames, adultes_abreuves):
    # Breed bunnies
    babies_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"].get("nbLapereauxBebes")
    reproduction_response = requests.post(f"{APP_URL}/fermiers/clapier/reproduction", headers=headers)
    assert reproduction_response.status_code == 200, f"Failed: {reproduction_response.text}"

    # Verify the bunnies bred
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("nbLapereauxBebes") >= babies_response

def test_reproduction_affames_assoiffes(headers, clapier_plein, adultes_affames, adultes_assoiffes):
    # Breed bunnies
    babies_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"].get("nbLapereauxBebes")
    reproduction_response = requests.post(f"{APP_URL}/fermiers/clapier/reproduction", headers=headers)
    assert reproduction_response.status_code == 200, f"Failed: {reproduction_response.text}"

    # Verify the bunnies bred
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("nbLapereauxBebes") >= babies_response

def test_reproduction_zero_adultes(headers, clapier_vide, adultes_nourris, adultes_abreuves):
    # Breed bunnies
    babies_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"].get("nbLapereauxBebes")
    reproduction_response = requests.post(f"{APP_URL}/fermiers/clapier/reproduction", headers=headers)
    assert reproduction_response.status_code == 200, f"Failed: {reproduction_response.text}"

    # Verify the bunnies bred
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("nbLapereauxBebes") == babies_response

def test_reproduction_zero_males(headers, clapier_plein, adultes_nourris, adultes_abreuves):
    # Breed bunnies
    babies_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"].get("nbLapereauxBebes")
    nbLapinsSupp = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"].get("nbLapinsMales")
    suppMales_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/males/supp/{nbLapinsSupp}", headers=headers)
    assert suppMales_response.status_code == 200, f"Failed: {suppMales_response.text}"
    reproduction_response = requests.post(f"{APP_URL}/fermiers/clapier/reproduction", headers=headers)
    assert reproduction_response.status_code == 200, f"Failed: {reproduction_response.text}"

    # Verify the bunnies bred
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("nbLapinsMales") == 0
    assert updated_farm_data["clapier"].get("nbLapereauxBebes") == babies_response

def test_reproduction_zero_femelles(headers, clapier_plein, adultes_nourris, adultes_abreuves):
    # Breed bunnies
    babies_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"].get("nbLapereauxBebes")
    nbLapinsSupp = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"].get("nbLapinsFemelles")
    suppFemelles_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/femelles/supp/{nbLapinsSupp}", headers=headers)
    assert suppFemelles_response.status_code == 200, f"Failed: {suppFemelles_response.text}"
    reproduction_response = requests.post(f"{APP_URL}/fermiers/clapier/reproduction", headers=headers)
    assert reproduction_response.status_code == 200, f"Failed: {reproduction_response.text}"

    # Verify the bunnies bred
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("nbLapinsFemelles") == 0
    assert updated_farm_data["clapier"].get("nbLapereauxBebes") == babies_response

def test_reproduction_pas_de_place(headers, clapier_max, adultes_nourris, adultes_abreuves):
    # Breed bunnies
    remise_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
    babies_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"].get("nbLapereauxBebes")
    reproduction_response = requests.post(f"{APP_URL}/fermiers/clapier/reproduction", headers=headers)
    assert reproduction_response.status_code == 200, f"Failed: {reproduction_response.text}"

    # Verify the bunnies bred
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    babies_response == 50
    assert updated_farm_data["clapier"].get("nbLapereauxBebes") == babies_response

def test_grandir(headers, clapier_plein, enfants_nourris, enfants_abreuves):
    # Grow bunnies
    req = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"]
    nb_bebes = req.get("nbLapereauxBebes")
    nb_petits = req.get("nbLapereauxPetits")
    nb_gros = req.get("nbLapereauxGros")
    nb_adultes = req.get("nbLapinsMales") + req.get("nbLapinsFemelles")
    grow_response = requests.post(f"{APP_URL}/fermiers/clapier/grandir", headers=headers)
    assert grow_response.status_code == 200, f"Failed: {grow_response.text}"

    # Verify the babies grew
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("nbLapereauxBebes") == 0
    assert updated_farm_data["clapier"].get("nbLapereauxPetits") == nb_bebes
    assert updated_farm_data["clapier"].get("nbLapereauxGros") == nb_petits
    assert (updated_farm_data["clapier"].get("nbLapinsMales") + updated_farm_data["clapier"].get("nbLapinsFemelles")) == nb_adultes + nb_gros


def test_grandir_affames(headers, clapier_plein, enfants_affames, enfants_abreuves):
    # Grow bunnies
    req = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"]
    nb_bebes = req.get("nbLapereauxBebes")
    nb_petits = req.get("nbLapereauxPetits")
    nb_gros = req.get("nbLapereauxGros")
    nb_adultes = req.get("nbLapinsMales") + req.get("nbLapinsFemelles")
    grow_response = requests.post(f"{APP_URL}/fermiers/clapier/grandir", headers=headers)
    assert grow_response.status_code == 200, f"Failed: {grow_response.text}"

    # Verify the babies grew
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("nbLapereauxBebes") == nb_bebes
    assert updated_farm_data["clapier"].get("nbLapereauxPetits") == nb_petits
    assert updated_farm_data["clapier"].get("nbLapereauxGros") == nb_gros
    assert (updated_farm_data["clapier"].get("nbLapinsMales") + updated_farm_data["clapier"].get("nbLapinsFemelles")) == nb_adultes

def test_grandir_assoiffes(headers, clapier_plein, enfants_nourris, enfants_assoiffes):
    # Grow bunnies
    req = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"]
    nb_bebes = req.get("nbLapereauxBebes")
    nb_petits = req.get("nbLapereauxPetits")
    nb_gros = req.get("nbLapereauxGros")
    nb_adultes = req.get("nbLapinsMales") + req.get("nbLapinsFemelles")
    grow_response = requests.post(f"{APP_URL}/fermiers/clapier/grandir", headers=headers)
    assert grow_response.status_code == 200, f"Failed: {grow_response.text}"

    # Verify the babies grew
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("nbLapereauxBebes") == nb_bebes
    assert updated_farm_data["clapier"].get("nbLapereauxPetits") == nb_petits
    assert updated_farm_data["clapier"].get("nbLapereauxGros") == nb_gros
    assert (updated_farm_data["clapier"].get("nbLapinsMales") + updated_farm_data["clapier"].get("nbLapinsFemelles")) == nb_adultes

def test_grandir_affames_assoiffes(headers, clapier_plein, enfants_affames, enfants_assoiffes):
    # Grow bunnies
    req = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"]
    nb_bebes = req.get("nbLapereauxBebes")
    nb_petits = req.get("nbLapereauxPetits")
    nb_gros = req.get("nbLapereauxGros")
    nb_adultes = req.get("nbLapinsMales") + req.get("nbLapinsFemelles")
    grow_response = requests.post(f"{APP_URL}/fermiers/clapier/grandir", headers=headers)
    assert grow_response.status_code == 200, f"Failed: {grow_response.text}"

    # Verify the babies grew
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("nbLapereauxBebes") == nb_bebes
    assert updated_farm_data["clapier"].get("nbLapereauxPetits") == nb_petits
    assert updated_farm_data["clapier"].get("nbLapereauxGros") == nb_gros
    assert (updated_farm_data["clapier"].get("nbLapinsMales") + updated_farm_data["clapier"].get("nbLapinsFemelles")) == nb_adultes


def test_grandir_clapier_plein(headers, clapier_max, enfants_nourris, enfants_abreuves):
    # Grow bunnies
    req = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"]
    nb_bebes = req.get("nbLapereauxBebes")
    nb_petits = req.get("nbLapereauxPetits")
    nb_gros = req.get("nbLapereauxGros")
    nb_adultes = req.get("nbLapinsMales") + req.get("nbLapinsFemelles")
    grow_response = requests.post(f"{APP_URL}/fermiers/clapier/grandir", headers=headers)
    assert grow_response.status_code == 200, f"Failed: {grow_response.text}"

    # Verify the babies grew
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("nbLapereauxBebes") == 0
    assert updated_farm_data["clapier"].get("nbLapereauxPetits") == nb_bebes
    assert updated_farm_data["clapier"].get("nbLapereauxGros") == nb_gros + nb_petits
    assert (updated_farm_data["clapier"].get("nbLapinsMales") + updated_farm_data["clapier"].get("nbLapinsFemelles")) == nb_adultes

def test_grandir_clapier_partiellement_plein(headers, clapier_max, enfants_nourris, enfants_abreuves):
    # Grow bunnies
    req = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"]
    nb_bebes = req.get("nbLapereauxBebes")
    nb_petits = req.get("nbLapereauxPetits")
    nb_gros = req.get("nbLapereauxGros")
    nb_adultes = req.get("nbLapinsMales") + req.get("nbLapinsFemelles")
    suppFemelles_response = requests.post(f"{APP_URL}/fermiers/clapier/adultes/femelles/supp/{5}", headers=headers)
    assert suppFemelles_response.status_code == 200, f"Failed: {suppFemelles_response.text}"
    req2 = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"]
    nb_adultes_supp = req2.get("nbLapinsMales") + req2.get("nbLapinsFemelles")
    nb_places = nb_adultes - nb_adultes_supp
    grow_response = requests.post(f"{APP_URL}/fermiers/clapier/grandir", headers=headers)
    assert grow_response.status_code == 200, f"Failed: {grow_response.text}"

    # Verify the babies grew
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("nbLapereauxBebes") == 0
    assert updated_farm_data["clapier"].get("nbLapereauxPetits") == nb_bebes
    assert updated_farm_data["clapier"].get("nbLapereauxGros") == nb_gros + nb_petits - nb_places
    assert (updated_farm_data["clapier"].get("nbLapinsMales") + updated_farm_data["clapier"].get("nbLapinsFemelles")) == nb_adultes_supp + nb_places

def test_mort_sales(headers, clapier_plein, adultes_nourris, adultes_sains, adultes_sales, enfants_nourris, enfants_sains, enfants_sales):
    # Kill the bunnies
    req = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"]
    nb_enfants = req.get("nbLapereauxBebes") + req.get("nbLapereauxPetits") + req.get("nbLapereauxGros")
    nb_adultes = req.get("nbLapinsMales") + req.get("nbLapinsFemelles")
    mort_response = requests.post(f"{APP_URL}/fermiers/clapier/mort", headers=headers)
    assert mort_response.status_code == 200, f"Failed: {mort_response.text}"

    # Verify the bunnies are dead
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("nbLapereauxBebes") + updated_farm_data["clapier"].get("nbLapereauxPetits") + updated_farm_data["clapier"].get("nbLapereauxGros") < nb_enfants
    assert updated_farm_data["clapier"].get("nbLapinsMales") + updated_farm_data["clapier"].get("nbLapinsFemelles") < nb_adultes

def test_mort_malades(headers, clapier_plein, adultes_nourris, adultes_malades, adultes_propres, enfants_nourris, enfants_malades, enfants_propres):
    # Kill the bunnies
    req = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"]
    nb_enfants = req.get("nbLapereauxBebes") + req.get("nbLapereauxPetits") + req.get("nbLapereauxGros")
    nb_adultes = req.get("nbLapinsMales") + req.get("nbLapinsFemelles")
    mort_response = requests.post(f"{APP_URL}/fermiers/clapier/mort", headers=headers)
    assert mort_response.status_code == 200, f"Failed: {mort_response.text}"

    # Verify the bunnies are dead
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("nbLapereauxBebes") + updated_farm_data["clapier"].get("nbLapereauxPetits") + updated_farm_data["clapier"].get("nbLapereauxGros") < nb_enfants
    assert updated_farm_data["clapier"].get("nbLapinsMales") + updated_farm_data["clapier"].get("nbLapinsFemelles") < nb_adultes

def test_mort_affames(headers, clapier_plein, adultes_affames, adultes_sains, adultes_propres, enfants_affames, enfants_sains, enfants_propres):
    # Kill the bunnies
    req = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"]
    nb_enfants = req.get("nbLapereauxBebes") + req.get("nbLapereauxPetits") + req.get("nbLapereauxGros")
    nb_adultes = req.get("nbLapinsMales") + req.get("nbLapinsFemelles")
    mort_response = requests.post(f"{APP_URL}/fermiers/clapier/mort", headers=headers)
    assert mort_response.status_code == 200, f"Failed: {mort_response.text}"

    # Verify the bunnies are dead
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("nbLapereauxBebes") + updated_farm_data["clapier"].get("nbLapereauxPetits") + updated_farm_data["clapier"].get("nbLapereauxGros") < nb_enfants
    assert updated_farm_data["clapier"].get("nbLapinsMales") + updated_farm_data["clapier"].get("nbLapinsFemelles") < nb_adultes

def test_survie(headers, clapier_plein, adultes_nourris, adultes_sains, adultes_propres, enfants_nourris, enfants_sains, enfants_propres):
    # Kill the bunnies
    req = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"]
    nb_enfants = req.get("nbLapereauxBebes") + req.get("nbLapereauxPetits") + req.get("nbLapereauxGros")
    nb_adultes = req.get("nbLapinsMales") + req.get("nbLapinsFemelles")
    mort_response = requests.post(f"{APP_URL}/fermiers/clapier/mort", headers=headers)
    assert mort_response.status_code == 200, f"Failed: {mort_response.text}"

    # Verify the bunnies are dead
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("nbLapereauxBebes") + updated_farm_data["clapier"].get("nbLapereauxPetits") + updated_farm_data["clapier"].get("nbLapereauxGros") == nb_enfants
    assert updated_farm_data["clapier"].get("nbLapinsMales") + updated_farm_data["clapier"].get("nbLapinsFemelles") == nb_adultes

def test_mort_petits(headers, clapier_plein, enfants_affames, enfants_sains, enfants_propres):
    # Kill the bunnies
    suppBebes_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/bebes/supp/{50}", headers=headers)
    assert suppBebes_response.status_code == 200, f"Failed: {suppBebes_response.text}"
    req = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"]
    nb_petits = req.get("nbLapereauxPetits")
    mort_response = requests.post(f"{APP_URL}/fermiers/clapier/mort", headers=headers)
    assert mort_response.status_code == 200, f"Failed: {mort_response.text}"

    # Verify the bunnies are dead
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("nbLapereauxPetits") < nb_petits

def test_mort_gros(headers, clapier_plein, enfants_affames, enfants_sains, enfants_propres):
    # Kill the bunnies
    suppBebes_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/bebes/supp/{50}", headers=headers)
    assert suppBebes_response.status_code == 200, f"Failed: {suppBebes_response.text}"
    suppPetits_response = requests.post(f"{APP_URL}/fermiers/clapier/enfants/petits/supp/{50}", headers=headers)
    assert suppPetits_response.status_code == 200, f"Failed: {suppPetits_response.text}"
    req = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["clapier"]
    nb_gros = req.get("nbLapereauxGros")
    mort_response = requests.post(f"{APP_URL}/fermiers/clapier/mort", headers=headers)
    assert mort_response.status_code == 200, f"Failed: {mort_response.text}"

    # Verify the bunnies are dead
    updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    assert updated_farm_data["clapier"].get("nbLapereauxGros") < nb_gros