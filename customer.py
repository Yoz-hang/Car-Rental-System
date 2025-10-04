# This file manages customer information

class Customer:
    def __init__(self, name, phone_number):
        self._name = name
        self._phone_number = phone_number
        self._rented_vehicles = {}

    def get_name(self):
        return self._name

    def get_phone_number(self):
        return self._phone_number

    def get_rented_vehicles(self):
        return self._rented_vehicles

    def set_name(self, name):
        self._name = name

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def add_rented_vehicle(self, vehicle):
        vin = vehicle.get_vin()
        self._rented_vehicles[vin] = vehicle

    def return_rented_vehicle(self, vin):
        if vin in self._rented_vehicles:
            vehicle = self._rented_vehicles[vin]
            vehicle.set_available(True)
            del self._rented_vehicles[vin]
            return True
        else:
            return False