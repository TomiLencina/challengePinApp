import requests


# URL base de la API de Rick and Morty
BASE_URL = "https://rickandmortyapi.com/api"


# Función para obtener la lista de personajes
def get_lista_personajes(page=1):
    response = requests.get(f"{BASE_URL}/character", params={'page': page})
    return response


# Función para obtener los detalles de un personaje
def get_personaje(id):
    response = requests.get(f"{BASE_URL}/character/{id}")
    return response


# Función para obtener la lista de episodios
def get_lista_episodios(page=1):
    response = requests.get(f"{BASE_URL}/episode", params={'page': page})
    return response


# Función para obtener los detalles de un episodio
def get_episodio(id):
    response = requests.get(f"{BASE_URL}/episode/{id}")
    return response


# Test 1: Obtener la lista de personajes de la API
def test_get_lista_personajes():
    response = get_lista_personajes()

    # Verificar que el código de estado es 200 (OK)
    assert response.status_code == 200

    # Verificar que la respuesta contenga una lista de personajes
    data = response.json()
    assert 'results' in data  # Asegurarse de que el campo "results" esté presente
    assert isinstance(data['results'], list)  # Verificar que "results" sea una lista
    assert len(data['results']) > 0  # Verificar que haya al menos un personaje


# Test 2: Obtener los detalles de un personaje específico
def test_get_detalle_personaje():
    id_personaje = 1  # Usamos el ID del primer personaje (Rick Sanchez)
    response = get_personaje(id_personaje)

    # Verificar que el código de estado es 200 (OK)
    assert response.status_code == 200

    # Verificar que los datos del personaje estén presentes en la respuesta
    data = response.json()
    assert 'id' in data  # Verificar que el campo "id" esté presente
    assert data['id'] == id_personaje  # Verificar que el ID del personaje sea el correcto
    assert 'name' in data  # Verificar que el campo "name" esté presente
    assert 'species' in data  # Verificar que el campo "species" esté presente


# Test 3: Obtener la lista de episodios
def test_get_lista_episodios():
    response = get_lista_episodios()

    # Verificar que el código de estado es 200 (OK)
    assert response.status_code == 200

    # Verificar que la respuesta contenga una lista de episodios
    data = response.json()
    assert 'results' in data  # Asegurarse de que el campo "results" esté presente
    assert isinstance(data['results'], list)  # Verificar que "results" sea una lista
    assert len(data['results']) > 0  # Verificar que haya al menos un episodio


# Test 4: Obtener los detalles de un episodio específico
def test_get_detalle_episodio():
    id_episodio = 1  # Usamos el ID del primer episodio
    response = get_episodio(id_episodio)

    # Verificar que el código de estado es 200 (OK)
    assert response.status_code == 200

    # Verificar que los datos del episodio estén presentes en la respuesta
    data = response.json()
    assert 'id' in data  # Verificar que el campo "id" esté presente
    assert data['id'] == id_episodio  # Verificar que el ID del episodio sea el correcto
    assert 'name' in data  # Verificar que el campo "name" esté presente
    assert 'air_date' in data  # Verificar que el campo "air_date" esté presente


# Test 5: Verificar error al obtener detalles de un personaje inexistente
def test_get_personaje_inexistente():
    id_personaje_inexistente = 999999  # Usamos un ID que no existe
    response = get_personaje(id_personaje_inexistente)

    # Verificar que el código de estado sea 404 (Not Found)
    assert response.status_code == 404

    # Verificar que la respuesta contenga el mensaje de error
    data = response.json()
    assert 'error' in data  # Verificar que el campo "error" esté presente
    assert data['error'] == "Character not found"  # Verificar que el mensaje sea el esperado


# Test 6: Verificar error al obtener detalles de un episodio inexistente
def test_get_episodio_inexistente():
    id_episodio_inexistente = 999999  # Usamos un ID que no existe
    response = get_episodio(id_episodio_inexistente)

    # Verificar que el código de estado sea 404 (Not Found)
    assert response.status_code == 404

    # Verificar que la respuesta contenga el mensaje de error
    data = response.json()
    assert 'error' in data  # Verificar que el campo "error" esté presente
    assert data['error'] == "Episode not found"  # Verificar que el mensaje sea el esperado


# Test 7: Verificar que un personaje está asociado correctamente a los episodios
def test_integracion_personaje_y_episodios():
    id_personaje = 1  # Usamos el ID de Rick Sanchez

    # Obtener los detalles del personaje
    response_personaje = get_personaje(id_personaje)
    assert response_personaje.status_code == 200
    data_personaje = response_personaje.json()

    # Verificar que el personaje tiene una lista de episodios
    assert 'episode' in data_personaje  # Asegurarse de que el campo 'episode' esté presente
    assert isinstance(data_personaje['episode'], list)  # Verificar que 'episode' sea una lista

    # Verificar que la lista de episodios no esté vacía
    assert len(data_personaje['episode']) > 0

    # Tomamos el ID del primer episodio al que el personaje está asociado
    id_episodio = data_personaje['episode'][0].split('/')[-1]  # Extraemos el ID del episodio

    # Obtener los detalles del episodio
    response_episodio = get_episodio(id_episodio)
    assert response_episodio.status_code == 200
    data_episodio = response_episodio.json()

    # Verificar que el episodio tenga un campo 'characters' que incluye el personaje
    assert 'characters' in data_episodio  # Asegurarse de que el campo 'characters' esté presente
    assert id_personaje in [int(character.split('/')[-1]) for character in data_episodio['characters']]

    # Si pasamos todas las verificaciones, significa que el personaje está correctamente asociado a los episodios
    print(f"El personaje con ID {id_personaje} está correctamente asociado a los episodios.")




#test_get_lista_personajes
#test_get_detalle_personaje
#test_get_lista_episodios
#test_get_detalle_episodio
#test_get_personaje_inexistente
#test_get_episodio_inexistente()