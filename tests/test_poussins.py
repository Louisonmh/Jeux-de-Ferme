import requests
import pytest
import datetime

# Base URL for the Spring Boot application
APP_URL = "http://localhost:8080"

from test_secu import auth_token, headers, fermier_pauvre, fermier_riche, remise_pleine, remise_vide
from test_poules import add3_poules_vivante
from test_coqs import add_coqs_vivant

@pytest.fixture
def all_poussins_nourris(headers):
    nourrir_all_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/nourrirAll", headers=headers)
    assert nourrir_all_poussins_response.status_code == 200, f"Failed to fed poussins: {nourrir_all_poussins_response.text}"

@pytest.fixture
def all_poussins_nourris_hier(headers):
    nourrir_all_poussins_hier_response = requests.post(f"{APP_URL}/fermiers/poussins/nourrirHier", headers=headers)
    assert nourrir_all_poussins_hier_response.status_code == 200, f"Failed to fed poussins: {nourrir_all_poussins_hier_response.text}"

@pytest.fixture
def all_poussins_affame(headers):
    affamer_all_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/affamer", headers=headers)
    assert affamer_all_poussins_response.status_code == 200, f"Failed to fed poussins: {affamer_all_poussins_response.text}"

@pytest.fixture
def all_poussins_affame2(headers):
    affamer2_all_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/affamer2", headers=headers)
    assert affamer2_all_poussins_response.status_code == 200, f"Failed to fed poussins: {affamer2_all_poussins_response.text}"

@pytest.fixture
def all_poussins_affame3(headers):
    affamer3_all_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/affamer3", headers=headers)
    assert affamer3_all_poussins_response.status_code == 200, f"Failed to fed poussins: {affamer3_all_poussins_response.text}"

@pytest.fixture
def all_poussins_affame4(headers):
    affamer4_all_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/affamer4", headers=headers)
    assert affamer4_all_poussins_response.status_code == 200, f"Failed to fed poussins: {affamer4_all_poussins_response.text}"

@pytest.fixture
def all_poussins_assoiffer(headers):
    assoiffer_all_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/assoiffer", headers=headers)
    assert assoiffer_all_poussins_response.status_code == 200, f"Failed to fed poussins: {assoiffer_all_poussins_response.text}"

@pytest.fixture
def all_poussins_abreuver(headers):
    abreuver_all_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/abreuveAll", headers=headers)
    assert abreuver_all_poussins_response.status_code == 200, f"Failed to fed poussins: {abreuver_all_poussins_response.text}"

@pytest.fixture
def all_poussins_abreuver_hier(headers):
    abreuver_all_poussins_hier_response = requests.post(f"{APP_URL}/fermiers/poussins/abreuveHier", headers=headers)
    assert abreuver_all_poussins_hier_response.status_code == 200, f"Failed to fed poussins: {abreuver_all_poussins_hier_response.text}"

@pytest.fixture
def all_poussins_sale(headers):
    sale_all_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/salir", headers=headers)
    assert sale_all_poussins_response.status_code == 200, f"Failed to fed poussins: {sale_all_poussins_response.text}"

@pytest.fixture
def all_poussins_nettoyer(headers):
    nettoyer_all_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/nettoyerAll", headers=headers)
    assert nettoyer_all_poussins_response.status_code == 200, f"Failed to fed poussins: {nettoyer_all_poussins_response.text}"

@pytest.fixture
def all_poussins_malade(headers):
    malade_all_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/malade", headers=headers)
    assert malade_all_poussins_response.status_code == 200, f"Failed to fed poussins: {malade_all_poussins_response.text}"

@pytest.fixture
def all_poussins_malade4(headers):
    malade_all_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/malade4", headers=headers)
    assert malade_all_poussins_response.status_code == 200, f"Failed to fed poussins: {malade_all_poussins_response.text}"

@pytest.fixture
def all_poussins_soigner(headers):
    soigner_all_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/soignerAll", headers=headers)
    assert soigner_all_poussins_response.status_code == 200, f"Failed to fed poussins: {soigner_all_poussins_response.text}"

