from ticket import Ticket
import hashlib

class User:
    def __init__(self, username: str, password: str, id_: str):
        self.username: str = username
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.password: str =  hashed_password
        self.id_: str = id_
        self.tickets: list = []

    def add_ticket(self, ticket: Ticket):
        self.tickets.append(ticket)

    def save(self):
        with open('users.csv', 'r') as f:
            lines = f.readlines()

        updated_line_index = None
        for i, line in enumerate(lines):
            if line.startswith(str(self.id_)):
                tickets_str = ''
                for ticket in self.tickets:
                    tickets_str += f'{ticket.ticket_id}-'
                updated_line = f'{self.id_},{self.username},{self.password},{tickets_str}\n'
                lines[i] = updated_line
                updated_line_index = i  # Запоминаем индекс обновленной строки
                break

        if updated_line_index is None:
            tickets_str = ''
            for ticket in self.tickets:
                tickets_str += f'{ticket.ticket_id}-'
            new_line = f'{self.id_},{self.username},{self.password},{tickets_str}\n'
            lines.append(new_line)

        with open('users.csv', 'w') as f:
            for line in lines:
                f.write(line)
