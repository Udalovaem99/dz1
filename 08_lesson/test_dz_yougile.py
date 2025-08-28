import requests
import pytest

BASE_URL = "https://yougile.com"
API_TOKEN = "PkaRm7GDExBzGBvDMD3ejas-jxdHn0VuslodXGhvnluiNnPfan5IawIGYNu8fYp6"

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

@pytest.fixture
def create_project():
    # Создаём проект для тестов обновления и получения
    payload = {
        "title": "Test Project"
    }
    response = requests.post(f"{BASE_URL}/api-v2/projects", headers=HEADERS, json=payload)
    assert response.status_code == 201
    response.json()


def test_create_new_pozitive_project():
    payload = {
        "title": "DZ1"
    }
    response = requests.post(f"{BASE_URL}/api-v2/projects", headers=HEADERS, json=payload)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data


def test_create_new_negative_project():
    payload = {
        "title": "DZ1"
    }
    response = requests.post(f"{BASE_URL}/api-v2/projects", headers=HEADERS, json=payload)
    assert response.status_code == 400
    data = response.json()
    assert "id" in data


def test_upd_pozitive_project():
    project_id = "84fb530e-10dd-4413-9ec3-7a93ee07a094"
    update_payload = {
        "title": "Updated DZ1"
    }
    response = requests.put(f"{BASE_URL}/api-v2/projects/{project_id}", headers=HEADERS, json=update_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == project_id
    

def test_upd_negative_project():
    project_id = "84fb530e-10dd-4413-9ec3-7a93ee07a094"
    update_payload = {
        "title": "Updated DZ1"
    }
    response = requests.put(f"{BASE_URL}/api-v2/projects/{project_id}", headers=HEADERS, json=update_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == update_payload["title"]
    

def test_get_pozitive_project():
    project_id = "84fb530e-10dd-4413-9ec3-7a93ee07a094"
    response = requests.get(f"{BASE_URL}/api-v2/projects/{project_id}", headers=HEADERS)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == project_id


def test_get_negative_project():
    project_id = "84fb530e-10dd-4413-9ec3-7a93ee07a094"
    response = requests.get(f"{BASE_URL}/api-v2/projects/{project_id}", headers=HEADERS)
    assert response.status_code == 404
    data = response.json()
    assert data["id"] == project_id