@pytest.fixture
def add_poussins_vivant(headers):
    add_poussins_vivant_response = requests.post(f"{APP_URL}/fermiers/add3Poussin", headers=headers)
    assert add_poussins_vivant_response.status_code == 200, f"Failed to revive poussins: {add_poussins_vivant_response.text}"

@pytest.fixture
def all_poussins_maigrir(headers):
    all_poussins_maigrir_response = requests.post(f"{APP_URL}/fermiers/poussins/maigrir", headers=headers)
    assert all_poussins_maigrir_response.status_code == 200, f"Failed to revive poussins: {all_poussins_maigrir_response.text}"

@pytest.fixture
def all_poussins_adultes(headers):
    all_poussins_adultes_response = requests.post(f"{APP_URL}/fermiers/poussins/adultes", headers=headers)
    assert all_poussins_adultes_response.status_code == 200, f"Failed to made poussins adultes: {all_poussins_adultes_response.text}"

def test_poussin(headers, add_poussins_vivant):
    poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers)
    assert poussins_response.status_code == 200, f"Failed to get poussins: {poussins_response.text}"

    poussins_data =poussins_response.json()
    now = datetime.datetime.now().date()
    assert len(poussins_data) == 3
    for i in range(len(poussins_data)):
        assert poussins_data[i].get("poids") == 0.5
        assert poussins_data[i].get("age") == 0
        assert poussins_data[i].get("abreuve")[0:10] != now.strftime('%Y-%m-%d')
        assert poussins_data[i].get("nourris")[0:10] != now.strftime('%Y-%m-%d')
        assert poussins_data[i].get("sale") == None
        assert poussins_data[i].get("malade") == None

def test_nourrir_poussin(headers, fermier_riche, add_poussins_vivant, all_poussins_affame, all_poussins_assoiffer):
    poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    nourrir_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/nourrir/{poussins_response[0].get("id")}", headers=headers)
    assert nourrir_poussins_response.status_code == 200, f"Failed to fed poussin: {nourrir_poussins_response.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    now = datetime.datetime.now().date()
    assert updated_poussins_response[0].get("nourris")[0:10] == now.strftime('%Y-%m-%d')
    assert updated_poussins_response[0].get("poids") == poussins_response[0].get("poids") + 0.5

def test_nourrir_poussin_pauvre(headers, fermier_pauvre, add_poussins_vivant, all_poussins_affame, all_poussins_assoiffer):
    poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    nourrir_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/nourrir/{poussins_response[0].get("id")}", headers=headers)
    assert nourrir_poussins_response.status_code == 200, f"Failed to fed poussin: {nourrir_poussins_response.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    assert updated_poussins_response[0].get("nourris")[0:10] == poussins_response[0].get("nourris")[0:10]

def test_nourrir_all_poussins(headers, fermier_riche, add_poussins_vivant, all_poussins_affame, all_poussins_assoiffer):
    nourrir_all_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/nourrirAll", headers=headers)
    assert nourrir_all_poussins_response.status_code == 200, f"Failed to fed poussins: {nourrir_all_poussins_response.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    now = datetime.datetime.now().date()
    for i in range(len(updated_poussins_response)):
        assert updated_poussins_response[i].get("nourris")[0:10] == now.strftime('%Y-%m-%d')

def test_nourrir_all_poussins_pauvre(headers, fermier_pauvre, add_poussins_vivant, all_poussins_affame, all_poussins_assoiffer):
    poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    nourrir_all_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/nourrirAll", headers=headers)
    assert nourrir_all_poussins_response.status_code == 200, f"Failed to fed poussins: {nourrir_all_poussins_response.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    now = datetime.datetime.now().date()
    for i in range(len(updated_poussins_response)):
        assert updated_poussins_response[i].get("nourris")[0:10] == poussins_response[0].get("nourris")[0:10]
        assert updated_poussins_response[i].get("poids") == poussins_response[i].get("poids")

