from restaurant import Restaurant

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super(IceCreamStand, self).__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print(str(self.flavors))


someStand = IceCreamStand('My Ice', 'Ice Cream', ['Chocolate', 'Strawberry'])
someStand.display_flavors()