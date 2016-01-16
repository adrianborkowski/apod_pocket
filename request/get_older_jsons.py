from urllib.request import urlopen
from .models import Data
from datetime import date, timedelta
from apod_pocket.settings import URL


print('APPENDING DATA TO DATABASE')
date_entry = input('Enter a date in YYYY-MM-DD format: ')
year, month, day = map(int, date_entry.split('-'))
DATE = date(year, month, day)
RANGE = int(input('Set number of days to add:'))

for i in range(RANGE):  # HOW MANY DAYS ADD (SINCE DATE FROM VAR. DATE TO PAST)
    d = eval(urlopen(URL.format(date=DATE)).read().decode("utf-8"))
    qs = Data.objects.all()
    if qs.filter(title=d['title']).exists():  # CHECKING IF LAST DATA TITLE IN DB IS THE SAME AS LAST JSON'S TITLE.
        print("Data {type} '{title}' already exists.".format(type=d['media_type'], title=d['title']))
        DATE = DATE - timedelta(days=1)  # SUBTRACTING DATE, days - NUMBER OF DAYS TO SUBTRACT
    else:
        Data.objects.create(title=d.get('title'),  # ADDING DATA TO DB
                            date=d.get('date'),
                            url=d.get('url'),
                            hd_url=d.get('hdurl'),
                            copyright=d.get('copyright'),
                            type=d.get('media_type'),
                            explanation=d.get('explanation'),
                            )
        print("Successfully added {type} '{title}' from {date}.".format(type=d['media_type'], title=d['title'], date=DATE))
        DATE = DATE - timedelta(days=1)
