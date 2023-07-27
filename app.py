import os
import googlemaps
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_openapi3 import OpenAPI, Info
from config.config import access


info = Info(title='Xtrim Api', version='1.0.0')


jwt = {
    "type": "http",
    "scheme": "bearer",
    "bearerFormat": "JWT"
}
security_schemes = {"jwt": jwt}


config = access()
os.environ["FLASK_DEBUG"] = config["FLASK_DEBUG"]


app = OpenAPI(__name__, info=info, security_schemes=security_schemes)


app.config["FLASK_APP"] = config["FLASK_APP"]
app.config["FLASK_DEBUG"] = config["FLASK_DEBUG"]
app.config["SECRET_KEY"] = config["SECRET_KEY"]
app.config["SQLALCHEMY_DATABASE_URI"] = config["DB"]["SQLALCHEMY_DATABASE_URI"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SALT"] = config["SALT"]

google_maps_api_key = googlemaps.Client(key=(config["KEY_API_GOOGLE_MAPS"]))


db = SQLAlchemy(app)
migrate = Migrate(app, db)


from controllers import (
    
    geolocation_controller,
    
)


app.register_api(geolocation_controller.bp)



if __name__ == "__main__":
    app.run(port=2064)
