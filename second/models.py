from django.db import models

# Create your models here.

from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(upload_to='posts', blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)


class StudentId(models.Model):
    full_name = models.CharField(max_length=30)
    roll = models.IntegerField()
    childid = models.IntegerField()

    def __str__(self):
        return self.full_name


class Attendance(models.Model):
    full_name = models.CharField(max_length=30)
    roll = models.IntegerField()
    childid = models.IntegerField()
    present_days = models.IntegerField(default=0)
    absent_days = models.IntegerField(default=0)

    def __str__(self):
        return self.full_name
