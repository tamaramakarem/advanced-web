from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.sites.models import get_current_site
from django.shortcuts import redirect
from forms import PersonForm, PersonCityFormSet, PersonCountryFormSet
from django.core.mail import send_mail
from  admin import PersonAdmin
from django.forms.models import inlineformset_factory
from models import  Person, Country, City, Mayor, House
from django.views.generic import *

class home(TemplateView):
	template_name = "home.html"

class contactus(CreateView):
	template_name = "ContactForm/contactus.html"
	model = Person
	form_class = PersonForm
	success_url = 'thankyou/'

	def form_valid(self, form):
		context = self.get_context_data()
		Country_form = context['Country_formset']
		City_form = context['City_formset']
		if Country_form.is_valid() and City_form.is_valid():
			self.object = form.save()
			Country_form.instance = self.object
			Country_form.save()
			City_form.instance = self.object
			City_form.save()
			return HttpResponseRedirect('thankyou/')
		else:
			return self.render_to_response(self.get_context_data(form=form))
			
	def form_invalid(self, form):
		return self.render_to_response(self.get_context_data(form=form))
		
	def get_context_data(self, **kwargs):
		context = super(contactus, self).get_context_data(**kwargs)
		if self.request.POST:
			context['Country_form'] = PersonCountryFormSet(self.request.POST)
			context['City_form'] = PersonCityFormSet(self.request.POST)
		else:
			context['Country_form'] = PersonCountryFormSet()
			context['City_form'] = PersonCityFormSet()
		return context
		
class thankyou(TemplateView):
	template_name = "ContactForm/thankyou.html"
	