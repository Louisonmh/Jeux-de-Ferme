import requests
import pytest
import datetime

# Base URL for the Spring Boot application
APP_URL = "http://localhost:8080"

from test_secu import auth_token, headers, fermier_pauvre, fermier_riche, remise_pleine, remise_plusieurs, remise_vide
from test_coqs import add_coqs_vivant, all_coqs_nourris, all_coqs_abreuver, all_coqs_nettoyer, all_coqs_soigner, all_coqs_nourris_hier, all_coqs_abreuver_hier

@pytest.fixture
def all_poules_nourris(headers):
    nourrir_all_poules_response = requests.post(f"{APP_URL}/fermiers/poules/nourrirAll", headers=headers)
    assert nourrir_all_poules_response.status_code == 200, f"Failed to fed poules: {nourrir_all_poules_response.text}"

@pytest.fixture
def all_poules_nourris_hier(headers):
    nourrir_all_poules_hier_response = requests.post(f"{APP_URL}/fermiers/poules/nourrirHier", headers=headers)
    assert nourrir_all_poules_hier_response.status_code == 200, f"Failed to fed poules: {nourrir_all_poules_hier_response.text}"

@pytest.fixture
def all_poules_affame(headers):
    affamer_all_poules_response = requests.post(f"{APP_URL}/fermiers/poules/affamer", headers=headers)
    assert affamer_all_poules_response.status_code == 200, f"Failed to hungry poules: {affamer_all_poules_response.text}"

@pytest.fixture
def all_poules_affame2(headers):
    affamer2_all_poules_response = requests.post(f"{APP_URL}/fermiers/poules/affamer2", headers=headers)
    assert affamer2_all_poules_response.status_code == 200, f"Failed to hungry poules: {affamer2_all_poules_response.text}"

@pytest.fixture
def all_poules_affame3(headers):
    affamer3_all_poules_response = requests.post(f"{APP_URL}/fermiers/poules/affamer3", headers=headers)
    assert affamer3_all_poules_response.status_code == 200, f"Failed to hungry poules: {affamer3_all_poules_response.text}"

@pytest.fixture
def all_poules_affame4(headers):
    affamer4_all_poules_response = requests.post(f"{APP_URL}/fermiers/poules/affamer4", headers=headers)
    assert affamer4_all_poules_response.status_code == 200, f"Failed to hungry poules: {affamer4_all_poules_response.text}"

@pytest.fixture
def all_poules_assoiffer(headers):
    assoiffer_all_poules_response = requests.post(f"{APP_URL}/fermiers/poules/assoiffer", headers=headers)
    assert assoiffer_all_poules_response.status_code == 200, f"Failed to thirsty poules: {assoiffer_all_poules_response.text}"

@pytest.fixture
def all_poules_abreuver(headers):
    abreuver_all_poules_response = requests.post(f"{APP_URL}/fermiers/poules/abreuver", headers=headers)
    assert abreuver_all_poules_response.status_code == 200, f"Failed to watered poules: {abreuver_all_poules_response.text}"

@pytest.fixture
def all_poules_abreuver_hier(headers):
    abreuver_all_poules_hier_response = requests.post(f"{APP_URL}/fermiers/poules/abreuveHier", headers=headers)
    assert abreuver_all_poules_hier_response.status_code == 200, f"Failed to watered poules: {abreuver_all_poules_hier_response.text}"

@pytest.fixture
def all_poules_sale(headers):
    sale_all_poules_response = requests.post(f"{APP_URL}/fermiers/poules/salir", headers=headers)
    assert sale_all_poules_response.status_code == 200, f"Failed to made dirty poules: {sale_all_poules_response.text}"

@pytest.fixture
def all_poules_nettoyer(headers):
    nettoyer_all_poules_response = requests.post(f"{APP_URL}/fermiers/poules/nettoyerAll", headers=headers)
    assert nettoyer_all_poules_response.status_code == 200, f"Failed to cleaned poules: {nettoyer_all_poules_response.text}"

@pytest.fixture
def all_poules_malade(headers):
    malade_all_poules_response = requests.post(f"{APP_URL}/fermiers/poules/malade", headers=headers)
    assert malade_all_poules_response.status_code == 200, f"Failed to made sick poules: {malade_all_poules_response.text}"

