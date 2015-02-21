from django.db import models


class Marker(models.Model):
    name = models.CharField(max_length=255)
    lat = models.CharField(max_length=255)
    long = models.CharField(max_length=255)

    def to_dict(self):
        return {
            'name': self.name,
            'lat': self.lat,
            'long': self.long
        }