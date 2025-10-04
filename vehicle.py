class Vehicle:
    # Shared VIN set to ensure uniqueness across all Vehicle instances
    _vin_set = set()
    
    def __init__(self, model, rental_rate, vin, available=True):
        self._validate_vin(vin)
        self._model = model
        self._rental_rate = rental_rate
        self._available = available
        self._vin = vin
        
    def _validate_vin(self, vin):
        if len(vin) != 6:
            raise ValueError("VIN must be 6 characters.")
        has_digit = any(char.isdigit() for char in vin)
        if not has_digit:
            raise ValueError("VIN must contain at least one digit.")
        if vin in self._vin_set:
            raise ValueError("VIN must be unique.")
        self._vin_set.add(vin)
        
    def get_model(self):
        return self._model
    
    def get_rental_rate(self):
        return self._rental_rate
    
    def get_vin(self):
        return self._vin
    
    def get_available(self):
        return self._available
    
    def set_model(self, model):
        self._model = model
    
    def set_rental_rate(self, rental_rate):
        self._rental_rate = rental_rate
    
    def set_available(self, available):
        self._available = available