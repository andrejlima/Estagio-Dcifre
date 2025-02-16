from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_empresa():
    response = client.post("/empresas/", json={
        "nome": "Empresa Teste",
        "cnpj": "12645678901234",
        "endereco": "Rua X",
        "email": "empresa@teste.com",
        "telefone": "11999999999"
    })
    assert response.status_code == 200
    assert response.json()["nome"] == "Empresa Teste"

def test_create_obrigacao():
    response = client.post("/obrigacoes/", json={
        "nome": "DCTF",
        "periodicidade": "mensal",
        "empresa_id": 1
    })
    assert response.status_code == 200
    assert response.json()["nome"] == "DCTF"