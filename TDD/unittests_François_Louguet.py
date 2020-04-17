import Class.py 
import unittest

class get_colorTest(unittest.TestCase):
    
    def setUp(self):
        self.color = "jaune"
        self.brand = "lamborghini"
        self.price = 500000
    
    def test_get_color(self):
        """ teste le fonctionnement de get_color"""
        self.assertEqual(get_color(self),self.color)

    def test_get_color(self):
        """ teste le fonctionnement de get_color"""
        self.assertEqual(get_color(self),self.color)
    
    def test_get_color(self):
        """ teste le fonctionnement de get_color"""
        self.assertEqual(get_color(self),self.color)
