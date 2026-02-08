import requests
import pytest
import datetime

# Base URL for the Spring Boot application
APP_URL = "http://localhost:8080"

from test_secu import auth_token, headers, fermier_pauvre, fermier_riche, remise_pleine, remise_vide

@pytest.fixture
def all_coqs_nourris(headers):
    nourrir_all_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/nourrirAll", headers=headers)
    assert nourrir_all_coqs_response.status_code == 200, f"Failed to fed coqs: {nourrir_all_coqs_response.text}"

@pytest.fixture
def all_coqs_nourris_hier(headers):
    nourrir_all_coqs_hier_response = requests.post(f"{APP_URL}/fermiers/coqs/nourrirHier", headers=headers)
    assert nourrir_all_coqs_hier_response.status_code == 200, f"Failed to fed coqs: {nourrir_all_coqs_hier_response.text}"

@pytest.fixture
def all_coqs_affame(headers):
    affamer_all_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/affamer", headers=headers)
    assert affamer_all_coqs_response.status_code == 200, f"Failed to fed coqs: {affamer_all_coqs_response.text}"

@pytest.fixture
def all_coqs_affame2(headers):
    affamer2_all_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/affamer2", headers=headers)
    assert affamer2_all_coqs_response.status_code == 200, f"Failed to fed coqs: {affamer2_all_coqs_response.text}"

@pytest.fixture
def all_coqs_affame3(headers):
    affamer3_all_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/affamer3", headers=headers)
    assert affamer3_all_coqs_response.status_code == 200, f"Failed to fed coqs: {affamer3_all_coqs_response.text}"

@pytest.fixture
def all_coqs_affame4(headers):
    affamer4_all_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/affamer4", headers=headers)
    assert affamer4_all_coqs_response.status_code == 200, f"Failed to fed coqs: {affamer4_all_coqs_response.text}"

@pytest.fixture
def all_coqs_assoiffer(headers):
    assoiffer_all_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/assoiffer", headers=headers)
    assert assoiffer_all_coqs_response.status_code == 200, f"Failed to fed coqs: {assoiffer_all_coqs_response.text}"

@pytest.fixture
def all_coqs_abreuver(headers):
    abreuver_all_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/abreuveAll", headers=headers)
    assert abreuver_all_coqs_response.status_code == 200, f"Failed to fed coqs: {abreuver_all_coqs_response.text}"

@pytest.fixture
def all_coqs_abreuver_hier(headers):
    abreuver_all_coqs_hier_response = requests.post(f"{APP_URL}/fermiers/coqs/abreuveHier", headers=headers)
    assert abreuver_all_coqs_hier_response.status_code == 200, f"Failed to fed coqs: {abreuver_all_coqs_hier_response.text}"

@pytest.fixture
def all_coqs_sale(headers):
    sale_all_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/salir", headers=headers)
    assert sale_all_coqs_response.status_code == 200, f"Failed to fed coqs: {sale_all_coqs_response.text}"

@pytest.fixture
def all_coqs_nettoyer(headers):
    nettoyer_all_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/nettoyerAll", headers=headers)
    assert nettoyer_all_coqs_response.status_code == 200, f"Failed to fed coqs: {nettoyer_all_coqs_response.text}"

@pytest.fixture
def all_coqs_malade(headers):
    malade_all_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/malade", headers=headers)
    assert malade_all_coqs_response.status_code == 200, f"Failed to fed coqs: {malade_all_coqs_response.text}"

@pytest.fixture
def all_coqs_malade4(headers):
    malade_all_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/malade4", headers=headers)
    assert malade_all_coqs_response.status_code == 200, f"Failed to fed coqs: {malade_all_coqs_response.text}"

@pytest.fixture
def all_coqs_soigner(headers):
    soigner_all_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/soignerAll", headers=headers)
    assert soigner_all_coqs_response.status_code == 200, f"Failed to fed coqs: {soigner_all_coqs_response.text}"

