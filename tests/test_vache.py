import requests
import pytest
import datetime

# Base URL for the Spring Boot application
APP_URL = "http://localhost:8080"

from test_secu import auth_token, headers, fermier_pauvre, fermier_riche, remise_pleine, remise_vide

@pytest.fixture
def vache_assoiffee(headers):
    assoiffer_vache_response = requests.post(f"{APP_URL}/fermiers/vache/assoiffer", headers=headers)
    assert assoiffer_vache_response.status_code == 200, f"Failed to make thirsty: {assoiffer_vache_response.text}"

@pytest.fixture
def vache_abreuvee(headers, fermier_riche):
    abreuver_vache_response = requests.post(f"{APP_URL}/fermiers/vache/abreuver", headers=headers)
    assert abreuver_vache_response.status_code == 200, f"Failed to give water: {abreuver_vache_response.text}"

@pytest.fixture
def vache_affamee(headers):
    affamer_vache_response = requests.post(f"{APP_URL}/fermiers/vache/affamer", headers=headers)
    assert affamer_vache_response.status_code == 200, f"Failed to starve: {affamer_vache_response.text}"

@pytest.fixture
def vache_nourrie(headers, fermier_riche):
    nourrir_vache_response = requests.post(f"{APP_URL}/fermiers/vache/nourrirPaille", headers=headers)
    assert nourrir_vache_response.status_code == 200, f"Failed to feed with straw: {nourrir_vache_response.text}"

@pytest.fixture
def vache_propre(headers, fermier_riche):
    nettoyer_vache_response = requests.post(f"{APP_URL}/fermiers/vache/nettoyer", headers=headers)
    assert nettoyer_vache_response.status_code == 200, f"Failed to cleans: {nettoyer_vache_response.text}"

@pytest.fixture
def vache_sale(headers):
    salir_vache_response = requests.post(f"{APP_URL}/fermiers/vache/salir", headers=headers)
    assert salir_vache_response.status_code == 200, f"Failed to dirty: {salir_vache_response.text}"

@pytest.fixture
def vache_malade(headers):
    rendre_malade_vache_response = requests.post(f"{APP_URL}/fermiers/vache/rendreMalade5J", headers=headers)
    assert rendre_malade_vache_response.status_code == 200, f"Failed to make sick: {rendre_malade_vache_response.text}"

@pytest.fixture
def vache_saine(headers, fermier_riche):
    soigner_vache_response = requests.post(f"{APP_URL}/fermiers/vache/soigner", headers=headers)
    assert soigner_vache_response.status_code == 200, f"Failed to heal: {soigner_vache_response.text}"

@pytest.fixture
def vache_adulte(headers):
    grandir_vache_response = requests.post(f"{APP_URL}/fermiers/vache/grandir", headers=headers)
    assert grandir_vache_response.status_code == 200, f"Failed to grow: {grandir_vache_response.text}"

@pytest.fixture
def vache_enfant(headers):
    rajeunir_vache_response = requests.post(f"{APP_URL}/fermiers/vache/rajeunir", headers=headers)
    assert rajeunir_vache_response.status_code == 200, f"Failed to make young: {rajeunir_vache_response.text}"

@pytest.fixture
def vache_vivante(headers):
    vie_vache_response = requests.post(f"{APP_URL}/fermiers/vache/ressuciter", headers=headers)
    assert vie_vache_response.status_code == 200, f"Failed to make young: {vie_vache_response.text}"

@pytest.fixture
def vache_morte(headers):
    vie_vache_response = requests.post(f"{APP_URL}/fermiers/vache/tuer", headers=headers)
    assert vie_vache_response.status_code == 200, f"Failed to make young: {vie_vache_response.text}"

@pytest.fixture
def vache_maigre(headers):
    maigrir_vache_response = requests.post(f"{APP_URL}/fermiers/vache/maigrir", headers=headers)
    assert maigrir_vache_response.status_code == 200, f"Failed to lose weight: {rajeunir_vache_response.text}"

@pytest.fixture
def vache_pleine(headers):
    pleine_vache_response = requests.post(f"{APP_URL}/fermiers/vache/remplir", headers=headers)
    assert pleine_vache_response.status_code == 200, f"Failed to fill: {pleine_vache_response.text}"

