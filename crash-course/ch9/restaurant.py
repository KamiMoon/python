class Restaurant(object):

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.numbered_served = 0
    
    def describe_restaurant(self):
        print(self.restaurant_name + ", " + self.cuisine_type)
    
    def open_restaurant(self):
        print('The restaurant is now open')
    
    def set_numbered_served(self, numbered_served):
        self.numbered_served = numbered_served

    def increment_numbered_served(self):
        self.numbered_served += 1