@pytest.fixture
def add_coqs_vivant(headers):
    add_coqs_vivant_response = requests.post(f"{APP_URL}/fermiers/add1Coq", headers=headers)
    assert add_coqs_vivant_response.status_code == 200, f"Failed to revive coqs: {add_coqs_vivant_response.text}"

@pytest.fixture
def all_coqs_maigrir(headers):
    all_coqs_maigrir_response = requests.post(f"{APP_URL}/fermiers/coqs/maigrir", headers=headers)
    assert all_coqs_maigrir_response.status_code == 200, f"Failed to revive coqs: {all_coqs_maigrir_response.text}"

@pytest.fixture
def all_coqs_enfant(headers):
    all_coqs_enfant_response = requests.post(f"{APP_URL}/fermiers/coqs/enfant", headers=headers)
    assert all_coqs_enfant_response.status_code == 200, f"Failed to revive coqs: {all_coqs_enfant_response.text}"

def test_coq(headers, add_coqs_vivant):
    coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers)
    assert coqs_response.status_code == 200, f"Failed to get coqs: {coqs_response.text}"

    coqs_data =coqs_response.json()
    now = datetime.datetime.now().date()
    assert len(coqs_data) == 1
    for i in range(len(coqs_data)):
        assert coqs_data[i].get("poids") == 2.5
        assert coqs_data[i].get("age") == 5
        assert coqs_data[i].get("abreuve")[0:10] != now.strftime('%Y-%m-%d')
        assert coqs_data[i].get("nourris")[0:10] != now.strftime('%Y-%m-%d')
        assert coqs_data[i].get("sale") == None
        assert coqs_data[i].get("malade") == None

def test_nourrir_coq(headers, fermier_riche, add_coqs_vivant, all_coqs_affame, all_coqs_assoiffer):
    coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    nourrir_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/nourrir/{coqs_response[0].get("id")}", headers=headers)
    assert nourrir_coqs_response.status_code == 200, f"Failed to fed coq: {nourrir_coqs_response.text}"

    updated_coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    now = datetime.datetime.now().date()
    assert updated_coqs_response[0].get("nourris")[0:10] == now.strftime('%Y-%m-%d')
    assert updated_coqs_response[0].get("poids") == coqs_response[0].get("poids") + 0.5

def test_nourrir_coq_pauvre(headers, fermier_pauvre, add_coqs_vivant, all_coqs_affame, all_coqs_assoiffer):
    coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    fermier_data = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    nourrir_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/nourrir/{coqs_response[0].get("id")}", headers=headers)
    assert nourrir_coqs_response.status_code == 200, f"Failed to fed coq: {nourrir_coqs_response.text}"

    updated_coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    assert updated_coqs_response[0].get("nourris")[0:10] == coqs_response[0].get("nourris")[0:10]

def test_nourrir_all_coqs(headers, fermier_riche, add_coqs_vivant, all_coqs_affame, all_coqs_assoiffer):
    nourrir_all_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/nourrirAll", headers=headers)
    assert nourrir_all_coqs_response.status_code == 200, f"Failed to fed coqs: {nourrir_all_coqs_response.text}"

    updated_coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    now = datetime.datetime.now().date()
    for i in range(len(updated_coqs_response)):
        assert updated_coqs_response[i].get("nourris")[0:10] == now.strftime('%Y-%m-%d')

def test_nourrir_all_coqs_pauvre(headers, fermier_pauvre, add_coqs_vivant, all_coqs_affame, all_coqs_assoiffer):
    coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    nourrir_all_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/nourrirAll", headers=headers)
    assert nourrir_all_coqs_response.status_code == 200, f"Failed to fed coqs: {nourrir_all_coqs_response.text}"

    updated_coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    for i in range(len(updated_coqs_response)):
        assert updated_coqs_response[i].get("nourris")[0:10] == coqs_response[i].get("nourris")[0:10]
        assert updated_coqs_response[i].get("poids") == coqs_response[i].get("poids")

