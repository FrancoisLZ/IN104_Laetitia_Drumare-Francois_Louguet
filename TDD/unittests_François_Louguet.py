import unittest
import classe


class FonctionsTest(unittest.TestCase):
    
   
     
    def test_get_color(self):
        """ teste le fonctionnement de get_color"""
        v=classe.Car("jaune","lamborghini",500000)
        self.assertEqual(classe.Car.get_color(v),"jaune")

    def test_get_brand(self):
        """ teste le fonctionnement de get_brand"""
        v=classe.Car("jaune","lamborghini",500000)
        self.assertEqual(classe.Car.get_brand(v),"lamborghini")
    
    def test_get_price(self):
        """ teste le fonctionnement de get_price"""
        v=classe.Car("jaune","lamborghini",500000)
        self.assertEqual(classe.Car.get_price(v),500000)

    def test_get_width(self):
        """ teste le fonctionnement de get_width"""
        v=classe.Car("jaune","lamborghini",500000)
        classe.Car.details_car(v,2,3)
        self.assertEqual(classe.Car.get_width(v),3)

if __name__=="__main__":
    unittest.main()
