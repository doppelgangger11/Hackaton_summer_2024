from user import User
from ticket import Ticket
import hashlib
import csv
import uuid

class UserManager():
    def __init__(self, userList: list):
        self.userList = userList
        self.user = None
        

    def add_user(self, username: str, password: str):
        id_ = str(uuid.uuid4())
        user = User(username=username, password=password, id_=id_)
        for user in self.userList:
            if user['ID'] != id_ and user['username'] != username and user['password'] != password:
                self.userList.append(self.user)
                user.save()
        else:
            print("User is already exist")

    def login(self, username: str, password: str, id_: str):
        for user in self.userList:
            if user['username'] == username and user['password'] == hashlib.sha256(password.encode()).hexdigest():
                self.user = User(username=username, password=password, id_=id_)
            else:
                print("User does not exist")

    def logout(self):
        if self.user != None:
            print(f"Goodbye {self.user.name}!")
            self.user = None

    def buy_ticket(self, ticket: Ticket):
        if self.user != None:
            self.user.tickets.append(f'{ticket.ticket_id}')
            self.user.save()
        else:
            print("You must be logged in to buy a ticket")


    def __str__(self) -> str:
        return str(self.userList)
