from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from request.models import Data
from request.serializers import DataSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def data_list(request):
    """
    List all jsons.
    """
    if request.method == 'GET':
        j = Data.objects.all()
        serializer = DataSerializer(j, many=True)
        return JSONResponse(serializer.data)


def data_detail(request, pk):
    """
    Retrieve json.
    """
    try:
        json = Data.objects.get(pk=pk)
    except Data.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DataSerializer(json)
        return JSONResponse(serializer.data)
