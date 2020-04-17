
import unittest

class get_colorTest(unittest.Testcase):
    
    def setUp(self):
        self.color = "jaune"
        self.brand = "lamborghini"
        self.price = 500000
    
    def test_get_color(self):
        self.assertEqual(get_color(self),self.color)

