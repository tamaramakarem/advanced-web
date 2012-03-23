from django.conf.urls.defaults import *
from django.conf import settings
from ContactFormApp.views import *

urlpatterns = patterns('',    
    url(r'^contactus/$', contactus.as_view(), name='contactus'),
    url(r'^thankyou/$', thankyou.as_view(), name='thankyou'),
    
)
