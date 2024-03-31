from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class List_of_Dream(models.Model):
    #adicionado
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    #
    dream = models.CharField(max_length=200, default='', blank=True)
    schedule = models.DurationField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return (f"{self.dream}")
       
class Steps_to_Concretize(models.Model):
    dream = models.ForeignKey(List_of_Dream, on_delete=models.CASCADE, default='')
    description = models.CharField(max_length=500, default='', blank=True)
    time_line = models.DurationField()
    step_done = models.BooleanField(default=False)
    
    def __str__(self):
        return (f"{self.description}")
    
    
