from django.db import models


class Property(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    notes = models.TextField()
    viewing = models.DateTimeField()

    class Meta:
        ordering = ('viewing',)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'marker_colour': 'red'
        }

