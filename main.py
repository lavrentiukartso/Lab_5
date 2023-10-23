class User:
    def __init__(self, id, name, user_name, password):
        self.id = id
        self.name = name
        self.user_name = user_name
        self.password = password

user1 = User(id=1, name="Lavrentiuk Arturun", user_name="lavrentiukartso", password="01052004")

print("User ID:", user1.id)
print("Name:", user1.name)
print("Username:", user1.user_name)
print("Password:", user1.password)