def test_nourrir_all_coqs_sac_nourriture(headers, remise_pleine, add_coqs_vivant, all_coqs_affame, all_coqs_assoiffer):
    fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    nourrir_all_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/nourrirAllSacNourriture", headers=headers)
    assert nourrir_all_coqs_response.status_code == 200, f"Failed to fed coqs: {nourrir_all_coqs_response.text}"

    updated_coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    updated_fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    now = datetime.datetime.now().date()
    for i in range(len(updated_coqs_response)):
        assert updated_coqs_response[i].get("nourris")[0:10] == now.strftime('%Y-%m-%d')
        assert updated_coqs_response[i].get("poids") == coqs_response[i].get("poids") + 0.5
    assert updated_fermiers_response.get("remise").get("sac_nourriture") == fermiers_response.get("remise").get("sac_nourriture") - 1

def test_nourrir_all_coqs_sans_sac_nourriture(headers, fermier_riche, add_coqs_vivant, remise_vide, all_coqs_affame, all_coqs_assoiffer):
    fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    nourrir_all_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/nourrirAllSacNourriture", headers=headers)
    assert nourrir_all_coqs_response.status_code == 200, f"Failed to fed coqs: {nourrir_all_coqs_response.text}"

    updated_coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    updated_fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    for i in range(len(updated_coqs_response)):
        assert updated_coqs_response[i].get("nourris")[0:10] == coqs_response[i].get("nourris")[0:10]
    assert updated_fermiers_response.get("remise").get("sac_nourriture") == fermiers_response.get("remise").get("sac_nourriture")

def test_abreuve_coq(headers, fermier_riche, add_coqs_vivant, all_coqs_assoiffer, all_coqs_nourris):
    coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    abreuve_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/abreuve/{coqs_response[0].get("id")}", headers=headers)
    assert abreuve_coqs_response.status_code == 200, f"Failed to watered coq: {abreuve_coqs_response.text}"

    updated_coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    now = datetime.datetime.now().date()
    assert updated_coqs_response[0].get("abreuve")[0:10] == now.strftime('%Y-%m-%d')
    assert updated_coqs_response[0].get("poids") == coqs_response[0].get("poids") + 0.15

def test_abreuve_coq_pauvre(headers, fermier_pauvre, add_coqs_vivant, all_coqs_assoiffer, all_coqs_nourris):
    coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    abreuve_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/abreuve/{1}", headers=headers)
    assert abreuve_coqs_response.status_code == 200, f"Failed to watered coq: {abreuve_coqs_response.text}"

    updated_coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    assert updated_coqs_response[0].get("abreuve")[0:10] == coqs_response[0].get("abreuve")[0:10]

def test_abreuve_all_coqs(headers, fermier_riche, add_coqs_vivant, all_coqs_assoiffer, all_coqs_nourris):
    abreuve_all_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/abreuveAll", headers=headers)
    assert abreuve_all_coqs_response.status_code == 200, f"Failed to watered coqs: {abreuve_all_coqs_response.text}"

    updated_coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    now = datetime.datetime.now().date()
    for i in range(len(updated_coqs_response)):
        assert updated_coqs_response[i].get("abreuve")[0:10] == now.strftime('%Y-%m-%d')

def test_abreuve_all_coqs_pauvre(headers, fermier_pauvre, add_coqs_vivant, all_coqs_affame, all_coqs_assoiffer):
    coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    nourrir_all_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/abreuveAll", headers=headers)
    assert nourrir_all_coqs_response.status_code == 200, f"Failed to watered coqs: {nourrir_all_coqs_response.text}"

    coqs_updated_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    for i in range(len(coqs_updated_response)):
        assert coqs_updated_response[i].get("abreuve")[0:10] == coqs_response[i].get("abreuve")[0:10]
        assert coqs_updated_response[i].get("poids") == coqs_response[i].get("poids")

def test_abreuve_all_coqs_eau(headers, remise_pleine, add_coqs_vivant, all_coqs_assoiffer):
    fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    abreuve_all_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/abreuveAllSeauDeau", headers=headers)
    assert abreuve_all_coqs_response.status_code == 200, f"Failed to watered coqs: {abreuve_all_coqs_response.text}"

    updated_coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    updated_fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    now = datetime.datetime.now().date()
    for i in range(len(updated_coqs_response)):
        assert updated_coqs_response[i].get("abreuve")[0:10] == now.strftime('%Y-%m-%d')
    assert updated_fermiers_response.get("remise").get("eau") == fermiers_response.get("remise").get("eau") - 1

