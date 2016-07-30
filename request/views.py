from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from request.models import Data
from request.serializers import DataSerializer
from datetime import date, timedelta
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render


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


class BaseView(ListView):
    """Displaying apods on main page"""
    model = Data
    template_name = 'base.html'
    context_object_name = 'main'

    def get_queryset(self):
        lte = Data.objects.dates('date', 'day', order='DESC')[0]
        gte = lte - timedelta(2)
        return Data.objects.filter(date__lte=lte).filter(date__gte=gte).order_by('-date')


class ArchiveView(ListView):
    """Displaying all apods in archive"""
    model = Data
    template_name = 'request/archive.html'
    context_object_name = 'archive'

    def get_queryset(self):
        return Data.objects.order_by('-date')

def listing(request):
    apods_list = Data.objects.all()
    paginator = Paginator(apods_list, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        apods = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        apods = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        apods = paginator.page(paginator.num_pages)

    return render(request, 'request/archive.html', {'apods': apods})
