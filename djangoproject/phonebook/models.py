from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=16)

    def save(self, *args, **kwargs):
        # Check if the number does not already start with '+359'
        if not self.number.startswith('+359'):
            # Add the '+359' prefix
            self.number = '+359' + self.number
        super().save(*args, **kwargs)