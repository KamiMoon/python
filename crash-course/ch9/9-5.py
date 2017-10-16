class Users(object):

    def __init__(self, first_name, last_name, age, religion, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.religion = religion
        self.login_attempts = login_attempts

    def describe_user(self):
        print('Hello ' + self.first_name + " " + self.last_name + " " + str(self.age) + " " + self.religion)
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = Users("Eric", "Kizaki", 30, "None")
print(user1.login_attempts)
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)

