from .models import Data
from datetime import date, timedelta


def start():
    print('CHECKING IS DATA EXIST IN DATABASE')
    date_entry = input('Enter a start date in YYYY-MM-DD format: ')
    year, month, day = map(int, date_entry.split('-'))
    DATE = date(year, month, day)
    RANGE = int(input('Set number of days to check:'))
    for i in range(RANGE):
        qs = Data.objects.all()
        if qs.filter(date=DATE).exists():
            print('exist')
            DATE = DATE - timedelta(days=1)
        else:
            print(DATE)
            DATE = DATE - timedelta(days=1)
            continue
    start()
