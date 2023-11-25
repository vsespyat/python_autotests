import requests
import pytest

HOST = 'https://api.pokemonbattle.me:9104';
def test_status_code():
     response = requests.get(url=f'{HOST}/trainers', params={'trainer_id':3557} , timeout=5)
     assert response.status_code==200, 'Unexpected status code for /trainers'
     assert response.json()['trainer_name']=='Godzilla', 'Its not Godzilla!'



CASES = [
          (3557, 200),
          (39557, 400)
     ]    

@pytest.mark.parametrize('id, code', CASES)
def test_parametrize(id, code):
        response = requests.get(url=f'{HOST}/trainers', params={'trainer_id':3557} , timeout=5)
        assert response.status_code==200, 'Unexpected status code for /trainers'     