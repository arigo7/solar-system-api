# get all books and return no records
def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

# get one planet by id
def test_get_planet_by_id(client, two_saved_planets):
    response = client.get('/planets/1')
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "One Planet",
        "description": "watr 4evr",
        "radius": 123.1
    }
    # assert response_body == {
    #     "id": "",
    #     "name": "",
    #     "description": "",
    #     "radius": None}

# get one planet by id
def test_create_one_planet(client, create_one_planet):
    response = client.post('/planets')
    response_body = response.get_json() # we might need to check into this compared
    # to the name 

    assert response.status_code == 201
    # assert response_body == {
    #     "description": "Another Fourth planet from the Sun and the second-smallest planet in the Solar System, being larger than only Mercury.",
    #     "name": "Another Mars",
    #     "radius": 2106.1
    # }
    
    # {
    # "message": f"Planet {request_body['name']} has been created",
    # "success": true}
# {
#             "success": True,
#             "message": f"Planet {request_body['name']} has been created"
#     }