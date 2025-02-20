import pytest

from app import app

username = "john"

@pytest.fixture
def client():
  app.config["TESTING"] = True
  with app.test_client() as client:
    yield client

def test_hello(client):
  response = client.get("/")
  assert response.status_code == 200
  assert b"Hello, World!!!" in response.data

def test_show_user_profile(client):
  response = client.get(f"/user/{username}")
  assert response.status_code == 200
  assert f"User {username}".encode() in response.data

# def test_template_example(client):
#   response = client.get(f"/template/{username}")
#   assert response.status_code == 200
#   assert f"User {username}".encode() in response.data
#   assert b"Item 1" in response.data
#   assert b"Item 2" in response.data
#   assert b"Item 3" in response.data

def test_form(client):
  response = client.get("/form")
  assert response.status_code == 200
  assert b"Name:" in response.data
  assert b"Email:" in response.data

def test_process_form(client):
  data = {"name": "Alice", "email": "alice@example.com"}
  response = client.post("/process_form", data=data)
  assert response.status_code == 200
  assert b"Submitted data: Name = Alice, Email = alice@example.com" in response.data