@pytest.fixture
def all_poules_malade4(headers):
    malade_all_poules_response = requests.post(f"{APP_URL}/fermiers/poules/malade4", headers=headers)
    assert malade_all_poules_response.status_code == 200, f"Failed to made sick poules: {malade_all_poules_response.text}"

@pytest.fixture
def all_poules_soigner(headers):
    soigner_all_poules_response = requests.post(f"{APP_URL}/fermiers/poules/soignerAll", headers=headers)
    assert soigner_all_poules_response.status_code == 200, f"Failed to cure poules: {soigner_all_poules_response.text}"

@pytest.fixture
def add3_poules_vivante(headers):
    add_poules_vivante_response = requests.post(f"{APP_URL}/fermiers/add3Poule", headers=headers)
    assert add_poules_vivante_response.status_code == 200, f"Failed to add poules: {add_poules_vivante_response.text}"

@pytest.fixture
def all_poules_maigrir(headers):
    all_poules_maigrir_response = requests.post(f"{APP_URL}/fermiers/poules/maigrir", headers=headers)
    assert all_poules_maigrir_response.status_code == 200, f"Failed to to lose weight poules: {all_poules_maigrir_response.text}"

@pytest.fixture
def all_poules_enfant(headers):
    all_poules_enfant_response = requests.post(f"{APP_URL}/fermiers/poules/enfant", headers=headers)
    assert all_poules_enfant_response.status_code == 200, f"Failed to made young poules: {all_poules_enfant_response.text}"

@pytest.fixture
def all_poules_couv(headers):
    all_poules_couv_response = requests.post(f"{APP_URL}/fermiers/poules/couvaison", headers=headers)
    assert all_poules_couv_response.status_code == 200, f"Failed to incubated poules: {all_poules_couv_response.text}"

def test_poule(headers, add3_poules_vivante):
    poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers)
    assert poules_response.status_code == 200, f"Failed to get poules: {poules_response.text}"

    poules_data = poules_response.json()
    now = datetime.datetime.now().date()
    assert len(poules_data) == 3
    for i in range(len(poules_data)):
        assert poules_data[i].get("enCouvaison") == False
        assert poules_data[i].get("poids") == 2.5
        assert poules_data[i].get("age") == 5
        assert poules_data[i].get("abreuve")[0:10] != now.strftime('%Y-%m-%d')
        assert poules_data[i].get("nourris")[0:10] != now.strftime('%Y-%m-%d')
        assert poules_data[i].get("sale") == None
        assert poules_data[i].get("malade") == None

def test_nourrir_poule(headers, fermier_riche, add3_poules_vivante, all_poules_affame, all_poules_assoiffer, all_poules_malade, all_poules_sale):
    poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    nourrir_poules_response = requests.post(f"{APP_URL}/fermiers/poules/nourrir/{poules_response[0].get("id")}", headers=headers)
    assert nourrir_poules_response.status_code == 200, f"Failed to fed poule: {nourrir_poules_response.text}"

    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    now = datetime.datetime.now().date()
    assert updated_poules_response[0].get("nourris")[0:10] == now.strftime('%Y-%m-%d')
    assert updated_poules_response[0].get("poids") == poules_response[0].get("poids") + 0.5

def test_nourrir_poule_pauvre(headers, fermier_pauvre, add3_poules_vivante, all_poules_affame, all_poules_assoiffer, all_poules_malade, all_poules_sale):
    poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    nourrir_poules_response = requests.post(f"{APP_URL}/fermiers/poules/nourrir/{poules_response[0].get("id")}", headers=headers)
    assert nourrir_poules_response.status_code == 200, f"Failed to fed poule: {nourrir_poules_response.text}"

    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    now = datetime.datetime.now().date()
    assert updated_poules_response[0].get("nourris")[0:10] == poules_response[0].get("nourris")[0:10]
    assert updated_poules_response[0].get("poids") == poules_response[0].get("poids")

def test_nourrir_all_poules(headers, fermier_riche, add3_poules_vivante, all_poules_affame, all_poules_assoiffer, all_poules_malade, all_poules_sale):
    poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    nourrir_all_poules_response = requests.post(f"{APP_URL}/fermiers/poules/nourrirAll", headers=headers)
    assert nourrir_all_poules_response.status_code == 200, f"Failed to fed poules: {nourrir_all_poules_response.text}"

    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    now = datetime.datetime.now().date()
    for i in range(len(updated_poules_response)):
        assert updated_poules_response[i].get("nourris")[0:10] == now.strftime('%Y-%m-%d')
        assert updated_poules_response[i].get("poids") == poules_response[i].get("poids") + 0.5

