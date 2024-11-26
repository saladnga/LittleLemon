from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=255)
    number_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.name} for {self.number_of_guests} guests on {self.booking_date}"


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.title} : {str(self.price)}"
