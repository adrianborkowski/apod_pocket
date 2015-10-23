from urllib.request import urlopen
from .models import Data

URL = 'https://api.nasa.gov/planetary/apod?concept_tags=True&hd=True&api_key=DEMO_KEY'


def get():
    content = urlopen(URL).read().decode("utf-8")
    d = eval(content)
    Data.objects.create(title=d['title'],  # ADDING DATA TO DB
                        url=d['url'],
                        hd_url=d['hdurl'],
                        concepts=', '.join(d['concepts']),
                        explanation=d['explanation'],
                        media_type=d['media_type'])

get()
