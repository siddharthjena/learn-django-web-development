from django.shortcuts import render,HttpResponseRedirect
from .models import RedgModel
from .forms import RedgForm

# Create your views here.
def redg_view(request):
    if request.method == 'POST':
        form = RedgForm(request.POST)
        if form.is_valid():
            form.save()
            data = RedgModel.objects.all()
            d = {'data' : data}
            return render(request, 'FormApp/all_records.html',d)
    else:
        form = RedgForm()
        d = {'form' : form}
        return render(request,'FormApp/redg.html',d )