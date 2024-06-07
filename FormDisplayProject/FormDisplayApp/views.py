from django.shortcuts import render
from .forms import Emp_reg_form

# Create your views here.
def Emp_reg_view(request):
    f = Emp_reg_form()
    
    d = {'form':f}

    if request.method == 'POST':
        f = Emp_reg_form(request.POST)
        if f.is_valid():
            name = f.cleaned_data['name']
            age = f.cleaned_data['age']
            company = f.cleaned_data['company']
            sal = f.cleaned_data['sal']

            d = {'name':name, 'age':age, 'company':company, 'sal':sal}

            return render(request, 'FormDisplayApp/data.html',d)
    return render(request,'FormDisplayApp/home.html', d)