@pytest.fixture
def vache_vide(headers):
    vide_vache_response = requests.post(f"{APP_URL}/fermiers/vache/vider", headers=headers)
    assert vide_vache_response.status_code == 200, f"Failed to empty: {vide_vache_response.text}"

@pytest.fixture
def vache_traite(headers):
    traite_vache_response = requests.post(f"{APP_URL}/fermiers/vache/traire", headers=headers)
    assert traite_vache_response.status_code == 200, f"Failed to milk: {traite_vache_response.text}"

@pytest.fixture
def vache_non_traite(headers):
    non_traite_vache_response = requests.post(f"{APP_URL}/fermiers/vache/resetTraire", headers=headers)
    assert non_traite_vache_response.status_code == 200, f"Failed to reset milking: {non_traite_vache_response.text}"

def test_cow(headers):
    response = requests.get(f"{APP_URL}/fermiers", headers=headers)
    assert response.status_code == 200, f"Failed to fetch/create farm: {response.text}"

    farm_data = response.json()
    assert "vache" in farm_data
    print(farm_data["vache"])
    assert farm_data["vache"].get("litresLait") == 0

def test_prod_lait_non_traite_vide_cow(headers, vache_adulte, vache_propre, vache_saine, vache_nourrie, vache_vide, vache_non_traite):
        # cow makes milk
        milk_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["vache"].get("litresLait")
        prod_lait_response = requests.post(f"{APP_URL}/fermiers/vache/prodLait", headers=headers)
        assert prod_lait_response.status_code == 200, f"Cow failed to produce milk: {prod_lait_response.text}"

        # Verify the cow made milk
        updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        assert updated_farm_data["vache"].get("litresLait") > milk_response, "Cow didn't make milk"
        assert updated_farm_data["vache"].get("litresLait") == 4, "Cow made too much milk"

def test_prod_lait_traite_vide_cow(headers, vache_adulte, vache_propre, vache_saine, vache_nourrie, vache_vide, vache_traite):
        # cow makes milk
        milk_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["vache"].get("litresLait")
        prod_lait_response = requests.post(f"{APP_URL}/fermiers/vache/prodLait", headers=headers)
        assert prod_lait_response.status_code == 200, f"Cow failed to produce milk: {prod_lait_response.text}"

        # Verify the cow made milk
        updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        assert updated_farm_data["vache"].get("litresLait") > milk_response, "Cow didn't make milk"
        assert updated_farm_data["vache"].get("litresLait") == 8, "Cow made too much milk"

def test_prod_lait_pleine_cow(headers, vache_adulte, vache_propre, vache_saine, vache_nourrie, vache_pleine):
        # cow makes milk
        milk_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["vache"].get("litresLait")
        prod_lait_response = requests.post(f"{APP_URL}/fermiers/vache/prodLait", headers=headers)
        assert prod_lait_response.status_code == 200, f"Cow failed to produce milk: {prod_lait_response.text}"

        # Verify the cow made milk
        updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        assert updated_farm_data["vache"].get("litresLait") == 16, "Cow made too much milk"

def test_prod_lait_enfant_cow(headers, vache_enfant, vache_propre, vache_saine, vache_nourrie, vache_vide):
        # cow makes milk
        milk_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["vache"].get("litresLait")
        prod_lait_response = requests.post(f"{APP_URL}/fermiers/vache/prodLait", headers=headers)
        assert prod_lait_response.status_code == 200, f"Cow failed to produce milk: {prod_lait_response.text}"

        # Verify the cow made milk
        updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        assert updated_farm_data["vache"].get("litresLait") == milk_response, "Cow made milk"

def test_prod_lait_affamee_cow(headers, vache_adulte, vache_propre, vache_saine, vache_affamee, vache_vide):
        # cow makes milk
        milk_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["vache"].get("litresLait")
        prod_lait_response = requests.post(f"{APP_URL}/fermiers/vache/prodLait", headers=headers)
        assert prod_lait_response.status_code == 200, f"Cow failed to produce milk: {prod_lait_response.text}"

        # Verify the cow made milk
        updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        assert updated_farm_data["vache"].get("litresLait") == milk_response, "Cow made milk"