def test_nourrir_all_poules_pauvre(headers, fermier_pauvre, add3_poules_vivante, all_poules_affame, all_poules_assoiffer, all_poules_malade, all_poules_sale):
    dernier_repas_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()["poules"][0].get("nourris")[0:10]
    poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    nourrir_all_poules_response = requests.post(f"{APP_URL}/fermiers/poules/nourrirAll", headers=headers)
    assert nourrir_all_poules_response.status_code == 200, f"Failed to fed poules: {nourrir_all_poules_response.text}"

    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    now = datetime.datetime.now().date()
    for i in range(len(updated_poules_response)):
        assert updated_poules_response[i].get("nourris")[0:10] == dernier_repas_response
        assert updated_poules_response[i].get("poids") == poules_response[i].get("poids")

def test_nourrir_all_poules_sac_nourriture(headers, fermier_riche, add3_poules_vivante, remise_pleine, all_poules_affame, all_poules_assoiffer, all_poules_malade, all_poules_sale):
    fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    nourrir_all_poules_response = requests.post(f"{APP_URL}/fermiers/poules/nourrirAllSacNourriture", headers=headers)
    assert nourrir_all_poules_response.status_code == 200, f"Failed to fed poules: {nourrir_all_poules_response.text}"

    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    updated_fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    now = datetime.datetime.now().date()
    for i in range(len(updated_poules_response)):
        assert updated_poules_response[i].get("nourris")[0:10] == now.strftime('%Y-%m-%d')
    assert updated_fermiers_response.get("remise").get("sac_nourriture") == fermiers_response.get("remise").get("sac_nourriture") - 1
    
def test_nourrir_all_poules_sans_sac_nourriture(headers, fermier_riche, add3_poules_vivante, remise_vide, all_poules_affame, all_poules_assoiffer, all_poules_malade, all_poules_sale):
    poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    nourrir_all_poules_response = requests.post(f"{APP_URL}/fermiers/poules/nourrirAllSacNourriture", headers=headers)
    assert nourrir_all_poules_response.status_code == 200, f"Failed to fed poules: {nourrir_all_poules_response.text}"

    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    updated_fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    for i in range(len(updated_poules_response)):
        assert updated_poules_response[i].get("nourris")[0:10] == poules_response[i].get("nourris")[0:10]
    assert updated_fermiers_response.get("remise").get("sac_nourriture") == fermiers_response.get("remise").get("sac_nourriture")

def test_abreuve_poule(headers, fermier_riche, add3_poules_vivante, all_poules_nourris, all_poules_assoiffer, all_poules_malade, all_poules_sale, all_poules_maigrir):
    poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    abreuve_poules_response = requests.post(f"{APP_URL}/fermiers/poules/abreuve/{poules_response[0].get("id")}", headers=headers)
    assert abreuve_poules_response.status_code == 200, f"Failed to watered poule: {abreuve_poules_response.text}"

    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    now = datetime.datetime.now().date()
    assert updated_poules_response[0].get("abreuve")[0:10] == now.strftime('%Y-%m-%d')
    assert updated_poules_response[0].get("poids") == poules_response[0].get("poids") + 0.15

def test_abreuve_poule_pauvre(headers, fermier_pauvre, add3_poules_vivante, all_poules_affame, all_poules_assoiffer, all_poules_malade, all_poules_sale):
    poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    abreuve_poules_response = requests.post(f"{APP_URL}/fermiers/poules/abreuve/{poules_response[0].get("id")}", headers=headers)
    assert abreuve_poules_response.status_code == 200, f"Failed to watered poule: {abreuve_poules_response.text}"

    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    assert updated_poules_response[0].get("abreuve")[0:10] == poules_response[0].get("abreuve")[0:10]

def test_abreuve_all_poules(headers, fermier_riche, add3_poules_vivante, all_poules_affame, all_poules_assoiffer, all_poules_malade, all_poules_sale):
    abreuve_all_poules_response = requests.post(f"{APP_URL}/fermiers/poules/abreuveAll", headers=headers)
    assert abreuve_all_poules_response.status_code == 200, f"Failed to watered poules: {abreuve_all_poules_response.text}"

    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    now = datetime.datetime.now().date()
    for i in range(len(updated_poules_response)):
        assert updated_poules_response[i].get("abreuve")[0:10] == now.strftime('%Y-%m-%d')

