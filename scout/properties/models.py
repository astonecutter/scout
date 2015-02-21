from django.db import models


class Property(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def to_dict(self):
        return {
            'name': self.name,
            'address': self.address
        }