def test_prod_lait_sale_cow(headers, vache_adulte, vache_sale, vache_saine, vache_nourrie, vache_vide):
        # cow makes milk
        milk_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["vache"].get("litresLait")
        prod_lait_response = requests.post(f"{APP_URL}/fermiers/vache/prodLait", headers=headers)
        assert prod_lait_response.status_code == 200, f"Cow failed to produce milk: {prod_lait_response.text}"

        # Verify the cow made milk
        updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        assert updated_farm_data["vache"].get("litresLait") == milk_response, "Cow made milk"

def test_prod_lait_malade_cow(headers, vache_adulte, vache_propre, vache_malade, vache_nourrie, vache_vide):
        # cow makes milk
        milk_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["vache"].get("litresLait")
        prod_lait_response = requests.post(f"{APP_URL}/fermiers/vache/prodLait", headers=headers)
        assert prod_lait_response.status_code == 200, f"Cow failed to produce milk: {prod_lait_response.text}"

        # Verify the cow made milk
        updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        assert updated_farm_data["vache"].get("litresLait") == milk_response, "Cow made milk"

def test_traite_reussie_cow(headers, vache_pleine):
        # Milks the cow
        lait_remise_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("litresLait")
        traire_response = requests.post(f"{APP_URL}/fermiers/vache/traire", headers=headers)
        assert traire_response.status_code == 200, f"Failed to milk: {traire_response.text}"

        # Verify the cow is milked
        updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        assert updated_farm_data["vache"].get("litresLait") == 0, "Cow made milk"
        assert updated_farm_data["remise"].get("litresLait") > lait_remise_response, "Milk didn't augment"

def test_traite_ratee_cow(headers, vache_vide):
        # Milks the cow
        lait_remise_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["remise"].get("litresLait")
        traire_response = requests.post(f"{APP_URL}/fermiers/vache/traire", headers=headers)
        assert traire_response.status_code == 200, f"Failed to milk: {traire_response.text}"

        # Verify the cow is milked
        updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        assert updated_farm_data["vache"].get("litresLait") == 0, "Cow made milk"
        assert updated_farm_data["remise"].get("litresLait") == lait_remise_response, "Milk augmented"

def test_nourrir_herbe_assoiffee_cow(headers, vache_affamee, vache_assoiffee):
        # Feed the cow
        poids_vache_response = requests.get(f"{APP_URL}/fermiers/vache", headers=headers).json()
        nourrir_paille_response = requests.post(f"{APP_URL}/fermiers/vache/nourrirHerbe", headers=headers)
        assert nourrir_paille_response.status_code == 200, f"Failed to feed with grass: {nourrir_paille_response.text}"

        # Verify the cow is fed
        updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        now = datetime.datetime.now().date()
        assert updated_farm_data["vache"].get("nourris")[0:10] == now.strftime('%Y-%m-%d'), "Cow is fed today"
        assert updated_farm_data["vache"].get("poids") == poids_vache_response.get("poids") + 5

def test_nourrir_herbe_abreuvee_cow(headers, vache_affamee, vache_abreuvee):
        # Feed the cow
        poids_vache_response = requests.get(f"{APP_URL}/fermiers/vache", headers=headers).json()
        nourrir_paille_response = requests.post(f"{APP_URL}/fermiers/vache/nourrirHerbe", headers=headers)
        assert nourrir_paille_response.status_code == 200, f"Failed to feed with grass: {nourrir_paille_response.text}"

        # Verify the cow is fed
        updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        now = datetime.datetime.now().date()
        assert updated_farm_data["vache"].get("nourris")[0:10] == now.strftime('%Y-%m-%d'), "Cow is fed today"
        assert updated_farm_data["vache"].get("poids") == poids_vache_response.get("poids") + 6

def test_abreuver_affamee_cow(headers, vache_affamee, vache_assoiffee, fermier_riche):
        # Give the cow water
        poids_vache_response = requests.get(f"{APP_URL}/fermiers/vache", headers=headers).json()
        abreuver_response = requests.post(f"{APP_URL}/fermiers/vache/abreuver", headers=headers)
        assert abreuver_response.status_code == 200, f"Failed to give water: {abreuver_response.text}"

        # Verify the cow isn't thirsty anymore
        updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        now = datetime.datetime.now().date()
        assert updated_farm_data["vache"].get("abreuve")[0:10] == now.strftime('%Y-%m-%d'), "Cow already drank today"
        assert updated_farm_data["vache"].get("poids") == poids_vache_response.get("poids")

