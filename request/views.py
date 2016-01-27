from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
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


@csrf_exempt
def data_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    jsons = Data.objects.all()
    serializer = DataSerializer(jsons, many=True)
    return JSONResponse(serializer.data)


<<<<<<< Updated upstream
@csrf_exempt
def data_detail(request, pk):
=======
def data_detail(request, date):
>>>>>>> Stashed changes
    """
    Retrieve, update or delete a code snippet.
    """
    try:
<<<<<<< Updated upstream
        j = Data.objects.get(pk=pk)
    except Data.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DataSerializer(j)
=======
        json = Data.objects.get(date=date)
        serializer = DataSerializer(json)
>>>>>>> Stashed changes
        return JSONResponse(serializer.data)
    except Data.DoesNotExist:
        return HttpResponse(status=404)
