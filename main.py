from usermanager import UserManager
from ticket import Ticket
import csv 
import parce
from typing import Any

user_list: list[dict] = list()

try:
    with open('users.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[0] != 'ID':
                user = dict()
                user['ID'] = row[0]
                user['username'] = row[1]
                user['password'] = row[2]
                user['tickets'] = row[3].split('-')[:-1:]

                user_list.append(user)

except FileNotFoundError:
    print("File not found")
    with open('users.csv', 'w') as csv_file:
        csv_file.write('ID,username,password,tickets\n')
    

def get_command(user_manager):
    if user_manager.user == None:
        com: str = input("Enter the command >>> ").strip()
        return com
    com: str = input(f"Enter the command {user_manager.user.username} >>> ").strip()

    return com


user_manager: UserManager = UserManager(user_list)
list_of_futures: (dict[str, dict[str, Any]]) = parce.main()

ticket_list: dict[str, Ticket] = dict()
for id_ in list_of_futures:
    # print(type(id_)) -> str
    ticket = Ticket(title=list_of_futures[id_]['title'], date=list_of_futures[id_]['date'], id_=int(id_), link=list_of_futures[id_]['link'])
    ticket_list[id_] = ticket

run: bool = True

while run:
    print(user_manager.userList)
    # print(list_of_futures)
    # for i in ticket_list:
    #     print(i)

    com = get_command(user_manager)

    if com != 'q':
        if user_manager.user == None:
            if com == "add":
                user_manager.add_user(
                    username=input("enter the username >>> ").strip(), 
                    password=input("enter the password >>> ").strip()
                )
            elif com == "login":
                username = input("enter the username >>> ").strip()
                password = input("enter the password >>> ").strip()
                
                for user in user_list:
                    if user['username'] == username and user['password'] == password:
                        id_ = user['ID']
                
                user_manager.login(
                    username=username,
                    password=password,
                    id_=id_
                )
            else:
                print("Invalid command")

        if user_manager.user != None:
            if com == "logout":
                user_manager.logout()
            elif com == "buy":
                for ticket in ticket_list:
                    print(ticket_list[ticket])
                ticket_id = input("Enter the ticket ID >>> ").strip()
                
                if ticket_id in ticket_list:
                    user_manager.buy_ticket(ticket=ticket_list[ticket_id])
                elif ticket_id == 'q':
                    break
                else:
                    print("Invalid ticket ID")

            elif com == "my":
                for ticket in user_manager.user.tickets:
                    print(ticket_list[ticket])
            elif com == "login":
                pass
            else:
                print("Invalid command")
    else:
        break