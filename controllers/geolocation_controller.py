from app import google_maps_api_key
from flask import request, jsonify
from flask_cors import cross_origin
from decorators.auth_decorator import auth_required
#from decorators.validate_transaction import validate_external_transaction_id
from flask_openapi3 import APIBlueprint, Tag
from schema.jwt_schema import Unauthorized
from schema.api_schema import ApiResponse
from schema.geolocation_schema import RevGeocode



tag = Tag(name="Geolocation", description="Geolocation endpoints")
security = [{"jwt": []}]

bp = APIBlueprint(
    "geolocation",
    __name__,
    url_prefix="/api/geolocation",
    abp_tags=[tag],
    abp_security=security,
    abp_responses={"401": Unauthorized},
    # disable openapi UI
    doc_ui=True,
)


@bp.get("/get-location", responses={"200": ApiResponse, "400": None})
@cross_origin()
@auth_required
#@validate_external_transaction_id
def get_geolocation(user_id):
    """
    Obtiene la geolocalización del usuario basada en su dirección IP.

    Args:
         (User): Usuario actual autenticado.
        external_transaction_id (str): ID de transacción externa opcional.
        channel (str): Canal opcional.
        internal_transaction_id (str): ID de transacción interna opcional.

    Returns:
        flask.Response: Respuesta HTTP JSON que contiene la dirección IP del usuario y su geolocalización.

    """
    response_data = {}

    try:
        ip = request.environ.get("HTTP_X_FORWARDED_FOR", request.remote_addr)
        geolocation = google_maps_api_key.geolocate()
        location = geolocation["location"]

        response_data.update({
            "code": 200,
            "success": True,
            "ip": ip,
            "location": location
        })

        return jsonify(response_data), 200
   
    except Exception as e:
        response_data.update({
            "code": 500,
            "success": False,
            "message": str(e)
        })
        
        return jsonify(response_data), 500


@bp.post("/rev-geocode", responses={"200": ApiResponse, "400": None})
@cross_origin()
@auth_required
#@validate_external_transaction_id
def get_rev_geocode(user_id, body:RevGeocode=None):
    """
    Obtiene la ubicación inversa (reverse geocoding) basada en las coordenadas proporcionadas.

    Args:
         (User): Usuario actual autenticado.
        external_transaction_id (str): ID de transacción externa opcional.
        channel (str): Canal opcional.
        internal_transaction_id (str): ID de transacción interna opcional.

    Returns:
        flask.Response: Respuesta HTTP JSON que contiene la ubicación inversa correspondiente a las coordenadas proporcionadas.

    """
    response_data = {}

    try:
        data = google_maps_api_key.reverse_geocode((request.json["lat"], request.json["lng"]))

        response_data.update({
            "code": 200,
            "success": True,
            "data": data
        })

        return jsonify(response_data), 200
   
    except Exception as e:
        response_data.update({
            "code": 500,
            "success": False,
            "message": str(e)
        })
        
        return jsonify(response_data), 500