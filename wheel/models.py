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

class Health(models.Model):
  points = models.IntegerField()
  
class Relationships(models.Model):
  points = models.IntegerField()

class Environment(models.Model):
  points = models.IntegerField()

class Vocation(models.Model):
  points = models.IntegerField()

class Prosperity(models.Model):
  points = models.IntegerField()

class SelfImprovement(models.Model):
  points = models.IntegerField()

class BrightnessOfLife(models.Model):
  points = models.IntegerField()

class Spirituality(models.Model):
  points = models.IntegerField()



class SubParagraphsHealth(models.Model):
  category = models.ForeignKey("Health", related_name='subparagraphsHealth', on_delete=models.CASCADE)
  subparagraphs = models.CharField(max_length=150, blank = True)

class SubParagraphsRelationships(models.Model):
  category = models.ForeignKey("Relationships", related_name='subparagraphsRelationships', on_delete=models.CASCADE)
  subparagraphs = models.CharField(max_length=150, blank = True)


class SubparagraphsEnvironment(models.Model):
  category = models.ForeignKey("Environment", related_name='subparagraphsEnvironment', on_delete=models.CASCADE)
  subparagraphs = models.CharField(max_length=150, blank = True)

class SubparagraphsVocation(models.Model):
  category = models.ForeignKey("Vocation", related_name='subparagraphsVocation', on_delete=models.CASCADE)
  subparagraphs = models.CharField(max_length=150, blank = True)


class SubparagraphsProsperity(models.Model):
  category = models.ForeignKey("Prosperity", related_name='subparagraphsProsperity', on_delete=models.CASCADE)
  subparagraphs = models.CharField(max_length=150, blank = True)


class SubparagraphsSelfImprovement(models.Model):
  category = models.ForeignKey("SelfImprovement", related_name='subparagraphsSelfImprovement', on_delete=models.CASCADE)
  subparagraphs = models.CharField(max_length=150, blank = True)


class SubparagraphsBrightnessOfLife(models.Model):
  category = models.ForeignKey("BrightnessOfLife", related_name='subparagraphsBrightnessOfLife', on_delete=models.CASCADE)
  subparagraphs = models.CharField(max_length=150, blank = True)


class SubparagraphsSpirituality(models.Model):
  category = models.ForeignKey("Spirituality", related_name='subparagraphsSpirituality', on_delete=models.CASCADE)
  subparagraphs = models.CharField(max_length=150, blank = True)


