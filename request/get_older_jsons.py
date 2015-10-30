from urllib.request import urlopen
from .models import Data
from datetime import date, timedelta

DATE = date(2015, 10, 27)  # DATE OF BEGIN ADDING JSONS' DATA TO DB(YYYY, MM, DD)

for i in range(2):  # HOW MANY DAYS ADD (SINCE DATE FROM VAR. DATE TO PAST)
    past_url = 'https://api.nasa.gov/planetary/apod?concept_tags=True' \
               '&date={date}' \
               '&hd=True' \
               '&api_key=DEMO_KEY'.format(date=DATE)
    content = urlopen(past_url).read().decode("utf-8")
    d = eval(content)
    if 'hdurl' not in d:
        hd_url = ''
    else:
        hd_url = d['hdurl']
    Data.objects.create(title=d['title'],  # ADDING DATA TO DB
                        url=d['url'],
                        hd_url=hd_url,
                        concepts=', '.join(d['concepts']),
                        explanation=d['explanation'],
                        media_type=d['media_type'],
                        created_date=DATE)
    DATE = DATE - timedelta(days=1)  # SUBTRACTING DATE, days-NUMBER OF DAYS TO SUBTRACT
    print("Successfully added '{}'".format(d['title']))