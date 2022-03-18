from django.db import models

class DateFilter(models.Model):
    date = models.DateField()
    def __str__(self):
        return self.date.strftime("%d/%m/%Y")