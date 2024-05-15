from user import User
import hashlib
import csv

class UserManager():
    def __init__(self, userList: list):
        self.userList = userList
        self.user = None
        

    def add_user(self, username, password):
        user = User(username=username, password=password)
        self.userList.append(self.user)
        user.save()

    def login(self, username, password):
        for user in self.userList:
            if user['username'] == username and user['password'] == hashlib.sha256(password.encode()).hexdigest():
                self.user = User(username=username, password=password)
            else:
                print("User does not exist")

    def logout(self):
        if self.user != None:
            print(f"Goodbye {self.user.name}!")
            self.user = None

    def __str__(self) -> str:
        return str(self.userList)
