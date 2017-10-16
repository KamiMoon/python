class Restaurant(object):

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(self.restaurant_name + ", " + self.cuisine_type)
    
    def open_restaurant(self):
        print('The restaurant is now open')



somePlace = Restaurant("Wendy's", "Fast Food")
print(somePlace.restaurant_name)
print(somePlace.cuisine_type)
somePlace.describe_restaurant()
somePlace.open_restaurant()
