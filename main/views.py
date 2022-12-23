from django.shortcuts import render
from main.models import *
from django.http import HttpResponseRedirect
from django import forms
import datetime

# Create your views here
def index(request):
    players = Player.objects.all().order_by('-points')
    print(players)
    return render(request, "leaderboard.html", {
        "players": players,
        "teams": Team.objects.all().order_by('-points'),
        })

def login(request):
    if request.session.has_key('username'):
        players = Player.objects.all().order_by('-points')
        return render(request, "leaderboard.html", {
            "players": players,
            "teams": Team.objects.all().order_by('-points'),
            'error': "You are already logged in"
            })
    if request.method == "POST":
        form = request.POST
        username = form['username']
        password = form['password']
        check = Player.objects.filter(username=username,password=password).count()

        print(check)
        if check == 1:
            request.session['username'] = username

            return render(request, "leaderboard.html", {
                "players": Player.objects.all().order_by('-points'),
                "teams": Team.objects.all().order_by('-points'),
                'success': f"You have successfully signed in as {username}",
                })
        else:
            return render(request, "login.html", {
                'error': "Either your username or password is incorrect",
                })
    return render(request, "login.html")

def submit(request):
    # message = None
    # if request.session.has_key('username') == False:
    #     return render(request, "login.html", {
    #         'error': "You need to log in",
    #         })
    # if request.method == "POST":
    #     form = request.POST
    #     id = form['entry']
    #     if id == '0':
    #         return render(request, "submit.html", {
    #             "categories": Category.objects.all(),
    #             'error': "Please pick something",
    #         })
    #     category = Category.objects.filter(id=id).first()
    #     player = Player.objects.filter(username=request.session['username']).first()
    #     entry = Entry(category=category, player=player)

    #     player.points += category.points
    #     entry.save()

    #     today = datetime.date.today()
    #     etime = entry.time

    #     sixhr = datetime.time(6,0,0)
    #     begin = datetime.date(1,1,1)

    #     newdate = datetime.datetime.combine(today,etime)
    #     sixhr = datetime.datetime.combine(begin,sixhr)

    #     comb = newdate - sixhr

    #     newcomb = datetime.datetime(1,1,1,0,0,0) + comb
    #     entry.date = newcomb
    #     print(entry)
    #     entry.save()
    #     player.save()

    #     message = f"Successfully saved your entry for '{category.name}'"

    # return render(request, "submit.html", {
    #     "categories": Category.objects.all(),
    #     'success': message,
    # })
    return render(request, "leaderboard.html", {
        "players": Player.objects.all().order_by('-points'),
        "teams": Team.objects.all().order_by('-points'),
        "error": "Submissions are closed since practice has resumed"
        })
def signup(request):
    if request.method == "POST":
        form = request.POST
        print(form)
        firstname = form['firstname'].rstrip()
        lastname = form['lastname'].rstrip()
        team = int(form['team'])
        username = form['username'].rstrip()
        password = form['password'].rstrip()
        print(team)
        if team == 0:
            return render(request, "signup.html", {
                'teams': Team.objects.all(),
                'error': "Team can't be empty, please try again."
            })
        team = Team.objects.get(id=team)
        check = Player.objects.filter(username=username).count()


        if check != 0:
            return render(request, "signup.html", {
                'teams': Team.objects.all(),
                'error': "Username taken, please try again."
            })
        if username == '':
            return render(request, "signup.html", {
                'teams': Team.objects.all(),
                'error': "Username can't be empty, please try again."
            })
        if password == '':
            return render(request, "signup.html", {
                'teams': Team.objects.all(),
                'error': "Password can't be empty, please try again."
            })
        if lastname == '':
            return render(request, "signup.html", {
                'teams': Team.objects.all(),
                'error': "Last name can't be empty, please try again."
            })
        if firstname == '':
            return render(request, "signup.html", {
                'teams': Team.objects.all(),
                'error': "First name can't be empty, please try again."
            })

        request.session['username'] = username
        newplayer = Player(firstname=firstname, lastname=lastname,username=username,password=password,team=team)
        newplayer.save()

        return render(request, "leaderboard.html", {
            'players': Player.objects.all(),
            'teams': Team.objects.all(),
            'success': "Successfully created account and signed in",
        })


    return render(request, "signup.html", {
        'teams': Team.objects.all(),
    })

def playerProfile(request, id):
    print(id)

    player = Player.objects.filter(id=id).first()

    print(player)
    entries = Entry.objects.filter(player=player).all()
    #
    print(entries)
    return render(request, "playerProfile.html", {
        'name': 'Profile of ' + player.firstname + ' ' + player.lastname,
        'entries': entries
    })


def logout(request):
    if request.session.has_key('username'):
        del request.session['username']
    players = Player.objects.all().order_by('-points')
    return render(request, "leaderboard.html", {
        "players": players,
        "teams": Team.objects.all().order_by('-points'),
        'success': "Successfully logged out",
        })