def test_nourrir_all_poussins_sac_nourriture(headers, remise_pleine, add_poussins_vivant, all_poussins_affame, all_poussins_assoiffer):
    fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    nourrir_all_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/nourrirAllSacNourriture", headers=headers)
    assert nourrir_all_poussins_response.status_code == 200, f"Failed to fed poussins: {nourrir_all_poussins_response.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    updated_fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    now = datetime.datetime.now().date()
    for i in range(len(updated_poussins_response)):
        assert updated_poussins_response[i].get("nourris")[0:10] == now.strftime('%Y-%m-%d')
        assert updated_poussins_response[i].get("poids") == poussins_response[i].get("poids") + 0.5
    assert updated_fermiers_response.get("remise").get("sac_nourriture") == fermiers_response.get("remise").get("sac_nourriture") - 1

def test_nourrir_all_poussins_sans_sac_nourriture(headers, fermier_riche, add_poussins_vivant, remise_vide, all_poussins_affame, all_poussins_assoiffer):
    fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    coqs_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    nourrir_all_coqs_response = requests.post(f"{APP_URL}/fermiers/poussins/nourrirAllSacNourriture", headers=headers)
    assert nourrir_all_coqs_response.status_code == 200, f"Failed to fed poussins: {nourrir_all_coqs_response.text}"

    updated_coqs_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    updated_fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    for i in range(len(updated_coqs_response)):
        assert updated_coqs_response[i].get("nourris")[0:10] == coqs_response[i].get("nourris")[0:10]
    assert updated_fermiers_response.get("remise").get("sac_nourriture") == fermiers_response.get("remise").get("sac_nourriture")

def test_abreuve_poussin(headers, fermier_riche, add_poussins_vivant, all_poussins_assoiffer, all_poussins_nourris):
    poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    abreuve_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/abreuve/{poussins_response[0].get("id")}", headers=headers)
    assert abreuve_poussins_response.status_code == 200, f"Failed to watered poussin: {abreuve_poussins_response.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    now = datetime.datetime.now().date()
    assert updated_poussins_response[0].get("abreuve")[0:10] == now.strftime('%Y-%m-%d')
    assert updated_poussins_response[0].get("poids") == poussins_response[0].get("poids") + 0.15

def test_abreuve_poussin_pauvre(headers, fermier_pauvre, add_poussins_vivant, all_poussins_assoiffer, all_poussins_nourris):
    poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    abreuve_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/abreuve/{1}", headers=headers)
    assert abreuve_poussins_response.status_code == 200, f"Failed to watered poussin: {abreuve_poussins_response.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    assert updated_poussins_response[0].get("abreuve")[0:10] == poussins_response[0].get("abreuve")[0:10]

def test_abreuve_all_poussins(headers, fermier_riche, add_poussins_vivant, all_poussins_assoiffer, all_poussins_nourris):
    abreuve_all_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/abreuveAll", headers=headers)
    assert abreuve_all_poussins_response.status_code == 200, f"Failed to watered poussins: {abreuve_all_poussins_response.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    now = datetime.datetime.now().date()
    for i in range(len(updated_poussins_response)):
        assert updated_poussins_response[i].get("abreuve")[0:10] == now.strftime('%Y-%m-%d')

def test_abreuve_all_poussins_pauvre(headers, fermier_pauvre, add_poussins_vivant, all_poussins_affame, all_poussins_assoiffer):
    poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    nourrir_all_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/abreuveAll", headers=headers)
    assert nourrir_all_poussins_response.status_code == 200, f"Failed to watered poussins: {nourrir_all_poussins_response.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    now = datetime.datetime.now().date()
    for i in range(len(updated_poussins_response)):
        assert updated_poussins_response[i].get("abreuve")[0:10] == poussins_response[i].get("abreuve")[0:10]
        assert updated_poussins_response[i].get("poids") == poussins_response[i].get("poids")