def test_abreuve_all_coqs_sans_eau(headers, fermier_riche, add_coqs_vivant, remise_vide, all_coqs_affame, all_coqs_assoiffer):
    coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    nourrir_all_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/abreuveAllSeauDeau", headers=headers)
    assert nourrir_all_coqs_response.status_code == 200, f"Failed to watered coqs: {nourrir_all_coqs_response.text}"

    updated_coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    updated_fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    for i in range(len(updated_coqs_response)):
        assert updated_coqs_response[i].get("abreuve")[0:10] == coqs_response[i].get("abreuve")[0:10]
    assert updated_fermiers_response.get("remise").get("eau") == fermiers_response.get("remise").get("eau")

def test_famine_all_coqs(headers, add_coqs_vivant, all_coqs_affame):
    coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    famine_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/famine", headers=headers)
    assert famine_coqs_response.status_code == 200, f"Failed to famine coqs: {famine_coqs_response.text}"

    updated_coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    assert len(updated_coqs_response) == 1
    for i in range(len(updated_coqs_response)):
        assert round(updated_coqs_response[i].get("poids"), 4) == round((coqs_response[i].get("poids") - 0.2), 4)

def test_famine2_all_coqs(headers, add_coqs_vivant, all_coqs_affame2):
    coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    famine2_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/famine", headers=headers)
    assert famine2_coqs_response.status_code == 200, f"Failed to famine coqs: {famine2_coqs_response.text}"

    updated_coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    assert len(updated_coqs_response) == 1
    for i in range(len(updated_coqs_response)):
        assert round(updated_coqs_response[i].get("poids"), 4) == round((coqs_response[i].get("poids") - 0.5), 4)

def test_famine3_all_coqs(headers, add_coqs_vivant, all_coqs_affame3):
    coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    famine3_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/famine", headers=headers)
    assert famine3_coqs_response.status_code == 200, f"Failed to famine coqs: {famine3_coqs_response.text}"

    updated_coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    assert len(updated_coqs_response) == 1
    for i in range(len(updated_coqs_response)):
        assert round(updated_coqs_response[i].get("poids"), 4) == round((coqs_response[i].get("poids") - 1.0), 4)

def test_famine4_all_coqs(headers, add_coqs_vivant, all_coqs_affame4):
    coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    famine4_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/famine", headers=headers)
    assert famine4_coqs_response.status_code == 200, f"Failed to famine coqs: {famine4_coqs_response.text}"

    updated_coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    assert len(updated_coqs_response) == 0

def test_nettoyer_coq(headers, fermier_riche, add_coqs_vivant, all_coqs_affame, all_coqs_assoiffer, all_coqs_sale):
    coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    nettoyer_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/nettoyer/{coqs_response[0].get("id")}", headers=headers)
    assert nettoyer_coqs_response.status_code == 200, f"Failed to cleaned coq: {nettoyer_coqs_response.text}"

    updated_coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    assert updated_coqs_response[0].get("sale") == None

def test_nettoyer_coq_pauvre(headers, fermier_pauvre, add_coqs_vivant, all_coqs_affame, all_coqs_assoiffer, all_coqs_sale):
    coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    nourrir_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/nettoyer/{coqs_response[0].get("id")}", headers=headers)
    assert nourrir_coqs_response.status_code == 200, f"Failed to cleaned coq: {nourrir_coqs_response.text}"

    updated_coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    assert updated_coqs_response[0].get("sale")[0:10] == coqs_response[0].get("sale")[0:10]

def test_nettoyer_all_coqs(headers, fermier_riche, add_coqs_vivant, all_coqs_sale):
    nettoyer_all_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/nettoyerAll", headers=headers)
    assert nettoyer_all_coqs_response.status_code == 200, f"Failed to cleaned coqs: {nettoyer_all_coqs_response.text}"

    updated_coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    for i in range(len(updated_coqs_response)):
        assert updated_coqs_response[i].get("sale") == None

