from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

TIMES = (
    ('M', 'Morning'),
    ('N', 'Noon'),
    ('E', 'Evening')
)

# Create your models here.
class Pot(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pot-detail', kwargs={'pk': self.id})
    


class Flower(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    pots = models.ManyToManyField(Pot)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("flower-detail", kwargs={"flower_id": self.id})
    



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
    
    class Meta:
        ordering = ['-date'] 



