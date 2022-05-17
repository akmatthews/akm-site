from django.db import models

class Education(models.Model):
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)

class PersonalSkill(models.Model):
    skill = models.CharField(max_length=500)
    percentage = models.DecimalField(decimal_places=2, max_digits=2)
    def percentage_as_int(self):
        return self.percentage * 100

class SoftwareSkill(models.Model):
    skill = models.CharField(max_length=500)
    percentage = models.DecimalField(decimal_places=2, max_digits=2)
    def percentage_as_int(self):
        return self.percentage * 100

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()