def test_nettoyer_all_coqs_pauvre(headers, fermier_pauvre, add_coqs_vivant, all_coqs_affame, all_coqs_assoiffer, all_coqs_sale):
    coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    nourrir_all_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/nettoyerAll", headers=headers)
    assert nourrir_all_coqs_response.status_code == 200, f"Failed to cleaned coqs: {nourrir_all_coqs_response.text}"

    updated_coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    for i in range(len(updated_coqs_response)):
        assert updated_coqs_response[i].get("sale")[0:10] == coqs_response[i].get("sale")[0:10]

def test_nettoyer_all_coqs_savon(headers, remise_pleine, add_coqs_vivant, all_coqs_sale):
    fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    abreuve_all_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/nettoyerAllSavon", headers=headers)
    assert abreuve_all_coqs_response.status_code == 200, f"Failed to cleaned coqs: {abreuve_all_coqs_response.text}"

    updated_coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    updated_fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    for i in range(len(updated_coqs_response)):
        assert updated_coqs_response[i].get("sale") == None
    assert updated_fermiers_response.get("remise").get("savon") == fermiers_response.get("remise").get("savon") - 1

def test_nettoyer_all_coqs_sans_savon(headers, fermier_riche, add_coqs_vivant, remise_vide, all_coqs_affame, all_coqs_assoiffer, all_coqs_sale):
    fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    nourrir_all_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/nettoyerAllSavon", headers=headers)
    assert nourrir_all_coqs_response.status_code == 200, f"Failed to cleaned coqs: {nourrir_all_coqs_response.text}"

    updated_coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    updated_fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    for i in range(len(updated_coqs_response)):
        assert updated_coqs_response[i].get("sale")[0:10] == coqs_response[i].get("sale")[0:10]
    assert updated_fermiers_response.get("remise").get("savon") == fermiers_response.get("remise").get("savon")

def test_soigner_coq(headers, fermier_riche, add_coqs_vivant, all_coqs_affame, all_coqs_assoiffer, all_coqs_sale, all_coqs_malade):
    coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    nourrir_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/soigner/{coqs_response[0].get("id")}", headers=headers)
    assert nourrir_coqs_response.status_code == 200, f"Failed to cure coq: {nourrir_coqs_response.text}"

    updated_coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    assert updated_coqs_response[0].get("malade") == None

def test_soigner_coq_pauvre(headers, fermier_pauvre, add_coqs_vivant, all_coqs_affame, all_coqs_assoiffer, all_coqs_sale, all_coqs_malade):
    coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    nourrir_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/soigner/{coqs_response[0].get("id")}", headers=headers)
    assert nourrir_coqs_response.status_code == 200, f"Failed to cure coq: {nourrir_coqs_response.text}"

    updated_coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    assert updated_coqs_response[0].get("malade")[0:10] == coqs_response[0].get("sale")[0:10]

def test_soigner_all_coqs(headers, fermier_riche, add_coqs_vivant, all_coqs_malade):
    soigner_all_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/soignerAll", headers=headers)
    assert soigner_all_coqs_response.status_code == 200, f"Failed to cure coqs: {soigner_all_coqs_response.text}"

    updated_coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    for i in range(len(updated_coqs_response)):
        assert updated_coqs_response[i].get("malade") == None

def test_soigner_all_coqs_pauvre(headers, fermier_pauvre, add_coqs_vivant, all_coqs_affame, all_coqs_assoiffer, all_coqs_sale, all_coqs_malade):
    coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    nourrir_all_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/soignerAll", headers=headers)
    assert nourrir_all_coqs_response.status_code == 200, f"Failed to cure coqs: {nourrir_all_coqs_response.text}"

    updated_coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    now = datetime.datetime.now().date()
    for i in range(len(updated_coqs_response)):
        assert updated_coqs_response[i].get("malade")[0:10] == coqs_response[i].get("malade")[0:10]

