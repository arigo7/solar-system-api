from app import db
from flask import Blueprint
from .models.planet import Planet
from flask import request
from flask import jsonify 


# creating instance of the class, first arg is name of app's module
planet_bp = Blueprint("planets", __name__, url_prefix="/planets")

#create a planet
@planet_bp.route("", methods = ["POST"], strict_slashes = False)
def handle_planet_data():
    request_body = request.get_json()
    new_planet = Planet(name=request_body["name"],
                    description=request_body["description"],
                    radius = request_body["radius"]) 
    db.session.add(new_planet) # "adds model to the db"
    db.session.commit() # does the action above
    # return (f"Book #{new_book.title} has been created", 201)

    return {"success": True,
            "message": f"Planet {new_planet.name} has been created"
            }, 201

#Retrive all planet  

@planet_bp.route("", methods = ["GET"], strict_slashes = False)
def retrieve_planets_data():
    #request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "radius": planet.radius,
            })
        return jsonify(planets_response), 200  # returning the list of all planets

#Retrieve one planet

@planet_bp.route("/<planet_id>", methods=["GET"])
def retrieve_single_planet(planet_id):
    planet = Planet.query.get(planet_id)

    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "radius": planet.radius,
    }