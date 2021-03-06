import unittest 
from name_function import get_formatted_name

class NamesTestCase( unittest.TestCase): 
    """ Tests for 'name_function.py'.""" 
    def test_first_last_name( self): 
        """ Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name(' janis', 'joplin')
        self.assertEqual( formatted_name, 'Janis Joplin')

unittest.main()

Table 11-1: Assert Methods Available from the unittest Module 

Method Use 
assertEqual( a, b) Verify that a = = b 
assertNotEqual( a, b) Verify that a != b 
assertTrue( x) Verify that x is True 
assertFalse( x) Verify that x is False 
assertIn( item, list) Verify that item is in list 
assertNotIn( item, list) Verify that item is not in list


def setUp(self): - before each test - add to self
