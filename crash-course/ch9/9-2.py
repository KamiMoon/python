class Restaurant(object):

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(self.restaurant_name + ", " + self.cuisine_type)
    
    def open_restaurant(self):
        print('The restaurant is now open')



somePlace = Restaurant("Wendy's", "Fast Food")
somePlace.describe_restaurant()


somePlace1 = Restaurant("Burger King", "Fast Food")
somePlace1.describe_restaurant()


somePlace2 = Restaurant("Whataburger", "Other Fast Food")
somePlace2.describe_restaurant()