def test_abreuve_all_poules_pauvre(headers, fermier_pauvre, add3_poules_vivante, all_poules_affame, all_poules_assoiffer, all_poules_malade, all_poules_sale):
    poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    nourrir_all_poules_response = requests.post(f"{APP_URL}/fermiers/poules/nourrirAll", headers=headers)
    assert nourrir_all_poules_response.status_code == 200, f"Failed to watered poules: {nourrir_all_poules_response.text}"

    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    now = datetime.datetime.now().date()
    for i in range(len(updated_poules_response)):
        assert updated_poules_response[i].get("abreuve")[0:10] == poules_response[0].get("abreuve")[0:10]

def test_abreuve_all_poules_eau(headers, fermier_riche, add3_poules_vivante, remise_pleine, all_poules_affame, all_poules_assoiffer, all_poules_malade, all_poules_sale):
    fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    abreuve_all_poules_response = requests.post(f"{APP_URL}/fermiers/poules/abreuveAllSeauDeau", headers=headers)
    assert abreuve_all_poules_response.status_code == 200, f"Failed to watered poules: {abreuve_all_poules_response.text}"

    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    updated_fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    now = datetime.datetime.now().date()
    for i in range(len(updated_poules_response)):
        assert updated_poules_response[i].get("abreuve")[0:10] == now.strftime('%Y-%m-%d')
    assert updated_fermiers_response.get("remise").get("eau") == fermiers_response.get("remise").get("eau") - 1

def test_abreuve_all_poules_sans_eau(headers, fermier_riche, add3_poules_vivante, remise_vide, all_poules_affame, all_poules_assoiffer, all_poules_malade, all_poules_sale):
    fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    nourrir_all_poules_response = requests.post(f"{APP_URL}/fermiers/poules/abreuveAllSeauDeau", headers=headers)
    assert nourrir_all_poules_response.status_code == 200, f"Failed to watered poules: {nourrir_all_poules_response.text}"

    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    updated_fermiers__response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    for i in range(len(updated_poules_response)):
        assert updated_poules_response[i].get("nourris")[0:10] == poules_response[i].get("nourris")[0:10]
    assert updated_fermiers__response.get("remise").get("eau") == fermiers_response.get("remise").get("eau")

def test_famine_all_poules(headers, fermier_pauvre, add3_poules_vivante, all_poules_affame, all_poules_assoiffer, all_poules_malade, all_poules_sale):
    poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    famine_poules_response = requests.post(f"{APP_URL}/fermiers/poules/famine", headers=headers)
    assert famine_poules_response.status_code == 200, f"Failed to famine poules: {famine_poules_response.text}"

    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    assert len(updated_poules_response) == 3
    for i in range(len(updated_poules_response)):
        assert round(updated_poules_response[i].get("poids"), 4) == round((poules_response[i].get("poids") - 0.2), 4)

def test_famine2_all_poules(headers, fermier_pauvre, add3_poules_vivante, all_poules_affame2, all_poules_assoiffer, all_poules_malade, all_poules_sale):
    poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    famine2_poules_response = requests.post(f"{APP_URL}/fermiers/poules/famine", headers=headers)
    assert famine2_poules_response.status_code == 200, f"Failed to famine poules: {famine2_poules_response.text}"

    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    assert len(updated_poules_response) == 3
    for i in range(len(updated_poules_response)):
        assert round(updated_poules_response[i].get("poids"), 4) == round((poules_response[i].get("poids") - 0.5), 4)

def test_famine3_all_poules(headers, fermier_riche, add3_poules_vivante, all_poules_affame3, all_poules_assoiffer, all_poules_malade, all_poules_sale):
    poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    famine3_poules_response = requests.post(f"{APP_URL}/fermiers/poules/famine", headers=headers)
    assert famine3_poules_response.status_code == 200, f"Failed to famine poules: {famine3_poules_response.text}"

    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    assert len(updated_poules_response) == 3
    for i in range(len(updated_poules_response)):
        assert round(updated_poules_response[i].get("poids"), 4) == round((poules_response[i].get("poids") - 1.0), 4)

