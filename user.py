import csv
import hashlib
import uuid


class User:
    def __init__(self, username, password):
        self.name = username
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.password =  hashed_password
        self.ID = str(uuid.uuid4())
        self.tickets = list()
        

    def save(self):
        with open('users.csv', 'r') as f:
            lines = f.readlines()

        updated_line = None
        for i, line in enumerate(lines):
            if line.startswith(str(self.ID)):
                tickets_str = ''
                for ticket in self.tickets:
                    tickets_str += f'{ticket}-'
                updated_line = f'{self.ID},{self.name},{self.password},{tickets_str}\n'
                lines[i] = updated_line
                break

        if updated_line is None:
            tickets_str = ''
            for ticket in self.tickets:
                tickets_str += f'{ticket}-'
            updated_line = f'{self.ID},{self.name},{self.password},{tickets_str}\n'
            lines.append(updated_line)

        with open('users.csv', 'w') as f:
            for line in lines:
                f.write(line)