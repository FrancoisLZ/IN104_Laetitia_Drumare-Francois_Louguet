
class vehicules:
    def __init__(self,color, brand, price):
        self.color = color
        self.brand = brand
        self.price = price


    #affichage des différents paramètres

    def method1(self):
        return (self.color)

    def method2(self):
        return (self.brand)

    def method3(self):
        return (self.price)

class cars(vehicules):

    def details(self, car_boot_size, width):
        self.__car_boot_size = car_boot_size
        self.__width = width

        
    def get_width(self):     
        return (self.__width)

    def identity(self):
        print("This car is"+str(method1(self))+ "of the brand" +str(method2(self)))

    def size(self):
        print("This car is" +str(self.width)+"meters large")

class motorbike(vehicules):

    def details(self,weight,engine_power):
        self.__weight = weight
        self.__engine_power= engine_power

    def get_weight(self):
        return self.__weight

    def __get_power(self):
        print (self.engine_power)

    def define(self):
        print("This motorcycle weighs exactly" +str(self.__weight)+"pounds and has a motor power of" + str(self.engine_power))
