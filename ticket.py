class Ticket:
    def __init__(self, title, date, link, id_):
        self.title: str = title
        self.date: list = date
        self.ticket_id: int = id_
        self.link: str = link
        self.qr_code = None

    def __str__(self):
        return f'{self.ticket_id},{self.title},{self.date},{self.link}'