def test_soigner_all_coqs_seringue(headers, remise_pleine, add_coqs_vivant, all_coqs_malade):
    fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    soigner_seringue_all_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/soignerAllSeringue", headers=headers)
    assert soigner_seringue_all_coqs_response.status_code == 200, f"Failed to cure coqs: {soigner_seringue_all_coqs_response.text}"

    updated_coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    updated_fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    now = datetime.datetime.now().date()
    for i in range(len(updated_coqs_response)):
        assert updated_coqs_response[i].get("sale") == None
    assert updated_fermiers_response.get("remise").get("seringue") == fermiers_response.get("remise").get("seringue") - 1

def test_soigner_all_coqs_sans_seringue(headers, fermier_riche, add_coqs_vivant, remise_vide, all_coqs_affame, all_coqs_assoiffer, all_coqs_sale, all_coqs_malade):
    fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    nourrir_all_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/soignerAllSeringue", headers=headers)
    assert nourrir_all_coqs_response.status_code == 200, f"Failed to cure coqs: {nourrir_all_coqs_response.text}"

    updated_coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    updated_fermiers_response = requests.get(f"{APP_URL}/fermiers", headers=headers).json()
    for i in range(len(updated_coqs_response)):
        assert updated_coqs_response[i].get("malade")[0:10] == coqs_response[i].get("malade")[0:10]
    assert updated_fermiers_response.get("remise").get("seringue") == fermiers_response.get("remise").get("seringue")

def test_tuer_all_coq(headers, add_coqs_vivant, all_coqs_malade4):
    coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    tuer_all_coqs_response = requests.post(f"{APP_URL}/fermiers/coqs/tuer", headers=headers)
    assert tuer_all_coqs_response.status_code == 200, f"Failed to kill coqs: {tuer_all_coqs_response.text}"

    coqs_updated_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    assert len(coqs_response) == 1
    assert len(coqs_updated_response) == 0

def test_enfant_all_coq(headers, add_coqs_vivant, all_coqs_enfant):
    poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    regression_all_coqs = requests.post(f"{APP_URL}/fermiers/coqs/regression", headers=headers)
    assert regression_all_coqs.status_code == 200, f"Failed to regression coqs: {regression_all_coqs.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    updated_coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    assert len(updated_coqs_response) == len(coqs_response) - 1
    assert len(updated_poussins_response) == len(poussins_response) + 1

def test_enfant_all_coqs_adultes(headers, add_coqs_vivant):
    poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    regression_all_coqs = requests.post(f"{APP_URL}/fermiers/coqs/regression", headers=headers)
    assert regression_all_coqs.status_code == 200, f"Failed to regression coqs: {regression_all_coqs.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    updated_coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    assert len(updated_coqs_response) == len(coqs_response)
    assert len(updated_poussins_response) == len(poussins_response)

def test_passage_jour(headers, fermier_riche, add_coqs_vivant, all_coqs_abreuver_hier, all_coqs_nourris_hier, all_coqs_nettoyer, all_coqs_soigner):
    poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    
    print(coqs_response)
    passage_jour_response = requests.post(f"{APP_URL}/fermiers/coqs/passageJour", headers=headers)
    assert passage_jour_response.status_code == 200, f"Failed to passage jour: {passage_jour_response.text}"

    updated_poussins_response = requests.get(f"{APP_URL}/fermiers/poussins", headers=headers).json()
    updated_coqs_response = requests.get(f"{APP_URL}/fermiers/coqs", headers=headers).json()
    assert len(poussins_response) == len(updated_poussins_response)
    assert len(coqs_response) == len(updated_coqs_response)
    for i in range(len(updated_coqs_response)):
        assert updated_coqs_response[i].get("poids") == coqs_response[i].get("poids")
        assert updated_coqs_response[i].get("age") == coqs_response[i].get("age") + 1
        assert updated_coqs_response[i].get("nourris") == coqs_response[i].get("nourris")
        assert updated_coqs_response[i].get("abreuve") == coqs_response[i].get("abreuve")
