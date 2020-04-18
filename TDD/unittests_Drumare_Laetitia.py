import unittest
import classe


class FonctionsTest(unittest.TestCase):
    
   
     
    def test_get_color(self):
        v=classe.Vehicule('blue','Citroen','15000')
        self.assertEqual(classe.Car.get_color(v),'blue')

    def test_get_brand(self):
        v=classe.Vehicule('blue','Citroen','15000')
        self.assertEqual(classe.Car.get_brand(v),'Citroen')
    
    def test_get_price(self):
        v=classe.Vehicule('blue','Citroen','15000')
        self.assertEqual(classe.Car.get_price(v),'15000')

    def test_get_weight(self):
        "" teste le fonctionnement de get_weight pour la classe Motorbike""
        m=classe.Motorbike('white','vespa','1000')
        classe.Motorbike.details_motorbike(m,70,23)
        self.assertEqual(classe.Motorbike.get_weight(m),70)
        
    def test_get_power(self):
        "" teste le fonctionnement de get_power pour la classe Motorbike""
        m=classe.Motorbike('white','vespa','1000')
        classe.Motorbike.details_motorbike(m,70,23)
        self.assertEqual(classe.Motorbike.get_power(m),23)

if __name__=="__main__":
    unittest.main()
