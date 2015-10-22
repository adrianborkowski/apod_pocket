from urllib.request import urlopen
from .models import Data

    """
    komentarz sobie przeczytaj na dole, elo
    """

def present_json_to_db():

    url = 'https://api.nasa.gov/planetary/apod?concept_tags=True&date=2015-10-22&hd=True&api_key=DEMO_KEY'
    content = urlopen(url).read().decode("utf-8")
    d = eval(content)
    Data.objects.create(title=d['title'],
                        url=d['url'],
                        hd_url=d['hdurl'],
                        concepts=', '.join(d['concepts']),
                        explanation=d['explanation'],
                        media_type=d['media_type'])

present_json_to_db()

""" TO CONTINUE:
def past_json_to_db():
    date = '2015-10-22'
    past_url = 'https://api.nasa.gov/planetary/apod?concept_tags=True&date={date}&hd=True&api_key=DEMO_KEY'.format(date=date)
    content = urlopen(past_url).read().decode("utf-8")
    d = eval(content)
    Data.objects.create(title=d['title'],
                        url=d['url'],
                        concepts=', '.join(d['concepts']),
                        explanation=d['explanation'],
                        media_type=d['media_type'])

past_json_to_db()
"""
