from django.forms import ModelForm
from models import Person, City, Country, House, Mayor

from django.contrib.localflavor.us.us_states import STATE_CHOICES
from django import forms
from django.contrib.localflavor.us.forms import USStateField
from django.forms.models import inlineformset_factory


class PersonForm(ModelForm):
	class Meta:
		model = Person

#PersonCountryFormSet = inlineformset_factory(Person, Country, extra=2)
#PersonCityFormSet = inlineformset_factory(Person, City, extra=5)



