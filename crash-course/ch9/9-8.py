from users import Users
from privileges import Privilege

class Admin(Users):

    def __init__(self, first_name, last_name, age, religion, privileges, login_attempts=0):
        super(Admin, self).__init__(first_name, last_name, age, religion, login_attempts)

        self.privileges = Privilege(privileges)



admin = Admin('Eric', 'Kizaki', 30, 'None', ['add', 'edit', 'delete'])
admin.privileges.show_privileges()