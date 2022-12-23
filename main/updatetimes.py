import datetime
from .models import Entry

def update():
    for entry in Entry.objects.all():

        today = datetime.date(2021,1,14)
        etime = entry.time


        sixhr = datetime.time(6,0,0)
        begin = datetime.date(1,1,1)
        newdate = datetime.datetime.combine(today,etime)
        print('newdate', newdate)
        sixhr = datetime.datetime.combine(begin,sixhr)
        print('sixhr', sixhr)

        combined = newdate - sixhr

        print('type',type(combined))
        print('combined',combined)

        newcomb = datetime.datetime(1,1,1,0,0,0) + combined

        print('typecomb', type(newcomb))
        print('newcomb', newcomb)
        entry.date = newcomb
        entry.save()
