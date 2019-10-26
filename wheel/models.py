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



class ToDoHealth(models.Model):
  toDo = models.CharField(max_length=150, blank = True)

class ToDoRelationships(models.Model):
  toDo = models.CharField(max_length=150, blank = True)


class ToDoEnvironment(models.Model):
  toDo = models.CharField(max_length=150, blank = True)


class ToDoVocation(models.Model):
  toDo = models.CharField(max_length=150, blank = True)


class ToDoProsperity(models.Model):
  toDo = models.CharField(max_length=150, blank = True)


class ToDoSelfImprovement(models.Model):
  toDo = models.CharField(max_length=150, blank = True)


class ToDoBrightnessOfLife(models.Model):
  toDo = models.CharField(max_length=150, blank = True)


class ToDoSpirituality(models.Model):
  toDo = models.CharField(max_length=150, blank = True)