def test_abreuver_nourrie_cow(headers, vache_nourrie, vache_assoiffee, fermier_riche):
        # Give the cow water
        poids_vache_response = requests.get(f"{APP_URL}/fermiers/vache", headers=headers).json()
        abreuver_response = requests.post(f"{APP_URL}/fermiers/vache/abreuver", headers=headers)
        assert abreuver_response.status_code == 200, f"Failed to give water: {abreuver_response.text}"

        # Verify the cow isn't thirsty anymore
        updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        now = datetime.datetime.now().date()
        assert updated_farm_data["vache"].get("abreuve")[0:10] == now.strftime('%Y-%m-%d'), "Cow already drank today"
        assert updated_farm_data["vache"].get("poids") == poids_vache_response.get("poids") + 1

def test_abreuver_cow_pauvre(headers, vache_assoiffee, fermier_pauvre):
        # Give the cow water
        poids_vache_response = requests.get(f"{APP_URL}/fermiers/vache", headers=headers).json()
        abreuver_response = requests.post(f"{APP_URL}/fermiers/vache/abreuver", headers=headers)
        assert abreuver_response.status_code == 200, f"Failed to give water: {abreuver_response.text}"

        # Verify the cow isn't thirsty anymore
        updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        now = datetime.datetime.now().date()
        assert updated_farm_data["vache"].get("abreuve")[0:10] != now.strftime('%Y-%m-%d'), "Cow managed to drink"
        assert updated_farm_data["vache"].get("poids") == poids_vache_response.get("poids")

def test_abreuver_cow_seau_deau(headers, vache_assoiffee, vache_affamee, remise_pleine):
        # Give the cow a bucket of water
        poids_vache_response = requests.get(f"{APP_URL}/fermiers/vache", headers=headers).json()
        eau_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
        abreuver_response = requests.post(f"{APP_URL}/fermiers/vache/abreuverSeauDeau", headers=headers)
        assert abreuver_response.status_code == 200, f"Failed to give water: {abreuver_response.text}"

        # Verify the cow isn't thirsty anymore
        updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        now = datetime.datetime.now().date()
        assert updated_farm_data["vache"].get("abreuve")[0:10] == now.strftime('%Y-%m-%d'), "Cow managed to drink"
        assert updated_farm_data["vache"].get("poids") == poids_vache_response.get("poids")
        assert updated_farm_data["remise"].get("eau") == eau_response.get("eau") - 1

def test_abreuver_cow_seau_deau_no(headers, vache_assoiffee, vache_affamee, remise_vide):
        # Give the cow a bucket of water
        poids_vache_response = requests.get(f"{APP_URL}/fermiers/vache", headers=headers).json()
        eau_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
        abreuver_response = requests.post(f"{APP_URL}/fermiers/vache/abreuverSeauDeau", headers=headers)
        assert abreuver_response.status_code == 200, f"Failed to not give water: {abreuver_response.text}"

        # Verify the cow is thirsty
        updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        now = datetime.datetime.now().date()
        assert updated_farm_data["vache"].get("abreuve")[0:10] != now.strftime('%Y-%m-%d')
        assert updated_farm_data["vache"].get("poids") == poids_vache_response.get("poids")
        assert updated_farm_data["remise"].get("eau") == eau_response.get("eau")

def test_nourrir_paille_cow(headers, fermier_riche):
        # Feed the cow
        poids_vache_response = requests.get(f"{APP_URL}/fermiers/vache", headers=headers).json()
        ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        nourrir_paille_response = requests.post(f"{APP_URL}/fermiers/vache/nourrirPaille", headers=headers)
        assert nourrir_paille_response.status_code == 200, f"Failed to feed with straw: {nourrir_paille_response.text}"

        # Verify the cow is fed
        updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        now = datetime.datetime.now().date()
        assert updated_farm_data["vache"].get("nourris")[0:10] == now.strftime('%Y-%m-%d'), "Cow isn't fed"
        assert updated_farm_data["vache"].get("poids") == poids_vache_response.get("poids") + 3
        assert updated_farm_data["ecus"] == ecus_response.get("ecus") - 5