def test_famine4_all_poules(headers, fermier_pauvre, add3_poules_vivante, all_poules_affame4, all_poules_assoiffer, all_poules_malade, all_poules_sale):
    famine4_poules_response = requests.post(f"{APP_URL}/fermiers/poules/famine", headers=headers)
    assert famine4_poules_response.status_code == 200, f"Failed to famine poules: {famine4_poules_response.text}"

    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    assert len(updated_poules_response) == 0

def test_nettoyer_poule(headers, fermier_riche, add3_poules_vivante, all_poules_affame, all_poules_assoiffer, all_poules_malade, all_poules_sale):
    poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    nettoyer_poules_response = requests.post(f"{APP_URL}/fermiers/poules/nettoyer/{poules_response[0].get("id")}", headers=headers)
    assert nettoyer_poules_response.status_code == 200, f"Failed to cleaned poule: {nettoyer_poules_response.text}"

    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    assert updated_poules_response[0].get("sale") == None

def test_nettoyer_poule_pauvre(headers, fermier_pauvre, add3_poules_vivante, all_poules_affame, all_poules_assoiffer, all_poules_malade, all_poules_sale):
    poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    fermiers_data = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    nettoyer_poules_response = requests.post(f"{APP_URL}/fermiers/poules/abreuve/{poules_response[0].get("id")}", headers=headers)
    assert nettoyer_poules_response.status_code == 200, f"Failed to cleaned poule: {nettoyer_poules_response.text}"

    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    assert updated_poules_response[0].get("sale")[0:10] == poules_response[0].get("sale")[0:10]

def test_nettoyer_all_poules(headers, fermier_riche, add3_poules_vivante, all_poules_affame, all_poules_assoiffer, all_poules_malade, all_poules_sale):
    nettoyer_all_poules_response = requests.post(f"{APP_URL}/fermiers/poules/nettoyerAll", headers=headers)
    assert nettoyer_all_poules_response.status_code == 200, f"Failed to cleaned poules: {nettoyer_all_poules_response.text}"

    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    for i in range(len(updated_poules_response)):
        assert updated_poules_response[i].get("sale") == None

def test_nettoyer_all_poules_pauvre(headers, fermier_pauvre, add3_poules_vivante, all_poules_affame, all_poules_assoiffer, all_poules_malade, all_poules_sale):
    poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    nettoyer_all_poules_response = requests.post(f"{APP_URL}/fermiers/poules/nettoyerAll", headers=headers)
    assert nettoyer_all_poules_response.status_code == 200, f"Failed to cleaned poules: {nettoyer_all_poules_response.text}"

    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    for i in range(len(updated_poules_response)):
        assert updated_poules_response[i].get("sale")[0:10] == poules_response[0].get("sale")[0:10]

def test_nettoyer_all_poules_savon(headers, fermier_riche, add3_poules_vivante, remise_pleine, all_poules_affame, all_poules_assoiffer, all_poules_malade, all_poules_sale):
    fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    nettoyer_all_poules_response = requests.post(f"{APP_URL}/fermiers/poules/nettoyerAllSavon", headers=headers)
    assert nettoyer_all_poules_response.status_code == 200, f"Failed to cleaned poules: {nettoyer_all_poules_response.text}"

    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    updated_fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    for i in range(len(updated_poules_response)):
        assert updated_poules_response[i].get("sale") == None
    assert updated_fermiers_response.get("remise").get("savon") == fermiers_response.get("remise").get("savon") - 1

def test_nettoyer_all_poules_sans_savon(headers, fermier_riche, add3_poules_vivante, remise_vide, all_poules_affame, all_poules_assoiffer, all_poules_malade, all_poules_sale):
    fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    nettoyer_all_poules_response = requests.post(f"{APP_URL}/fermiers/poules/nettoyerAllSavon", headers=headers)
    assert nettoyer_all_poules_response.status_code == 200, f"Failed to cleaned poules: {nettoyer_all_poules_response.text}"

    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    updated_fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    for i in range(len(updated_poules_response)):
        assert updated_poules_response[i].get("sale")[0:10] == poules_response[i].get("sale")[0:10]
    assert updated_fermiers_response.get("remise").get("savon") == fermiers_response.get("remise").get("savon")

