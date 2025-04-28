import csv

from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render


def bus_stations(request):
    page_number = request.GET.get("page", 1)
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        stations = list(reader)
        paginator = Paginator(stations, 10) # 10 станций на страницу
        page = paginator.get_page(page_number)

    context = {
         'page': page,
    }
    return render(request, 'stations/index.html', context)