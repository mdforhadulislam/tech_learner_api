from django.db import models


class Session(models.Model):
    years = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.years


class Tag(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    name_bn = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class TeamProfile(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(
        upload_to='landing/about/', blank=True, null=True)

    def __str__(self):
        return f'Name: {self.name} - Title: {self.title}'


class About(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    titleBn = models.CharField(max_length=100, blank=True, null=True)
    descriptionBn = models.TextField(blank=True, null=True)
    image_banar = models.ImageField(
        upload_to='landing/about/', blank=True, null=True)
    title2 = models.CharField(max_length=100, blank=True, null=True)
    description2 = models.TextField(blank=True, null=True)
    team_section = models.ManyToManyField(TeamProfile, blank=True)

    def __str__(self):
        return f'Title: {self.title}'


class FrequentlyAskedQuestions(models.Model):
    question = models.CharField(max_length=150, blank=True, null=True)
    answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Question: {self.question}'


class HelpAbout(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    titleBn = models.CharField(max_length=50, blank=True, null=True)
    descriptionBn = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'Title: {self.title} - Location: {self.location} - Number: {self.number} - Email: {self.email}'


class HelpContact(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    number = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Name: {self.name} - Number: {self.number} - Email: {self.email}'
