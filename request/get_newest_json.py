from urllib.request import urlopen
from .models import Data
from datetime import date

URL = 'https://api.nasa.gov/planetary/apod?concept_tags=True&hd=True&api_key=DEMO_KEY'

d = eval(urlopen(URL).read().decode("utf-8"))  # CREATING DICTIONARY WHICH INCLUDE CONTENT OF URL (JSON).
qs = Data.objects.all()
if qs.filter(title=d['title']).exists():  # CHECKING IF LAST DATA TITLE IN DB IS THE SAME AS LAST JSON'S TITLE.
    print("Data {type} '{title}' already exists.".format(type=d['media_type'], title=d['title']))
else:
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
                        created_date=date.today())
    print("Successfully added {type} '{title}'.".format(type=d['media_type'], title=d['title']))
