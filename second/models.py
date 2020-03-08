from django.db import models

# Create your models here.

from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.template.defaultfilters import slugify

class School(models.Model):
    sch=models.CharField(max_length=50)
    schcode=models.CharField(max_length=20,default='school')

    def __str__(self):
        return self.sch

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

    class Meta:
        ordering = ["-date_posted"]


class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notice-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Notice, self).save(*args, **kwargs)

    
class Events(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('events-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Events, self).save(*args, **kwargs)


class Images(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.post.title + "Image"


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

class SID(models.Model):
    full_name = models.CharField(max_length=30)
    roll = models.IntegerField()
    childid = models.IntegerField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('registerchild')
    
    def save(self, *args, **kwargs):
        super(SID, self).save(*args, **kwargs)



class Attendance(models.Model):
    full_name = models.CharField(max_length=30)
    roll = models.IntegerField()
    childid = models.IntegerField()

    def __str__(self):
        return self.full_name

    @property
    def absentdayss(self):
        return self.absentday_set.count()

    @property
    def presentdayss(self):
        return self.presentday_set.count()

    @property
    def days(self):
        return self.absentday_set.all()

    def get_absolute_url(self):
        return reverse('attendance-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Attendance, self).save(*args, **kwargs)


class Food(models.Model):
    day = models.CharField(max_length=30, null=True)
    food = models.CharField(max_length=30, null=True)


    def __str__(self):
        return self.day


class Routine(models.Model):
    day = models.CharField(max_length=30)
    ten_ten45 = models.CharField(max_length=30)
    ten45_eleven30 = models.CharField(max_length=30)
    eleven45_twelve30 = models.CharField(max_length=30)
    twelve30_one15 = models.CharField(max_length=30)
    two_two45 = models.CharField(max_length=30)
    two45_three30 = models.CharField(max_length=30)

    def __str__(self):
        return self.day

    def get_absolute_url(self):
        return reverse('routine-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Routine, self).save(*args, **kwargs)


class Absentday(models.Model):
    name = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name.full_name + " A"


class Presentday(models.Model):
    name = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name.full_name + " P"


class Result(models.Model):
    name = models.ForeignKey(SID, on_delete=models.CASCADE)
    subject1 = models.DecimalField(max_digits=4, decimal_places=1)
    subject2 = models.DecimalField(max_digits=4, decimal_places=1)
    subject3 = models.DecimalField(max_digits=4, decimal_places=1)
    subject4 = models.DecimalField(max_digits=4, decimal_places=1)
    grade = models.CharField(max_length=2)
    remarks = models.TextField()

    def __str__(self):
        return self.name.full_name + "'s" + ' result '

    def get_absolute_url(self):
        return reverse('result-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Result, self).save(*args, **kwargs)
