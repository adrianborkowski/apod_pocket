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
    def apod(a, b):
        try:
            json = Data.objects.order_by('-date')[a:b]
        except Data.DoesNotExist:
            return HttpResponse(status=404)
        serializer = DataSerializer(json, many=True)
        return JSONResponse(serializer.data)
    if limit is None and offset is None:
        return apod(0, 20)
    elif limit is not None and offset is None:
        return apod(0, int(limit))
    elif offset is not None and limit is None:
        return apod(int(offset), int(offset)+20)
    else:
        return apod(int(offset), int(offset)+int(limit))






