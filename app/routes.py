from app import db
from flask import Blueprint
from .models.planet import Planet
from flask import request
from flask import jsonify 
# checking they all work 
# creating instance of the class, first arg is name of app's module
planet_bp = Blueprint("planets", __name__, url_prefix="/planets")

#Update a planet
@planet_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet: # successful updating planet
        form_data = request.get_json() # save user input form_data as json format 
        planet.name = form_data["name"] # updating model? title field language?
        planet.description = form_data["description"] # updating model description field for planet = planet_id
        planet.radius = form_data["radius"]
        db.session.commit()
        return {"success": True,
                "message": f"Planet #{planet.id}, successfully updated"
                }, 201
    return {"success": False,
            "message": f"Planet #{planet_id} was not found"
            }, 404

#Delete a planet
@planet_bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet:
        db.session.delete(planet)
        db.session.commit()
        return {"success": True,
                "message": f"Planet {planet.id} successfully deleted" }, 201
    return {"success": False,
            "message": f"Planet {planet_id} was not found" }, 404

#create a planet
@planet_bp.route("", methods = ["POST"], strict_slashes = False)
def handle_planet_data():
    
    request_body = request.get_json()

    # returns response if body of request is empty
    if request_body == None or request_body.get("name") == None \
        or request_body.get("description") == None \
            or request_body.get("radius") == None:
        return {"success": False, "message": f"Please provide planet info" }, 404

    new_planet = Planet(name=request_body["name"],
                    description=request_body["description"],
                    radius = request_body["radius"]) 
    db.session.add(new_planet) # "adds model to the db"
    db.session.commit() # does the action above
    return {"success": True,
            "message": f"Planet {new_planet.name} has been created"
            }, 201

#Retrieve all planets  
@planet_bp.route("", methods = ["GET"], strict_slashes = False)
def retrieve_planets_data():
    #request.method == "GET":
        planets = Planet.query.all()
        if planets != None:
            planets_response = []
            for planet in planets:
                planets_response.append({
                    "id": planet.id,
                    "name": planet.name,
                    "description": planet.description,
                    "radius": planet.radius,
                })
            return jsonify(planets_response), 200  # returning the list of all planets
        return {"success": False, "message": f"There are no planets" }, 404

#Retrieve one planet
@planet_bp.route("/<planet_id>", methods=["GET"])
def retrieve_single_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet:
        return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "radius": planet.radius,
        }
    return {"success": False,
            "message": f"Planet {planet_id} was not found" }, 404
