from django.core.management.base import BaseCommand
from playbills.models import Playbill
import requests
from bs4 import BeautifulSoup
from datetime import datetime

class Command(BaseCommand):
    help = 'Fetch playbills from gatob.kz'

    def handle(self, *args, **options):
        url = 'https://gatob.kz/#tab05_2024'  
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            playbill_items = soup.select('.tabs-items .tab-item .slide')
            if playbill_items:
                for item in playbill_items:
                    title_elem = item.select_one('.poster-prev')
                    date_elem = item.select_one('.date')
                    if title_elem and date_elem:
                        title = title_elem['href'].split('/')[-1]  
                        date_str = date_elem.text.split('-')[0].strip() 
                    try:
                        date_obj = datetime.strptime(date_str, '%d/%m')
                        date = date_obj.strftime('%Y-%m-%d') 
                    except ValueError:
                        self.stdout.write(self.style.ERROR(f'Invalid date format: {date_str}'))
                        continue
                    price = '0'  

                    Playbill.objects.create(title=title, date=date, price=price)
                    self.stdout.write(self.style.SUCCESS(f'Title: {title}, Date: {date}, Price: {price}'))

                self.stdout.write(self.style.SUCCESS('Successfully fetched playbills'))
            else:
                self.stdout.write(self.style.ERROR('No playbill items found'))
        else:
            self.stdout.write(self.style.ERROR('Failed to fetch playbills'))
