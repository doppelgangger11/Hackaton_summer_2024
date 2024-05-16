from user import User
from ticket import Ticket
import hashlib
import csv
import uuid

class UserManager():
    def __init__(self, userList: list):
        self.userList: list[dict] = userList
        self.user = None
        

    def add_user(self, username: str, password: str):
        id_ = str(uuid.uuid4())
        new_user = User(username=username, password=password, id_=id_)
        
        for user in self.userList:
            if new_user.username == user['username']:
                print("User is already exist")
                return
        
        new_user_dict = {'ID': new_user.id_, 'username': new_user.username, 'password': new_user.password, 'tickets': []}
        self.userList.append(new_user_dict)
        new_user.save()

    def login(self, username: str, password: str, id_: str):
        for user in self.userList:
            if user['username'] == username and user['password'] == hashlib.sha256(password.encode()).hexdigest():
                self.user = User(username=username, password=password, id_=id_)
            else:
                print("User does not exist")

    def logout(self):
        if self.user != None:
            print(f"Goodbye {self.user.username}!")
            self.user = None

    def buy_ticket(self, ticket: Ticket):
        if self.user is not None:
            self.user.add_ticket(ticket)  # Используем метод add_ticket для добавления билета к пользователю
            self.user.save()
        else:
            print("You must be logged in to buy a ticket")


    def __str__(self) -> str:
        return str(self.userList)