def test_nourrir_paille_cow_pauvre(headers, fermier_pauvre):
        # Try to feed the cow
        poids_vache_response = requests.get(f"{APP_URL}/fermiers/vache", headers=headers).json()
        ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        nourrir_paille_response = requests.post(f"{APP_URL}/fermiers/vache/nourrirPaille", headers=headers)
        dernier_repas_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["vache"].get("nourris")[0:10]
        assert nourrir_paille_response.status_code == 200, f"Failed to feed with straw: {nourrir_paille_response.text}"

        # Verify the cow isn't fed as the player is short on money
        updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        now = datetime.datetime.now().date()
        assert updated_farm_data["vache"].get("nourris")[0:10] == dernier_repas_response, "Cow is fed"
        assert updated_farm_data["vache"].get("poids") == poids_vache_response.get("poids")
        assert updated_farm_data["ecus"] == ecus_response.get("ecus")

def test_nourrir_botte_paille_cow(headers, remise_pleine):
        # Feed the cow
        poids_vache_response = requests.get(f"{APP_URL}/fermiers/vache", headers=headers).json()
        botte_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
        nourrir_paille_response = requests.post(f"{APP_URL}/fermiers/vache/nourrirBottePaille", headers=headers)
        assert nourrir_paille_response.status_code == 200, f"Failed to feed with straw bale: {nourrir_paille_response.text}"

        # Verify the cow is fed
        updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        now = datetime.datetime.now().date()
        assert updated_farm_data["vache"].get("nourris")[0:10] == now.strftime('%Y-%m-%d'), "Cow isn't fed"
        assert updated_farm_data["vache"].get("poids") == poids_vache_response.get("poids") + 3
        assert updated_farm_data["remise"].get("bottes_de_paille") == botte_response.get("bottes_de_paille") - 1

def test_nourrir_botte_paille_cow_pauvre(headers, remise_vide):
        # Try to feed the cow
        poids_vache_response = requests.get(f"{APP_URL}/fermiers/vache", headers=headers).json()
        botte_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
        nourrir_paille_response = requests.post(f"{APP_URL}/fermiers/vache/nourrirBottePaille", headers=headers)
        dernier_repas_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["vache"].get("nourris")[0:10]
        assert nourrir_paille_response.status_code == 200, f"Failed to feed with straw bale: {nourrir_paille_response.text}"

        # Verify the cow isn't fed as the player is short on money
        updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        now = datetime.datetime.now().date()
        assert updated_farm_data["vache"].get("nourris")[0:10] == dernier_repas_response, "Cow is fed"
        assert updated_farm_data["vache"].get("poids") == poids_vache_response.get("poids")
        assert updated_farm_data["remise"].get("bottes_de_paille") == botte_response.get("bottes_de_paille")

def test_nourrir_herbe_non_cow(headers, vache_nourrie, vache_assoiffee):
        # Feed the cow
        poids_vache_response = requests.get(f"{APP_URL}/fermiers/vache", headers=headers).json()
        nourrir_paille_response = requests.post(f"{APP_URL}/fermiers/vache/nourrirHerbe", headers=headers)
        assert nourrir_paille_response.status_code == 200, f"Failed to feed with grass: {nourrir_paille_response.text}"

        # Verify the cow is fed
        updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        now = datetime.datetime.now().date()
        assert updated_farm_data["vache"].get("nourris")[0:10] == now.strftime('%Y-%m-%d'), "Cow is fed today"
        assert updated_farm_data["vache"].get("poids") == poids_vache_response.get("poids")


def test_soigner_cow(headers, vache_malade, fermier_riche):
        # Heal the cow
        malade_vache_response = requests.get(f"{APP_URL}/fermiers/vache", headers=headers).json()
        ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        soigner_vache_response = requests.post(f"{APP_URL}/fermiers/vache/soigner", headers=headers)
        assert soigner_vache_response.status_code == 200, f"Failed to heal the cow: {soigner_vache_response.text}"

        # Verify the is healed
        updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        assert updated_farm_data["vache"].get("malade") == None
        assert updated_farm_data["ecus"] == ecus_response.get("ecus") - 6

def test_soigner_seringue_cow(headers, vache_malade, remise_pleine):
        # Heal the cow
        malade_vache_response = requests.get(f"{APP_URL}/fermiers/vache", headers=headers).json()
        seringue_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
        soigner_seringue_vache_response = requests.post(f"{APP_URL}/fermiers/vache/soignerSeringue", headers=headers)
        assert soigner_seringue_vache_response.status_code == 200, f"Failed to heal the cow: {soigner_seringue_response.text}"

        # Verify the cow is healed
        updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        assert updated_farm_data["vache"].get("malade") == None
        assert updated_farm_data["remise"].get("seringue") == seringue_response.get("seringue") - 1

