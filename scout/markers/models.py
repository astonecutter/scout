from django.db import models
from model_utils import Choices


MARKER_COLOURS = Choices(
    ('blue', 'Blue'),
    ('red', 'Red')
)


class Marker(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True)
    lat = models.CharField(max_length=255, blank=True)
    long = models.CharField(max_length=255, blank=True)
    marker_colour = models.CharField(max_length=10, choices=MARKER_COLOURS, default=MARKER_COLOURS.blue)

    def to_dict(self):
        return {
            'name': self.name,
            'lat': self.lat,
            'long': self.long,
            'address': self.address,
            'marker_colour': self.marker_colour
        }