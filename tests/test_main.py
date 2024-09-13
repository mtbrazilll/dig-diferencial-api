import pytest
from app.main import app

@pytest.fixture
def client():
    # Configura o Flask para testes
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    """Teste para verificar se a rota raiz retorna 'Hello, World!'"""
    response = client.get('/')
    assert response.data == b'Hello, World!'

def test_ia_service(client):
    """Teste para verificar o serviço de IA"""
    # Envia um JSON para o endpoint
    response = client.post('/api/ia_service', json={'input_text': 'hello'})
    json_data = response.get_json()

    # Verifica se o processamento está correto
    assert response.status_code == 200
    assert json_data['processed_text'] == 'HELLO'
