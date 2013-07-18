# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.utils import simplejson
from models import Postagem

def home(request):
#	context = {'doencas': doencas, 'form':form, 'site': Site.objects.get_current().domain}
	context = {'dado': 'dados'}
	return render_to_response('blog.html', context,
								context_instance=RequestContext(request))

def categorias(request):
	
	context = {'dado': 'dados'}
	return render_to_response('blog.html', context,
								context_instance=RequestContext(request))
def categoria(request, categoria):
	
	context = {'dado': 'dados'}
	return render_to_response('blog.html', context,
								context_instance=RequestContext(request))

def postagem(request, post_titulo):
	post = Postagem.objetos.get(titulo=post_titulo)
	context = {'dado': 'dados'}
	return render_to_response('blog.html', context,
								context_instance=RequestContext(request))

