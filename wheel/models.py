from django.db import models

class Author(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()

  def __str__(self):
        return self.name

class Wheel(models.Model):
    health = models.IntegerField()
    relationships = models.IntegerField()
    environment = models.IntegerField()
    vocation = models.IntegerField()
    prosperity = models.IntegerField()
    selfImprovement = models.IntegerField()
    brightnessOfLife = models.IntegerField()
    spirituality = models.IntegerField()
    author = models.ForeignKey('Author', related_name='wheel', on_delete=models.CASCADE)
