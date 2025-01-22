from django.db import models

class Route(models.Model):
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return f"{self.source} to {self.destination}"

class Booking(models.Model):
    user = models.CharField(max_length=100)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Booking by {self.user} for {self.route}"