from django import forms

class Emp_reg_form(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    company = forms.CharField()
    sal = forms.FloatField()