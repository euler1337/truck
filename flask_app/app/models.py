from app import db
from app import app
import sys

class Truck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    longitude = db.Column(db.Float, index=True, unique=False)
    latitude = db.Column(db.Float, index=True, unique=False)

    def __repr__(self):
        return 'Truck %r> at (long, lat) = (%f,%f)' % (self.name, self.longitude, self.latitude)

    def serialize(self):
    	return {'name'      : self.name,
    			'longitude' : self.longitude,
    			'latitude'  : self.latitude}

    def update_position(self, longitude, latitude):
    	self.longitude = longitude
    	self.latitude = latitude
    	db.session.commit()

    def add_to_database(self):
    	db.session.add(self)
    	db.session.commit()

def addDummyTrucks():
    dummy = ["Sofies Pizza", "Mickes Tacos", "Glassbilen", "Indiska rullar", "Husmans-Trucken"]
    longs = [18.0755917, 18.0765917, 18.0775917, 18.0785917, 18.0795917]
    lats  = [59.3271778, 59.3261778, 59.3251778, 59.3241778, 59.3231778]
    i = 0

    num_rows_deleted = db.session.query(Truck).delete()
    db.session.commit()

    for truck in dummy:

        if Truck.query.filter_by(name=truck).first() is None:
            d = Truck(name = truck, longitude = longs[i], latitude = lats[i])
            db.session.add(d)
            db.session.commit()
            i = i+1


def getAllTrucks():
	return Truck.query.all()