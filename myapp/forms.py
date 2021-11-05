from django.forms import ModelForm
from django import forms
from .models import Book
from .models import Person, City

BOOK_CHOICES= [
    ('prestado', 'No disponible'),
    ('disponible', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]

class BookForm(forms.Form):
        title= forms.CharField(max_length=100)
        description= forms.CharField(max_length=100)
        author= forms.CharField(max_length=100)
        #author= forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=BOOK_CHOICES))
        year= forms.IntegerField()

"""
class PersonForm(forms.Form):
        name = forms.CharField(max_length=100)
        birthdate = forms.CharField(max_length=100)
        country = forms.CharField(max_length=100)
        city = forms.CharField(max_length=100)
"""
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')        

