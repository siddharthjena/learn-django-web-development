from django.shortcuts import render
from .models import Table
# Create your views here.

def retrive_data(request):
    data = Table.objects.all()
    d = {'records': data}
    return render(request, 'IplTable/scoretable.html', d)

