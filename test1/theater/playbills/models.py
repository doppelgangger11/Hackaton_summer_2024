from django.contrib.auth.models import User
from django.db import models

class Playbill(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='playbill_images/', default='')

    def __str__(self):
        return self.title

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    playbill = models.ForeignKey(Playbill, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    seat_number = models.CharField(max_length=10, null=True)
    row_number = models.IntegerField(null=True)
    is_confirmed = models.BooleanField(default=False) 

    def __str__(self):
        return f'{self.user.username} - {self.playbill.title}'
