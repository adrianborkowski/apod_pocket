from .models import Data
from datetime import date, timedelta


def start():
    date_entry = input('Enter a date in YYYY-MM-DD format: ')
    year, month, day = map(int, date_entry.split('-'))
    DATE = date(year, month, day)
    for i in range(20):
        qs = Data.objects.all()
        if qs.filter(date=DATE).exists():
            print(DATE)
            DATE = DATE - timedelta(days=1)
            continue
        else:
            print("exist")
            DATE = DATE - timedelta(days=1)
