from django.db import models
import datetime
import csv
from django.utils import timezone

class WeatherSubscription(models.Model):
    email = models.EmailField(unique=True)
    city_choices = []
    with open('util/cities.csv') as csvfile:
        city_input = csv.reader(csvfile)
        next(city_input) # flush header line
        for i in range(0, 100):
            l = next(city_input)
            city_choices.append((str(l[1]) + "," + str(l[2]), 
                                 str(l[1]) + ", " + str(l[2])))
    
    city_choices = tuple([('', 'Select nearest city...')] + sorted(city_choices))
    
    location = models.CharField(max_length=100, choices=city_choices)
    
    def __str__(self):
        return str(self.email) + ' in ' + str(self.location)