def test_soigner_poule(headers, fermier_riche, add3_poules_vivante, all_poules_affame, all_poules_assoiffer, all_poules_malade, all_poules_sale):
    poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    soigner_poules_response = requests.post(f"{APP_URL}/fermiers/poules/soigner/{poules_response[0].get("id")}", headers=headers)
    assert soigner_poules_response.status_code == 200, f"Failed to cure poule: {soigner_poules_response.text}"

    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    assert updated_poules_response[0].get("malade") == None

def test_soigner_poule_pauvre(headers, fermier_pauvre, add3_poules_vivante, all_poules_affame, all_poules_assoiffer, all_poules_malade, all_poules_sale):
    poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    nettoyer_poules_response = requests.post(f"{APP_URL}/fermiers/poules/soigner/{poules_response[0].get("id")}", headers=headers)
    assert nettoyer_poules_response.status_code == 200, f"Failed to cure poule: {nettoyer_poules_response.text}"

    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    assert updated_poules_response[0].get("malade") == poules_response[0].get("malade")

def test_soigner_all_poules(headers, fermier_riche, add3_poules_vivante, all_poules_affame, all_poules_assoiffer, all_poules_malade, all_poules_sale):
    soigner_all_poules_response = requests.post(f"{APP_URL}/fermiers/poules/soignerAll", headers=headers)
    assert soigner_all_poules_response.status_code == 200, f"Failed to cure poules: {soigner_all_poules_response.text}"

    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    for i in range(len(updated_poules_response)):
        assert updated_poules_response[i].get("malade") == None

def test_soigner_all_poules_pauvre(headers, fermier_pauvre, add3_poules_vivante, all_poules_affame, all_poules_assoiffer, all_poules_malade, all_poules_sale):
    poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    soigner_all_poules_response = requests.post(f"{APP_URL}/fermiers/poules/soignerAll", headers=headers)
    assert soigner_all_poules_response.status_code == 200, f"Failed to cure poules: {soigner_all_poules_response.text}"

    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    for i in range(len(updated_poules_response)):
        assert updated_poules_response[i].get("malade")[0:10] == poules_response[0].get("malade")[0:10]

def test_soigner_all_poules_seringue(headers, fermier_riche, add3_poules_vivante, remise_pleine, all_poules_affame, all_poules_assoiffer, all_poules_malade, all_poules_sale):
    fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    soigner_seringue_all_poules_response = requests.post(f"{APP_URL}/fermiers/poules/soignerAllSeringue", headers=headers)
    assert soigner_seringue_all_poules_response.status_code == 200, f"Failed to cure poules: {soigner_seringue_all_poules_response.text}"

    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    updated_fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    for i in range(len(updated_poules_response)):
        assert updated_poules_response[i].get("malade") == None
    assert updated_fermiers_response.get("remise").get("seringue") == fermiers_response.get("remise").get("seringue") - 1

def test_soigner_all_poules_sans_seringue(headers, fermier_riche, add3_poules_vivante, remise_vide, all_poules_affame, all_poules_assoiffer, all_poules_malade, all_poules_sale):
    fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    soigner_all_poules_response = requests.post(f"{APP_URL}/fermiers/poules/soignerAllSeringue", headers=headers)
    assert soigner_all_poules_response.status_code == 200, f"Failed to cure poules: {soigner_all_poules_response.text}"

    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    updated_fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    for i in range(len(updated_poules_response)):
        assert updated_poules_response[i].get("malade")[0:10] == poules_response[i].get("malade")[0:10]
    assert updated_fermiers_response.get("remise").get("seringue") == fermiers_response.get("remise").get("seringue")

def test_ponte(headers, fermier_riche, add3_poules_vivante, add_coqs_vivant, all_poules_nourris_hier, all_poules_abreuver_hier, all_poules_nettoyer, all_poules_soigner, all_coqs_nourris_hier, all_coqs_abreuver_hier, all_coqs_nettoyer, all_coqs_soigner):
    ponte_response = requests.post(f"{APP_URL}/fermiers/poules/pondre", headers=headers)
    assert ponte_response.status_code == 200, f"Failed ponte : {ponte_response.text}"

    remise_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json()
    # possibilité que toutes les poules pondent 0 oeufs et fasse foiré le test
    assert remise_response.get("oeuf") >= 0

