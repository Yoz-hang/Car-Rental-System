from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data stores
vehicles = []
customers = []
rentals = []

@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    return jsonify(vehicles)

@app.route('/vehicles', methods=['POST'])
def add_vehicle():
    data = request.json
    vehicle = {
        "model": data["model"],
        "rental_rate": data["rental_rate"],
        "vin": data["vin"],
        "available": True
    }
    vehicles.append(vehicle)
    return jsonify(vehicle), 201

@app.route('/customers', methods=['GET'])
def get_customers():
    return jsonify(customers)

@app.route('/customers', methods=['POST'])
def add_customer():
    data = request.json
    customer = {
        "name": data["name"],
        "phone_number": data["phone_number"],
        "rented_vehicles": []
    }
    customers.append(customer)
    return jsonify(customer), 201

@app.route('/rent', methods=['POST'])
def rent_vehicle():
    data = request.json
    customer_name = data["customer_name"]
    vin = data["vin"]
    rental_duration = data["rental_duration"]

    vehicle = next((v for v in vehicles if v["vin"] == vin and v["available"]), None)
    customer = next((c for c in customers if c["name"] == customer_name), None)

    if not vehicle or not customer:
        return jsonify({"error": "Customer or vehicle not found, or vehicle not available."}), 400

    vehicle["available"] = False
    customer["rented_vehicles"].append(vin)
    rental = {
        "customer_name": customer_name,
        "vin": vin,
        "rental_duration": rental_duration,
        "cost": rental_duration * vehicle["rental_rate"]
    }
    rentals.append(rental)
    return jsonify(rental), 201

@app.route('/return', methods=['POST'])
def return_vehicle():
    data = request.json
    customer_name = data["customer_name"]
    vin = data["vin"]

    customer = next((c for c in customers if c["name"] == customer_name), None)
    vehicle = next((v for v in vehicles if v["vin"] == vin), None)

    if not customer or not vehicle or vin not in customer["rented_vehicles"]:
        return jsonify({"error": "Customer or vehicle not found, or vehicle not rented by customer."}), 400

    vehicle["available"] = True
    customer["rented_vehicles"].remove(vin)
    return jsonify({"message": "Vehicle returned successfully."})

if __name__ == '__main__':
    app.run(debug=True)
    
