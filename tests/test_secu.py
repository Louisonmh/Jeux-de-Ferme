import requests
import pytest
import datetime

# Base URL for the Spring Boot application
APP_URL = "http://localhost:8080"

@pytest.fixture(scope="module")
def auth_token():
    """Retrieve an authentication token for testing."""
    response = requests.get(f"{APP_URL}/auth/test-token/fermier1")
    assert response.status_code == 200, f"Failed to retrieve token: {response.text}"
    
    token = response.text
    assert token is not None, "Token is missing in the response"
    
    return token

@pytest.fixture(scope="module")
def auth_token2():
    """Retrieve an authentication token for testing."""
    response = requests.get(f"{APP_URL}/auth/test-token/fermier2")
    assert response.status_code == 200, f"Failed to retrieve token: {response.text}"
    
    token = response.text
    assert token is not None, "Token is missing in the response"
    
    return token

@pytest.fixture
def headers(auth_token):
    """Generate headers with the authentication token."""
    return {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }

@pytest.fixture
def headers2(auth_token2):
    """Generate headers with the authentication token."""
    return {
        "Authorization": f"Bearer {auth_token2}",
        "Content-Type": "application/json"
    }

@pytest.fixture
def fermier_pauvre(headers):
        # Removes ecus from user
        ecus_response = requests.post(f"{APP_URL}/fermiers/zeroEcus", headers=headers)
        assert ecus_response.status_code == 200, f"Failed to remove ecus: {ecus_response.text}"

@pytest.fixture
def fermier_riche(headers):
        # Makes sure user has money
        ecus_response = requests.post(f"{APP_URL}/fermiers/addEcus/{500}", headers=headers)
        assert ecus_response.status_code == 200, f"Failed to add ecus: {ecus_response.text}"

@pytest.fixture
def remise_vide(headers):
        # Removes straw bale from user
        botte_response = requests.post(f"{APP_URL}/fermiers/remise/vider", headers=headers)
        assert botte_response.status_code == 200, f"Failed to remove straw bales: {botte_response.text}"

@pytest.fixture
def remise_pleine(headers):
        # Makes sure user has straw bales
        botte_response = requests.post(f"{APP_URL}/fermiers/remise/remplirUn", headers=headers)
        assert botte_response.status_code == 200, f"Failed to add straw bale: {botte_response.text}"

@pytest.fixture
def remise_plusieurs(headers):
    # Makes suer user has full bales
    botte_response = requests.post(f"{APP_URL}/fermiers/remise/remplirPlusieurs", headers=headers)
    assert botte_response.status_code == 200, f"Failed to add straw bale: {botte_response.text}"

@pytest.fixture
def get_fermier(headers):
      
      #créer ma ferme et test si ça à executer 
      response = requests.get(f"{APP_URL}/fermiers", headers=headers)
      assert response.status_code == 200, f"Erreur de création du fermier:{response.text}"

      #récupère ma ferme et test si c'est bon
      fermier_data = response.json()
      expected_keys = {"nomUtilisateur", "vache", "ecus"}
      assert expected_keys.issubset(fermier_data.keys()), f"Missing keys in response: {fermier_data.keys()}"

      return fermier_data


@pytest.fixture
def get_fermier2(headers2):
      
      #créer ma ferme et test si ça à executer 
      response = requests.get(f"{APP_URL}/fermiers", headers=headers2)
      assert response.status_code == 200, f"Erreur de création du fermier:{response.text}"

      #récupère ma ferme et test si c'est bon
      fermier_data = response.json()
      expected_keys = {"nomUtilisateur", "vache", "ecus"}
      assert expected_keys.issubset(fermier_data.keys()), f"Missing keys in response: {fermier_data.keys()}"

      return fermier_data


def test_fermes_differents(headers, headers2):
    
    # Créer ferme pour utilisateur 1
    response1 = requests.get(f"{APP_URL}/fermiers", headers=headers)
    assert response1.status_code == 200
    fermier1 = response1.json()

    # Créer ferme pour utilisateur 2
    response2 = requests.get(f"{APP_URL}/fermiers", headers=headers2)
    assert response2.status_code == 200
    fermier2 = response2.json()

    assert fermier1["nomUtilisateur"] != fermier2["nomUtilisateur"], "Erreur: les fermiers sont les même"

def test_create_or_get_farm(headers):
    """Test fetching or creating a farm for the authenticated user."""
    response = requests.get(f"{APP_URL}/fermiers", headers=headers)
    assert response.status_code == 200, f"Failed to fetch/create farm: {response.text}"

    farm_data = response.json()
    expected_keys = {"nomUtilisateur", "vache", "ecus"}

    # Ensure the farm response contains the required fields
    assert expected_keys.issubset(farm_data.keys()), f"Missing keys in response: {farm_data.keys()}"

    print("✅ Test passed: Farm was successfully retrieved or created.")

"""
def test_feed_cow(headers):
        # Feed the cow
        feed_response = requests.post(f"{APP_URL}/farm/cow/feed", headers=headers)
        assert feed_response.status_code == 200, f"Failed to feed the cow: {feed_response.text}"

        # Verify the cow is no longer hungry
        updated_farm_data = requests.get(f"{APP_URL}/farm", headers=headers).json()
        assert updated_farm_data["cow"].get("hungry") == False, "Cow is still hungry after feeding"

def test_hungry_cow(headers):
        # Feed the cow
        feed_response = requests.post(f"{APP_URL}/farm/cow/hungry", headers=headers)
        assert feed_response.status_code == 200, f"Failed to hungry the cow: {feed_response.text}"

        # Verify the cow is no longer hungry
        updated_farm_data = requests.get(f"{APP_URL}/farm", headers=headers).json()
        assert updated_farm_data["cow"].get("hungry") == True, "Cow is still feed after hungrying"


def test_chicken(headers):
        # Feed the cow
        feed_response = requests.get(f"{APP_URL}/farm/chicken", headers=headers)
        assert feed_response.status_code == 200, f"Failed to get chickens: {feed_response.text}"

        chicken_data =feed_response.json()

        # Verify the cow is no longer hungry
        assert len(chicken_data)==5
"""
