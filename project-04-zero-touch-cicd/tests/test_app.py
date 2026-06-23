from app.app import app


def test_home_page():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Project 04 Zero-Touch CI/CD" in response.data


def test_version_text():
    client = app.test_client()
    response = client.get("/")

    assert b"Version 1" in response.data
