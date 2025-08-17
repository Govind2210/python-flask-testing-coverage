import app

def test_home():
    response = app.app.test_client().get('/')
    assert response.status_code == 200
    assert b"Hello, World!" in response.data

def test_about():
    response = app.app.test_client().get('/about')
    assert response.status_code == 200
    assert b"about" in response.data

def test_contact():
    response = app.app.test_client().get('/contact')
    assert response.status_code == 200
    assert b"contact" in response.data
