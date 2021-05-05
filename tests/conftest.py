import pytest
from app import create_app
from app import db
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def two_saved_planets(app):
    # Arrange
    one_planet = Planet(name="One Planet",
                        description="watr 4evr",
                        radius = 123.1)
    two_planet = Planet(name="Two Planet",
                        description="watr 4evr",
                        radius = 223.1)
    db.session.add_all([one_planet, two_planet])
    # Alternatively, we could do
    # db.session.add(one_planet)
    # db.session.add(two-planet)
    db.session.commit()
#POST /planets with a JSON request body returns a 201
@pytest.fixture
def create_one_planet(app):
    # Arrange
    return{
        "description": "Another Fourth planet from the Sun and the second-smallest planet in the Solar System, being larger than only Mercury.",
        "name": "Another Mars",
        "radius": 2106.1
    }