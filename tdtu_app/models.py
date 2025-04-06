from django.db import models

class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="news/")
    date = models.DateTimeField(auto_now_add=True)

    for_telegram = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save_news(self):
        print(self.image)
        self.save()



class Invites(models.Model):
    full_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.full_name

class Students(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="students/")
    content = models.TextField()

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Department(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="departments/")
    content = models.TextField()

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Banners(models.Model):
    image = models.ImageField(upload_to="banners/")
    is_public = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.is_public)

class Statistical(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=120)
    year = models.IntegerField(default=0)
    is_now = models.BooleanField(default=False)

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Partner(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="partners/")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AboutVideo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    video = models.FileField(upload_to="videos/")

    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Team(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name