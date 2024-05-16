import csv
import hashlib

class User:
    def __init__(self, username: str, password: str, id_: str):
        self.name: str = username
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.password: str =  hashed_password
        self.id_: str = id_
        self.tickets: list[str] = list()
        

    def save(self):
        with open('users.csv', 'r') as f:
            lines = f.readlines()

        updated_line = None
        for i, line in enumerate(lines):
            if line.startswith(str(self.id_)):
                tickets_str = ''
                for ticket in self.tickets:
                    tickets_str += f'{ticket}-'
                updated_line = f'{self.id_},{self.name},{self.password},{tickets_str}\n'
                lines[i] = updated_line
                break

        if updated_line is None:
            tickets_str = ''
            for ticket in self.tickets:
                tickets_str += f'{ticket}-'
            updated_line = f'{self.id_},{self.name},{self.password},{tickets_str}\n'
            lines.append(updated_line)

        with open('users.csv', 'w') as f:
            for line in lines:
                f.write(line)