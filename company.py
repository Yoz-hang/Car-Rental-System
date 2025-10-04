from .vehicle import Vehicle
from .customer import Customer

class Company:
    def __init__(self, name):
        self._name = name
        self._income = 0.0
        self._vehicles = {}
        self._customers = []

    def get_name(self):
        return self._name
    
    def get_income(self):
        return self._income
    
    def get_vehicles(self):
        return self._vehicles 
    
    def get_customers(self):
        return self._customers
    
    def set_name(self, name):
        self._name = name   
             
    def set_income(self, income):
        self._income = income
        
    def set_customers(self, customers):
        self._customers = customers   
             
    def set_vehicles(self, vehicles):
        self._vehicles = vehicles
    
    def add_to_income(self, value):
        self._income += value
        
    def add_vehicle(self, vehicle):
        self._vehicles[vehicle.get_vin()] = vehicle
        
    def add_customer(self, customer):
        for individual_customer in self._customers:
            if individual_customer.get_name() == customer.get_name():
                return False
        self._customers.append(customer)
        return True
        
    def rent_vehicle(self, customer_name, vin, rental_duration):
        customer = None
        for c in self._customers:
            if c.get_name() == customer_name:
                customer = c
                break
        vehicle = self._vehicles.get(vin)
        if customer is None or vehicle is None or not vehicle.get_available():
            return False
        vehicle.set_available(False)
        rental_cost = rental_duration * vehicle.get_rental_rate()
        self._income += rental_cost
        customer.add_rented_vehicle(vehicle)
        return True
        
    def get_summary(self, file_name):
        summary = f"Company Name: {self.get_name()}\n"
        summary += f"Total income: {self.get_income()} CAD\n"
        summary += "Customers:\n"
        for customer in self._customers:
            summary += customer.get_name() 
            summary += f" rented {len(customer.get_rented_vehicles())} vehicle(s)\n"
        summary += "Vehicles:\n"
        for vehicle in self._vehicles.values():
            summary += f"{vehicle.get_model()} ({vehicle.get_vin()}),  Available: {vehicle.get_available()}\n"
        summary += "End of Summary"
        with open(file_name, 'w') as file:
            file.write(summary)