import Class
import unittest

class get_colorTest(unittest.TestCase):
    
   
    
    def test_get_color(self):
        """ teste le fonctionnement de get_color"""
        v=Vehicule("jaune","lamborghini",500000)
        self.assertEqual(Class.get_color(v),v.color)

    def test_get_brand(self):
        """ teste le fonctionnement de get_brand"""
        v=Vehicule("jaune","lamborghini",500000)
        self.assertEqual(Class.get_brand(v),v.brand)
    
    def test_get_price(self):
        """ teste le fonctionnement de get_price"""
        v=Vehicule("jaune","lamborghini",500000)
        self.assertEqual(Class.get_price(v),v.price)

    def test_get_width(self):
        """ teste le fonctionnement de get_width"""
        c=Car(2,3)
        self.assertEqual(Class.get_price(c),c.price)
