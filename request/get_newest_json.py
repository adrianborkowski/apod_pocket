from urllib import request, error
from .models import Data
from datetime import date, datetime
from apod_pocket.settings import URL


try:
    d = eval(request.urlopen(URL.format(date=date.today())).read().decode("utf-8"))
    # CREATING DICTIONARY WHICH INCLUDE CONTENT OF URL (JSON).
except error.HTTPError:
    com = 'Internal Service Error: No Apod from {date}!!!'.format(date=date.today())
    print(com)
    w = str(datetime.now())+': '+com+'\n'
    with open('logs', 'a') as f:
        f.write(w)
        f.close()

qs = Data.objects.all()
if qs.filter(title=d['title']).exists():  # CHECKING IF LAST DATA TITLE IN DB IS THE SAME AS LAST JSON'S TITLE.
    print("Data {type} '{title}' already exists.".format(type=d['media_type'], title=d['title']))
else:
    Data.objects.create(title=d.get('title'),  # ADDING DATA TO DB
                        date=d.get('date'),
                        url=d.get('url'),
                        hd_url=d.get('hdurl'),
                        copyright=d.get('copyright'),
                        type=d.get('media_type'),
                        explanation=d.get('explanation'),
                        )
    print("Successfully added {type} '{title}'.".format(type=d['media_type'], title=d['title']))
