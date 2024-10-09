class Device:
    def __init__(self, brand, model, price):
         self.brand = brand
         self.model = model
         self.price = price
    def turn_on(self):
         print(f"{self.brand} {self.model} is powered on.") 
    def turn_off(self):
         print(f"{self.brand} {self.model} is powered off.")
    def display_info(self):
         print(f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}")
class Laptop(Device):
    def __init__(self, brand, model, price, ram_size):
         super().__init__(brand, model, price)
         self.ram_size = ram_size
    def open_laptop(self):
         print(f"{self.brand} {self.model} laptop is opened.")
class Smartphone(Device):
    def __init__(self, brand, model, price, camera_resolution):
         super().__init__(brand, model, price)
         self.camera_resolution = camera_resolution
    def take_photo(self):
         print(f"Photo taken with {self.brand} {self.model} smartphone.")


laptop = Laptop("Dell", "XPS 13", 999.99, 16)
smartphone = Smartphone("Apple", "iPhone 14", 799.99, 12)