def test_soigner_seringue_cow_no(headers, vache_malade, remise_vide):
        # Heal the cow
        malade_vache_response = requests.get(f"{APP_URL}/fermiers/vache", headers=headers).json()
        seringue_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
        soigner_seringue_vache_response = requests.post(f"{APP_URL}/fermiers/vache/soignerSeringue", headers=headers)
        assert soigner_seringue_vache_response.status_code == 200, f"Failed to heal the cow: {soigner_seringue_response.text}"

        # Verify the cow is healed
        updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        assert updated_farm_data["vache"].get("malade") != None
        assert updated_farm_data["remise"].get("seringue") == seringue_response.get("seringue")

def test_nettoyer_cow(headers, vache_sale, fermier_riche):
        # Clean the cow
        sale_vache_response = requests.get(f"{APP_URL}/fermiers/vache", headers=headers).json()
        ecus_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        nettoyer_vache_response = requests.post(f"{APP_URL}/fermiers/vache/nettoyer", headers=headers)
        assert nettoyer_vache_response.status_code == 200, f"Failed to clean the cow: {nettoyer_vache_response.text}"

        # Verify the cow is clean
        updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        assert updated_farm_data["vache"].get("sale") == None
        assert updated_farm_data["ecus"] == ecus_response.get("ecus") - 3

def test_nettoyer_savon_cow(headers, vache_sale, remise_pleine):
        # Clean the cow with soap
        sale_vache_response = requests.get(f"{APP_URL}/fermiers/vache", headers=headers).json()
        savon_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
        nettoyer_savon_vache_response = requests.post(f"{APP_URL}/fermiers/vache/nettoyerSavon", headers=headers)
        assert nettoyer_savon_vache_response.status_code == 200, f"Failed to clean the cow: {nettoyer_savon_vache_response.text}"

        # Verify the cow is clean
        updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        assert updated_farm_data["vache"].get("sale") == None
        assert updated_farm_data["remise"].get("savon") == savon_response.get("savon") - 1

def test_nettoyer_savon_cow_no(headers, vache_sale, remise_vide):
        # Clean the cow with soap
        sale_vache_response = requests.get(f"{APP_URL}/fermiers/vache", headers=headers).json()
        savon_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
        nettoyer_savon_vache_response = requests.post(f"{APP_URL}/fermiers/vache/nettoyerSavon", headers=headers)
        assert nettoyer_savon_vache_response.status_code == 200, f"Failed to clean the cow: {nettoyer_savon_vache_response.text}"

        # Verify the cow is clean
        updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        assert updated_farm_data["vache"].get("sale") != None
        assert updated_farm_data["remise"].get("savon") == savon_response.get("savon") 

def test_mourrir_maigre_cow(headers, vache_saine, vache_maigre, vache_vivante):
        # Kill the cow
        tuer_response = requests.post(f"{APP_URL}/fermiers/vache/tuer", headers=headers)
        assert tuer_response.status_code == 200, f"Failed to kill: {tuer_response.text}"

        # Verify the cow is dead
        updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        assert updated_farm_data["vache"].get("estVivante") == False, "Cow is still alive"

def test_mourrir_malade_cow(headers, vache_malade, vache_adulte, vache_vivante):
        # Kill the cow
        tuer_response = requests.post(f"{APP_URL}/fermiers/vache/tuer", headers=headers)
        assert tuer_response.status_code == 200, f"Failed to kill: {tuer_response.text}"

        # Verify the cow is dead
        updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        assert updated_farm_data["vache"].get("estVivante") == False, "Cow is still alive"

def test_survivre_cow(headers, vache_saine, vache_adulte, vache_vivante):
        # Kill the cow
        tuer_response = requests.post(f"{APP_URL}/fermiers/vache/tuer", headers=headers)
        assert tuer_response.status_code == 200, f"Failed to kill: {tuer_response.text}"

        # Verify the cow is dead
        updated_farm_data = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
        assert updated_farm_data["vache"].get("estVivante") == True, "Cow is dead"
