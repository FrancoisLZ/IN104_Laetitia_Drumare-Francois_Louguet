class Vehicule:
    """ on definit ici la superclasse "Vehicule" """
    
    def __init__(self,color, brand, price):
        self.color = color
        self.brand = brand
        self.price = price


    # methodes de la classe "Vehicule"

    def get_color(self):
        return (self.color)

    def get_brand(self):
        return (self.brand)

    def get_price(self):
        return (self.price)

class Car(Vehicule):
    """ on definit ici la premiere sous classe "Car" """
    
    # methodes de la classe "Car"
    
    def details_car(self, car_boot_size, width):
        self.__car_boot_size = car_boot_size
        self.__width = width

    def get_width(self):     
        return (self.__width)

    def identity(self):
        print("This car is a "+str(Vehicule.get_color(self))+ " car of the brand " +str(Vehicule.get_brand(self)))

    def size(self):
        print("This car is " +str(self.__width)+" meters large")

class Motorbike(Vehicule):
    """ on definit ici la deuxieme sous classe "Motorbike" """

    #methodes de la classe "Motorbike"
    
    def details_motorbike(self,weight,engine_power):
        self.__weight = weight
        self.__engine_power= engine_power

    def get_weight(self):
        return self.__weight

    def get_power(self):
        return self.__engine_power

    def define(self):
        print("This motorcycle weighs exactly " +str(self.__weight)+" pounds and has a motor power of " + str(self.__engine_power))

        
        
