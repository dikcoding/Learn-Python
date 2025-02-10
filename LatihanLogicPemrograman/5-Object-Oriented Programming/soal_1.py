from abc import ABC, abstractmethod

# Kelas HouseData dengan konsep Encapsulation
class HouseData:
    def __init__(self, locatioin, size, bedrooms, price):
        self.__location = locatioin
        self.__size = size
        self.__bedrooms = bedrooms
        self.__price = price
        
    # Getter dan Setter untuk location
    def get_location(self):
        return self.__location
    
    def set_location(self, location):
        self.__location = location
    
    # Getter dan Setter untuk size
    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size
    
    # Getter dan Setter untuk bedrooms
    def get_bedrooms(self):
        return self.__bedrooms
    
    def set_bedrooms(self, bedrooms):
        self.__bedrooms = bedrooms
    
    # Getter dan Setter untuk price
    def get_price(self):
        return self.__price
    
    def set_price(self, price):
        self.__price = price

# Class abstrak MLModel dengan konsep abstraction
class MLModel(ABC):
    @abstractmethod
    def train(self):
        pass
    
    @abstractmethod
    def predict(self, house: HouseData):
        pass

# Class LinearRegressionModel dengan konsep Inheritance dan Polymorphism
class LinearRegressionModel(MLModel):
    def train(self):
        print("Model dilatih dengan metode regresi linear.")
    
    def predict(self, house: HouseData):
        size = house.get_size()
        bedrooms = house.get_bedrooms()
        harga_prediksi = (size * 5000) + (bedrooms * 10000)
        return harga_prediksi
    
# Contoh Pengguna
if __name__ == "__main__":
    # Membuat objek dari class HouseData
    house = HouseData("Jakarta", 100, 2, 0)

    # Membuat Objek LinearRegressionModel
    model = LinearRegressionModel()

    # Melatih model
    model.train()

    # Melakukan Prediksi harga rumah
    prediksi_harga = model.predict(house)
    print(f"Prediksi harga rumah: {prediksi_harga}")