def test_abreuve_all_poussins_eau(headers, remise_pleine, add_poussins_vivant, all_poussins_assoiffer):
    fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    abreuve_all_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/abreuveAllSeauDeau", headers=headers)
    assert abreuve_all_poussins_response.status_code == 200, f"Failed to watered poussins: {abreuve_all_poussins_response.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    updated_fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    now = datetime.datetime.now().date()
    for i in range(len(updated_poussins_response)):
        assert updated_poussins_response[i].get("abreuve")[0:10] == now.strftime('%Y-%m-%d')
    assert updated_fermiers_response.get("remise").get("eau") == fermiers_response.get("remise").get("eau") - 1

def test_abreuve_all_poussins_sans_eau(headers, fermier_riche, add_poussins_vivant, remise_vide, all_poussins_affame, all_poussins_assoiffer):
    fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    nourrir_all_coqs_response = requests.post(f"{APP_URL}/fermiers/poussins/abreuveAllSeauDeau", headers=headers)
    assert nourrir_all_coqs_response.status_code == 200, f"Failed to watered poussins: {nourrir_all_coqs_response.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    updated_fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    for i in range(len(updated_poussins_response)):
        assert updated_poussins_response[i].get("abreuve")[0:10] == poussins_response[i].get("abreuve")[0:10]
    assert updated_fermiers_response.get("remise").get("eau") == fermiers_response.get("remise").get("eau")

def test_famine_all_poussins(headers, add_poussins_vivant, all_poussins_affame):
    poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    famine_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/famine", headers=headers)
    assert famine_poussins_response.status_code == 200, f"Failed to famine poussins: {famine_poussins_response.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    assert len(updated_poussins_response) == 3
    for i in range(len(updated_poussins_response)):
        assert round(updated_poussins_response[i].get("poids"), 4) == round((poussins_response[i].get("poids") - 0.2), 4)

def test_famine2_all_poussins(headers, add_poussins_vivant, all_poussins_affame2):
    poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    famine2_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/famine", headers=headers)
    assert famine2_poussins_response.status_code == 200, f"Failed to famine poussins: {famine2_poussins_response.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    assert len(updated_poussins_response) == 3
    for i in range(len(updated_poussins_response)):
        assert round(updated_poussins_response[i].get("poids"), 4) == round((poussins_response[i].get("poids") - 0.5), 4)

def test_famine3_all_poussins(headers, add_poussins_vivant, all_poussins_affame3):
    poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    famine3_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/famine", headers=headers)
    assert famine3_poussins_response.status_code == 200, f"Failed to famine poussins: {famine3_poussins_response.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    assert len(updated_poussins_response) == 3
    for i in range(len(updated_poussins_response)):
        assert round(updated_poussins_response[i].get("poids"), 4) == round((poussins_response[i].get("poids") - 1.0), 4)

def test_famine4_all_poussins(headers, add_poussins_vivant, all_poussins_affame4):
    famine4_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/famine", headers=headers)
    assert famine4_poussins_response.status_code == 200, f"Failed to famine poussins: {famine4_poussins_response.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    assert len(updated_poussins_response) == 0

def test_nettoyer_poussin(headers, fermier_riche, add_poussins_vivant, all_poussins_affame, all_poussins_assoiffer, all_poussins_sale):
    poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    nourrir_coqs_response = requests.post(f"{APP_URL}/fermiers/poussins/nettoyer/{poussins_response[0].get("id")}", headers=headers)
    assert nourrir_coqs_response.status_code == 200, f"Failed to cleaned coq: {nourrir_coqs_response.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    assert updated_poussins_response[0].get("sale") == None

def test_nettoyer_poussin_pauvre(headers, fermier_pauvre, add_poussins_vivant, all_poussins_affame, all_poussins_assoiffer, all_poussins_sale):
    poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    nourrir_coqs_response = requests.post(f"{APP_URL}/fermiers/poussins/nettoyer/{poussins_response[0].get("id")}", headers=headers)
    assert nourrir_coqs_response.status_code == 200, f"Failed to cleaned coq: {nourrir_coqs_response.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    assert updated_poussins_response[0].get("sale")[0:10] == poussins_response[0].get("sale")[0:10]

