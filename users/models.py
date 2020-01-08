from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class User_parents(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    ChildID=models.IntegerField()
    ChildGrade=models.IntegerField()
    occupation = models.CharField(max_length=200)
    ChildName=models.CharField(max_length=200)
    RelationToChild=models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

    

class User_teachers(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    age=models.IntegerField()
    grade=models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

    

