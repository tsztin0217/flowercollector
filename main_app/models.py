from django.db import models
from django.urls import reverse

TIMES = (
    ('M', 'Morning'),
    ('N', 'Noon'),
    ('E', 'Evening')
)

# Create your models here.
class Flower(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("flower_detail", kwargs={"flower_id": self.id})
    


class Watering(models.Model):
    date = models.DateField('Watering date')
    time = models.CharField(
        max_length=1,
        choices=TIMES,
        default=TIMES[0][0]
    )
    
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_time_display()} on {self.date}"
