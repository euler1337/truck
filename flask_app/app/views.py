from app import app
from flask import render_template, abort
from flask import jsonify, flash, request
from models import Truck, addDummyTrucks, getAllTrucks

@app.route("/index")
@app.route("/")
def main():
	addDummyTrucks()
	return render_template('index.html')

@app.route('/update', methods=['GET'])
def update():

    trucks = getAllTrucks()
    #return jsonify({
    #  'name'      : trucks[0].name,
    #  'longitude' : trucks[0].longitude,
    #  'latitude'  : trucks[0].latitude })
    return jsonify(d=[e.serialize() for e in trucks])

# THE API
@app.route('/api/v0.1/register', methods=['POST'])
def create_truck():

    if not request.json:
        abort(403)

    truckObj = Truck.query.filter_by(name=request.json['name']).first()

    if truckObj is not None:
        abort(402)

    for a in ['name', 'longitude', 'latitude']:
        if a not in request.json:
            abort(403)

    newTruck = Truck(name = request.json['name'], longitude = request.json['longitude'], latitude = request.json['latitude'])
    newTruck.add_to_database()

    return jsonify(newTruck.serialize()), 201

@app.route('/api/v0.1/update_position', methods=['POST'])
def update_position():

    # Check if truck is registered in database
    # If registered, update its coordinates.

    # validate request
    if not request.json:
        abort(400)

    for a in ['name', 'longitude', 'latitude']:
        if a not in request.json:
            abort(400)

    # Check that truck is in database
    truckObj = Truck.query.filter_by(name=request.json['name']).first()
    if truckObj is None:
        abort(400)

    truckObj.update_position(longitude=request.json['longitude'], latitude=request.json['latitude'])

    return jsonify(truckObj.serialize()), 204