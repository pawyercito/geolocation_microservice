from app import db


class GeolocationLogs(db.Model):
    __tablename__ = "geolocation_logs"
    id_geolocation_log = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey("users.id"))
    id_prospect = db.Column(db.Integer, db.ForeignKey("prospect.id"))
    ip_user= db.Column(db.String(100))
    latitude = db.Column(db.Float)  # Campo para guardar la latitud
    longitude = db.Column(db.Float)  # Campo para guardar la longitud
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __init__(self, payload):
        self.id_prospect = payload.get("id_prospect")
        self.id_user = payload.get("id_user")
        self.ip_user = payload.get("ip_user")
        self.latitude = payload.get("latitude")
        self.longitude = payload.get("longitude")

    def to_json(self):
        return {
            "id_geolocation_log": self.id_geolocation_log,
            "id_user": self.id_user,
            "id_prospect": self.id_prospect,
            "ip_user": self.ip_user,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "created_at": self.created_at,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
