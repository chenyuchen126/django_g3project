from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from textflow.models import FlowObject

urlpatterns = [
#	url(r'^$',views.index, name='index'),
	url(r'^index/',views.index, name='index'),
        url(r'about/(.*?)$',views.about, name='about'),	    
	#url(r'^result/',views.result, name='result'),	    
	url(r'^classification/',views.classification, name='classification'),	    
#	url(r'^gul/',views.gullist, name='gullist'),	    
	url(r'^gul/',views.gul, name='gul'),	    
	url(r'^guasb/',views.guasb, name='guasb'),	    
	url(r'^result',views.result, name='result'),	    
	#url(r'^result/(.*?)$',views.getlist, name='getlist'),	    
#	url(r'^result/',views.gullist, name='gullist'),	    
	
        url(r'^meta/',views.meta, name='meta'),	    
]



