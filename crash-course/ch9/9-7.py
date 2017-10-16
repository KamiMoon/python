from users import Users

class Admin(Users):

    def __init__(self, first_name, last_name, age, religion, privileges, login_attempts=0):
        super(Admin, self).__init__(first_name, last_name, age, religion, login_attempts)

        self.privileges = privileges

    def show_privileges(self):
        print(str(self.privileges))


admin = Admin('Eric', 'Kizaki', 30, 'None', ['add', 'edit', 'delete'])
admin.show_privileges()