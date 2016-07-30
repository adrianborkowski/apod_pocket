from time import sleep
from threading import Timer
from urllib import error, request
from .models import Data
from datetime import date, datetime, timedelta
from apod_pocket.settings import URL


def new():
    """Function check in every 15 minutes if newest apod is available and save it in database if it doest not exists"""
    try:
        d = eval(request.urlopen(URL.format(date=date.today())).read().decode("utf-8"))
    except error.HTTPError:
        print(datetime.now(), ': {0}'.format(error))
    qs = Data.objects.all()
    if qs.filter(date=d['date']).exists():
        print(datetime.now(), ": Apod from {date} already exists.".format(date=d['date']))
    else:
        Data.objects.create(title=d.get('title'),
                            date=d.get('date'),
                            url=d.get('url'),
                            hd_url=d.get('hdurl'),
                            copyright=d.get('copyright'),
                            type=d.get('media_type'),
                            explanation=d.get('explanation'),)
        print(datetime.now(), ": Successfully added {type} '{title}'.".format(type=d['media_type'], title=d['title']))
    Timer(900, new).start()


def old():
    """Function allows save older apods by typing date and range"""
    print('APPENDING DATA TO DATABASE')
    date_entry = input('Enter a date in YYYY-MM-DD format: ')
    year, month, day = map(int, date_entry.split('-'))
    DATE = date(year, month, day)
    RANGE = int(input('Set number of days to add:'))

    for i in range(RANGE):
        if Data.objects.filter(date=DATE).exists():
            print(datetime.now(), ": Apod from {date} already exists.".format(date=DATE))
            DATE = DATE - timedelta(days=1)
        else:
            try:
                d = eval(request.urlopen(URL.format(date=DATE)).read().decode("utf-8"))
            except error.HTTPError as err:
                print(datetime.now(), ': {0}'.format(err))
                DATE = DATE - timedelta(days=1)
                sleep(1)
                continue
            Data.objects.create(title=d.get('title'),
                                date=d.get('date'),
                                url=d.get('url'),
                                hd_url=d.get('hdurl'),
                                copyright=d.get('copyright'),
                                type=d.get('media_type'),
                                explanation=d.get('explanation'),)
            print(datetime.now(), ": Successfully added Apod from {date}.".format(date=DATE))
            DATE = DATE - timedelta(days=1)
        sleep(1)
    old()
