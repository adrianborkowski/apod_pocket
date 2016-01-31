from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from request.models import Data
from request.serializers import DataSerializer
from datetime import date, timedelta


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def data_detail(request, limit=None, offset=None):
    """
    Retrieve json.
    """
    def apod(first_day, last_day):
        try:
            json = Data.objects.filter(date__lte=first_day).filter(date__gte=last_day)
        except Data.DoesNotExist:
            return HttpResponse(status=404)
        serializer = DataSerializer(json, many=True)
        return JSONResponse(serializer.data)
    if limit and offset is None:
        day = date.today()
        return apod(day, day - timedelta(19))
    elif limit is not None and offset is None:
        day = date.today()
        return apod(day, day - timedelta(days=int(limit)-1))
    elif offset is not None and limit is None:
        day = date.today() - timedelta(days=int(offset))
        return apod(day, day - timedelta(19))
    else:
        day = date.today() - timedelta(days=int(offset))
        return apod(day, day - timedelta(days=int(limit)-1))






