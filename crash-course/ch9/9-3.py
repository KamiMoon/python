class Users(object):

    def __init__(self, first_name, last_name, age, religion):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.religion = religion

    def describe_user(self):
        print('Hello ' + self.first_name + " " + self.last_name + " " + str(self.age) + " " + self.religion)


user1 = Users("Eric", "Kizaki", 30, "None")
user2 = Users("Bob", "Sagat", 40, "Christian")
user3 = Users("Nick", "Con", 25, "Buddhist")

user1.describe_user()
user2.describe_user()
user3.describe_user()