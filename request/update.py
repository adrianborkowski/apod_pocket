from time import sleep
from threading import Timer
from urllib import error, request
from .models import Data
from datetime import date, datetime, timedelta
from apod_pocket.settings import URL


def new():
    """
    This function check in every 15 minutes if newest apod is available
    and download it to database if it does not exists.
    """
    current_date = date.today()
    latest_date = Data.objects.dates('date', 'day').order_by('-date')[0]
    delta = (current_date - latest_date).days
    if delta == 0:
        print(datetime.now(), ": Apod from {date} already exists.".format(date=current_date))
    else:
        day = latest_date + timedelta(days=1)
        for i in range(delta):
            try:
                d = eval(request.urlopen(URL.format(date=day)).read().decode("utf-8"))
            except error.HTTPError as err:
                print(datetime.now(), ': {0}'.format(err))
                Timer(900, new).start()
            Data.objects.create(title=d.get('title'),
                                date=d.get('date'),
                                url=d.get('url'),
                                hd_url=d.get('hdurl'),
                                copyright=d.get('copyright'),
                                type=d.get('media_type'),
                                explanation=d.get('explanation'),)
            print("{datetime}: Successfully added {type} '{title}' from {date}.".format(datetime=datetime.now(),
                                                                                        type=d['media_type'],
                                                                                        title=d['title'],
                                                                                        date=day))
            day = day + timedelta(days=1)
            sleep(1)
    Timer(900, new).start()


def old():
    """
    This function allows dowload older apods by typing date and period.
    """
    print('APPENDING DATA TO DATABASE')
    date_entry = input('Enter a start date in YYYY-MM-DD format: ')
    year, month, day = map(int, date_entry.split('-'))
    day = date(year, month, day)
    period = int(input('Set number of days to add:'))

    for i in range(period):
        if Data.objects.filter(date=day).exists():
            print("{datetime}: Apod from {date} already exists.".format(datetime=datetime.now(), date=day))
            day = day - timedelta(days=1)
            sleep(1)
        else:
            try:
                d = eval(request.urlopen(URL.format(date=day)).read().decode("utf-8"))
            except error.HTTPError as err:
                print(datetime.now(), ': {0}'.format(err))
                day = day - timedelta(days=1)
                sleep(1)
                continue
            Data.objects.create(title=d.get('title'),
                                date=d.get('date'),
                                url=d.get('url'),
                                hd_url=d.get('hdurl'),
                                copyright=d.get('copyright'),
                                type=d.get('media_type'),
                                explanation=d.get('explanation'),)
            print("{datetime}: Successfully added {type} '{title}' from {date}.".format(datetime=datetime.now(),
                                                                                        type=d['media_type'],
                                                                                        title=d['title'],
                                                                                        date=day))
            day = day - timedelta(days=1)
            sleep(1)
    old()
