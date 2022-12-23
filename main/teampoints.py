from .models import *

def update():
    for team in Team.objects.all():
        points = 0
        for p in Player.objects.filter(team=team):
            points += p.points

        team.points = points
        print(team.name, ' ', team.points)
        team.save()
