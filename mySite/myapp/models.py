from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class dateOfCleanup(models.Model):
    date = models.DateField()
    
    def __str__(self):
        return "Cleanup on {}".format(self.date)
    
class studentInformationModel(models.Model):
    name = models.CharField(max_length=200)
    idNum = models.IntegerField(validators=[MinValueValidator(1)])
    school = models.CharField(max_length=100)
    hours = models.IntegerField(validators=[MinValueValidator(1)])
    cleanup = models.ForeignKey(dateOfCleanup, on_delete=models.CASCADE,related_name='students', default=-1)

    def __str__(self):
        return self.name + " " + self.idNum + " " + self.school + " " + self.hours
