import unittest 
from city_functions import city_country

class CityTestCase( unittest.TestCase): 

    def test_city_country(self): 
        test = city_country('Mexico City', 'Mexico')
        self.assertEqual(test, 'Mexico City, Mexico')
    
    def test_city_country_pop(self): 
        test = city_country('Mexico City', 'Mexico', 5000)
        self.assertEqual(test, 'Mexico City, Mexico - 5000')

unittest.main()

