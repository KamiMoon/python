class Privilege(object):

    def __init__(self, privileges):
        self.privileges = privileges
    
    def show_privileges(self):
        print(str(self.privileges))
