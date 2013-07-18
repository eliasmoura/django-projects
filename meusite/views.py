# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.utils import simplejson

def home(request):
#	context = {'doencas': doencas, 'form':form, 'site': Site.objects.get_current().domain}
	context = {'dado': 'dados'}
	return render_to_response('home.html', context,
                              context_instance=RequestContext(request))