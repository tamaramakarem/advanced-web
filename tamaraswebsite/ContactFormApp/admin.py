from django.contrib import admin
from ContactFormApp.models import Person, City, Country, House, Mayor


class PersonAdmin(admin.ModelAdmin):
 	list_display = ('first_name', 'last_name', 'address','zipcode','email','phone','subject','inquiry', 'email_exists', 'has_been_answered')

	
admin.site.register(Person, PersonAdmin)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(House)
admin.site.register(Mayor)
 