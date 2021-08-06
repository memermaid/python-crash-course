class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name, self.last_name)
    
    def greet_user(self):
        print(f'Hello, {self.first_name} {self.last_name}.')

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User('Natalya', 'Zakharova')
user2 = User('Chshebetun', 'Irina')
user3 = User('Vladislav', 'Zakharov')

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(f'User {user1.first_name} has {user1.login_attempts} login attemps.')
user1.reset_login_attempts()
print(f'User {user1.first_name} has {user1.login_attempts} login attemps.')


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = []

    def show_privileges(self):
        print(f'Admin {self.first_name} {self.last_name} has the following privileges: ')
        for i in self.privileges:
            print("-", i)


admin1 = Admin("Natalya", "Ivanova")
admin1.privileges = ['can add post', 'can delete post']
admin1.show_privileges()