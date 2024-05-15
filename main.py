from usermanager import UserManager
import csv 
import parce

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
                user['tickets'] = row[3].split('-')

                user_list.append(user)

except FileNotFoundError:
    print("File not found")
    with open('users.csv', 'w') as csv_file:
        csv_file.write('ID,username,password,tickets')
    

def get_command(user_manager):
    if user_manager.user == None:
        com: str = input("Enter the command >>> ").strip()
        return com
    com: str = input(f"Enter the command {user_manager.user.name} >>> ").strip()

    return com


user_manager: UserManager = UserManager(user_list)
list_of_futures = parce.main()
run: bool = True

while run:
    print(user_manager)
    print(list_of_futures)
    com = get_command(user_manager)

    if com != 'q':
        if user_manager.user == None:
            if com == "add":
                user_manager.add_user(
                    username=input("enter the username >>> ").strip(), 
                    password=input("enter the password >>> ").strip()
                )
            elif com == "login":
                user_manager.login(
                    username=input("enter the username >>> ").strip(), 
                    password=input("enter the password >>> ").strip()
                )
            else:
                print("Invalid command")

        if user_manager.user != None:
            if com == "logout":
                user_manager.logout()
            # elif com == "buy":
            #     user_manager.buy_ticket(list_of_futures)
            # elif com == "sell":
            #     user_manager.sell_ticket(list_of_futures)
            else:
                print("Invalid command")
    else:
        break