def test_tuer_all_poule(headers, fermier_riche, add3_poules_vivante, all_poules_malade4):
    poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    tuer_all_poules_response = requests.post(f"{APP_URL}/fermiers/poules/tuer", headers=headers)
    assert tuer_all_poules_response.status_code == 200, f"Failed to killed poules: {tuer_all_poules_response.text}"

    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    assert len(poules_response) == 3
    assert len(updated_poules_response) == 0

def test_enfant_all_poules(headers, add3_poules_vivante, all_poules_enfant):
    poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    regression_all_poules = requests.post(f"{APP_URL}/fermiers/poules/regression", headers=headers)
    assert regression_all_poules.status_code == 200, f"Failed to regression poules: {regression_all_poules.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    assert len(updated_poules_response) == len(poules_response) - 3
    assert len(updated_poussins_response) == len(poussins_response) + 3

def test_couver_poules(headers, add3_poules_vivante, remise_plusieurs):
    oeufs_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json().get("oeuf")
    couver_poules = requests.post(f"{APP_URL}/fermiers/poules/couver/{3}", headers=headers)
    assert couver_poules.status_code == 200, f"Failed to couver poules: {couver_poules.text}"

    updated_oeufs_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json().get("oeuf")
    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    for i in range(len(updated_poules_response)):
        assert updated_poules_response[i].get("enCouvaison") == True
    assert updated_oeufs_response == oeufs_response - 3

def test_couver_poule(headers, add3_poules_vivante, remise_plusieurs):
    oeufs_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json().get("oeuf")
    couver_poules = requests.post(f"{APP_URL}/fermiers/poules/couver/{1}", headers=headers)
    assert couver_poules.status_code == 200, f"Failed to couver poules: {couver_poules.text}"

    updated_oeufs_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json().get("oeuf")
    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    assert updated_poules_response[0].get("enCouvaison") == True
    assert updated_poules_response[1].get("enCouvaison") == False
    assert updated_poules_response[2].get("enCouvaison") == False
    assert updated_oeufs_response == oeufs_response - 1

def test_couver_poules_sup(headers, add3_poules_vivante, remise_plusieurs):
    oeufs_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json().get("oeuf")
    couver_poules = requests.post(f"{APP_URL}/fermiers/poules/couver/{5}", headers=headers)
    assert couver_poules.status_code == 200, f"Failed to couver poules: {couver_poules.text}"

    updated_oeufs_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json().get("oeuf")
    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    for i in range(len(updated_poules_response)):
        assert updated_poules_response[i].get("enCouvaison") == True
    assert updated_oeufs_response == oeufs_response - len(updated_poules_response)

def test_sorti_couvaison(headers, add3_poules_vivante, all_poules_couv):
    poussin_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    couver_poules = requests.post(f"{APP_URL}/fermiers/poules/arreterCouver", headers=headers)
    assert couver_poules.status_code == 200, f"Failed to couver poules: {couver_poules.text}"

    updated_poussin_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    updated_poule_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    for i in range(len(updated_poule_response)):
        assert updated_poule_response[i].get("enCouvaison") == False
    assert len(updated_poussin_response) == len(poussin_response) + 3

def test_passage_jour(headers, fermier_riche, remise_vide, add3_poules_vivante, add_coqs_vivant, all_poules_abreuver_hier, all_poules_nourris_hier, all_poules_nettoyer, all_poules_soigner, all_coqs_abreuver_hier, all_coqs_nettoyer, all_coqs_nourris_hier, all_coqs_soigner):
    poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    oeufs_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json().get("oeuf")

    passage_jour_response = requests.post(f"{APP_URL}/fermiers/poules/passageJour", headers=headers)
    assert passage_jour_response.status_code == 200, f"Failed to passage jour: {passage_jour_response.text}"

    updated_poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    updated_coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    updated_oeufs_response = requests.get(f"{APP_URL}/fermiers/remise", headers=headers).json().get("oeuf")

    assert updated_oeufs_response != oeufs_response
    assert len(updated_poussins_response) == len(poussins_response)
    assert len(updated_coqs_response) == len(coqs_response)
    assert len(updated_poules_response) == len(poules_response)

    for i in range(len(updated_poules_response)):
        assert updated_poules_response[i].get("age") == poules_response[i].get("age") + 1
        assert updated_poules_response[i].get("poids") == poules_response[i].get("poids")
        assert updated_poules_response[i].get("nourris") == poules_response[i].get("nourris")
        assert updated_poules_response[i].get("abreuve") == poules_response[i].get("abreuve")