def test_nettoyer_all_poussins(headers, fermier_riche, add_poussins_vivant, all_poussins_sale):
    nettoyer_all_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/nettoyerAll", headers=headers)
    assert nettoyer_all_poussins_response.status_code == 200, f"Failed to cleaned poussins: {nettoyer_all_poussins_response.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    for i in range(len(updated_poussins_response)):
        assert updated_poussins_response[i].get("sale") == None

def test_nettoyer_all_poussins_pauvre(headers, fermier_pauvre, add_poussins_vivant, all_poussins_affame, all_poussins_assoiffer, all_poussins_sale):
    poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    nourrir_all_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/nettoyerAll", headers=headers)
    assert nourrir_all_poussins_response.status_code == 200, f"Failed to cleaned poussins: {nourrir_all_poussins_response.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    now = datetime.datetime.now().date()
    for i in range(len(updated_poussins_response)):
        assert updated_poussins_response[i].get("sale")[0:10] == poussins_response[0].get("sale")[0:10]
        assert updated_poussins_response[i].get("poids") == poussins_response[i].get("poids")

def test_nettoyer_all_poussins_savon(headers, remise_pleine, add_poussins_vivant, all_poussins_sale):
    fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    abreuve_all_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/nettoyerAllSavon", headers=headers)
    assert abreuve_all_poussins_response.status_code == 200, f"Failed to cleaned poussins: {abreuve_all_poussins_response.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    updates_fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    for i in range(len(updated_poussins_response)):
        assert updated_poussins_response[i].get("sale") == None
    assert updates_fermiers_response.get("remise").get("savon") == fermiers_response.get("remise").get("savon") - 1

def test_nettoyer_all_poussins_sans_savon(headers, fermier_riche, add_poussins_vivant, remise_vide, all_poussins_affame, all_poussins_assoiffer, all_poussins_sale):
    fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    nourrir_all_coqs_response = requests.post(f"{APP_URL}/fermiers/poussins/nettoyerAllSavon", headers=headers)
    assert nourrir_all_coqs_response.status_code == 200, f"Failed to cleaned poussins: {nourrir_all_coqs_response.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    updates_fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    for i in range(len(updated_poussins_response)):
        assert updated_poussins_response[i].get("sale")[0:10] == poussins_response[i].get("sale")[0:10]
    assert updates_fermiers_response.get("remise").get("savon") == fermiers_response.get("remise").get("savon")

def test_soigner_poussin(headers, fermier_riche, add_poussins_vivant, all_poussins_affame, all_poussins_assoiffer, all_poussins_sale, all_poussins_malade):
    poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    nourrir_coqs_response = requests.post(f"{APP_URL}/fermiers/poussins/soigner/{poussins_response[0].get("id")}", headers=headers)
    assert nourrir_coqs_response.status_code == 200, f"Failed to cure coq: {nourrir_coqs_response.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    assert updated_poussins_response[0].get("malade") == None

def test_soigner_poussin_pauvre(headers, fermier_pauvre, add_poussins_vivant, all_poussins_affame, all_poussins_assoiffer, all_poussins_sale, all_poussins_malade):
    poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    nourrir_coqs_response = requests.post(f"{APP_URL}/fermiers/poussins/soigner/{poussins_response[0].get("id")}", headers=headers)
    assert nourrir_coqs_response.status_code == 200, f"Failed to cure coq: {nourrir_coqs_response.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    assert updated_poussins_response[0].get("malade")[0:10] == poussins_response[0].get("malade")[0:10]

def test_soigner_all_poussins(headers, fermier_riche, add_poussins_vivant, all_poussins_malade):
    soigner_all_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/soignerAll", headers=headers)
    assert soigner_all_poussins_response.status_code == 200, f"Failed to cure poussins: {soigner_all_poussins_response.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    for i in range(len(updated_poussins_response)):
        assert updated_poussins_response[i].get("malade") == None

