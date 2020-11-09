from django.db import models


class Location(models.Model):
    country = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.country} {self.country_code}"
