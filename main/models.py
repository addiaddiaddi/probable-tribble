from django.db import models

# Create your models here.
class Team(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=40)

    points = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.name}"

class Player(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)

    points = models.IntegerField(default=0)

    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)

    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Category(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=40)

    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} | {self.points} points"

class Entry(models.Model):
    id = models.AutoField(primary_key=True)

    category  = models.ForeignKey(Category, on_delete=models.CASCADE)


    time = models.TimeField(auto_now=True)
    date = models.DateTimeField(auto_now_add=True)
    date.editable=True
    time.editable=True
    # player = models.OneToOneField(
    #     Player,
    #     on_delete=models.CASCADE,
    #     primary_key=True,
    #     default=None
    # )

    player = models.ForeignKey(Player, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.category} by {self.player}"