def test_soigner_all_poussins_pauvre(headers, fermier_pauvre, add_poussins_vivant, all_poussins_affame, all_poussins_assoiffer, all_poussins_sale, all_poussins_malade):
    poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    nourrir_all_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/soignerAll", headers=headers)
    assert nourrir_all_poussins_response.status_code == 200, f"Failed to cure poussins: {nourrir_all_poussins_response.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    for i in range(len(updated_poussins_response)):
        assert updated_poussins_response[i].get("malade")[0:10] == poussins_response[0].get("malade")[0:10]
        assert updated_poussins_response[i].get("poids") == poussins_response[i].get("poids")

def test_soigner_all_poussins_seringue(headers, remise_pleine, add_poussins_vivant, all_poussins_malade):
    fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    soigner_seringue_all_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/soignerAllSeringue", headers=headers)
    assert soigner_seringue_all_poussins_response.status_code == 200, f"Failed to cure poussins: {soigner_seringue_all_poussins_response.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    updated_fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    for i in range(len(updated_poussins_response)):
        assert updated_poussins_response[i].get("sale") == None
    assert updated_fermiers_response.get("remise").get("seringue") == fermiers_response.get("remise").get("seringue") - 1

def test_soigner_all_poussins_sans_seringue(headers, fermier_riche, add_poussins_vivant, remise_vide, all_poussins_affame, all_poussins_assoiffer, all_poussins_sale, all_poussins_malade):
    fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    nourrir_all_coqs_response = requests.post(f"{APP_URL}/fermiers/poussins/soignerAllSeringue", headers=headers)
    assert nourrir_all_coqs_response.status_code == 200, f"Failed to cure poussins: {nourrir_all_coqs_response.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    updated_fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    for i in range(len(updated_poussins_response)):
        assert updated_poussins_response[i].get("malade")[0:10] == poussins_response[i].get("malade")[0:10]
    assert updated_fermiers_response.get("remise").get("seringue") == fermiers_response.get("remise").get("seringue")

def test_tuer_all_poussin(headers, add_poussins_vivant, all_poussins_malade4):
    poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    tuer_all_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/tuer", headers=headers)
    assert tuer_all_poussins_response.status_code == 200, f"Failed to killed poussins: {tuer_all_poussins_response.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    assert len(poussins_response) == 3
    assert len(updated_poussins_response) == 0

def test_poussins_grandir(headers, add_poussins_vivant, add3_poules_vivante, add_coqs_vivant, all_poussins_adultes):
    poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    adultes_response = len(coqs_response) + len(poules_response)

    adultes_poussins_response = requests.post(f"{APP_URL}/fermiers/poussins/grandir", headers=headers)
    assert adultes_poussins_response.status_code == 200, f"Failed to grandir poussins: {adultes_poussins_response.text}"

    poules_response = requests.get(f"{APP_URL}/fermiers/poules", headers=headers).json()
    coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    updated_adultes_response = len(coqs_response) + len(poules_response)
    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    assert len(updated_poussins_response) == 0
    assert updated_adultes_response == adultes_response + 3

def test_passage_jour(headers, fermier_riche, add_poussins_vivant, all_poussins_abreuver_hier, all_poussins_nourris_hier, all_poussins_nettoyer, all_poussins_soigner):
    poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    passage_jour_response = requests.post(f"{APP_URL}/fermiers/poussins/passageJour", headers=headers)
    assert passage_jour_response.status_code == 200, f"Failed to passage jour: {passage_jour_response.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    assert len(updated_poussins_response) == len(poussins_response)
    for i in range(len(updated_poussins_response)):
        assert updated_poussins_response[i].get("age") == poussins_response[i].get("age") + 1
        assert updated_poussins_response[i].get("poids") == poussins_response[i].get("poids")
        assert updated_poussins_response[i].get("nourris") == poussins_response[i].get("nourris")
        assert updated_poussins_response[i].get("abreuve") == poussins_response[i].get("abreuve")