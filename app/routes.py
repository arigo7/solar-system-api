from app import db
from flask import Blueprint
from .models.planet import Planet
from flask import request
from flask import jsonify 


# creating instance of the class, first arg is name of app's module
planet_bp = Blueprint("planets", __name__, url_prefix="/planets")

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
            "message": f"Planet #{new_planet.name} has been created"
            }, 201

# @planet_bp.route("", methods = ["POST", "GET"], strict_slashes = False)
# def handle_planets_data():
#     if request.method == "GET":
#         planet = Planet.query.all()
#         planets_response = []
#         for planet in planets:
#             planets_response.append({
#                 "id": planet.id,
#                 "name": planet.name,
#                 "description": planet.description,
#                 "size": planet.size,
#             })
#         return jsonify(planets_response), 200  # returning the list of all planets
#     else: # for POST request
#         request_body = request.get_json() # for one planet 
#     new_planet = Planet(name = request_body["name"],
#                     description = request_body["description"],
#                     size = request_body["size"])

#     db.session.add(new_planet) # "adds model to the db"
#     db.session.commit() # does the action above
#     # return (f"Book #{new_book.title} has been created", 201)
#     return {"success": True,
#             "message": f"Book #{new_book.title} has been created"
#             }, 201

