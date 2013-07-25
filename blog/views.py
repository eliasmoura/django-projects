# -*- coding: utf8 -*-
# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.utils import simplejson
from django.shortcuts import get_object_or_404
from models import *

def home(request):
	#context = {'doencas': doencas, 'form':form, 'site': Site.objects.get_current().domain}
	npag = 0
	posts = Postagem.objects.all()
	sobre =get_object_or_404(Autor,nome='Elias')
	categoriasdb = Categoria.objects.all()
	subcategoriasdb = SubCategoria.objects.all()
	categorias = {}
	for categoria in categoriasdb:
		categorias[categoria.nome] = categoria
	postagens = []
	pag = 0
	if len(posts) > 6:
		pag = int(len(posts)/6)
		for post in posts[:6]:
			post.categorias = Post_Categorias.objects.filter(post=post.id)
			post.subcategorias = Post_SubCategorias.objects.filter(post=post.id)
			postagens.append(post)
	else:
		for post in posts[0:len(posts)]:
			post.categorias = Post_Categorias.objects.filter(post=post.id)
			post.subcategorias = Post_SubCategorias.objects.filter(post=post.id)
			postagens.append(post)

	sobre.conteudo = sobre.biografia
	context = {'posts': postagens,'sobre':sobre, 'categorias': categoriasdb
				, 'subcategorias': subcategoriasdb, 'npag':npag}
	return render_to_response('blog.html', context,
								context_instance=RequestContext(request))

def arquivo(request, year,month,day):
	npag = 0
	posts = Postagem.objects.filter(publicacao__year=year,
									publicacao__month=month,
									publicacao__day=day)
	sobre =get_object_or_404(Autor,nome='Elias')
	categoriasdb = Categoria.objects.all()
	subcategoriasdb = SubCategoria.objects.all()
	categorias = {}
	for categoria in categoriasdb:
		categorias[categoria.nome] = categoria
	postagens = []
	pag = 0
	if len(posts) > 6:
		pag = int(len(posts)/6)
		for post in posts[:6]:
			post.categorias = Post_Categorias.objects.filter(post=post.id)
			post.subcategorias = Post_SubCategorias.objects.filter(post=post.id)
			postagens.append(post)
	else:
		for post in posts[0:len(posts)]:
			post.categorias = Post_Categorias.objects.filter(post=post.id)
			post.subcategorias = Post_SubCategorias.objects.filter(post=post.id)
			postagens.append(post)

	sobre.conteudo = sobre.biografia
	context = {'posts': postagens,'sobre':sobre, 'categorias': categoriasdb
				, 'subcategorias': subcategoriasdb, 'npag':npag}
	return render_to_response('blog.html', context,
								context_instance=RequestContext(request))

def categorias(request):
	sobre = Autor.objects.get(nome='Elias')
	sobre.conteudo = sobre.biografia[0:31]
	context = {'post': post,'sobre':sobre}
	return render_to_response('blog.html', context,
								context_instance=RequestContext(request))

def categoria(request, slug):
	npag = 0
	posts = Postagem.objects.all()
	sobre =get_object_or_404(Autor,nome='Elias')
	categoriasdb = Categoria.objects.all()
	subcategoriasdb = SubCategoria.objects.all()
	categorias = {}
	for categoria in categoriasdb:
		categorias[categoria.nome] = categoria
	sobre.conteudo = sobre.biografia
	
	postagens = []
	try:
		categoria = get_object_or_404(Categoria,slug=slug)	
		posts = Post_Categorias.objects.filter(categoria=categoria.id)
		postagens = []
		for post in posts:
			postagens += Postagem.objects.filter(id=post.post.id)
	except Exception, e:
		pass
	try:
		subcategoria = SubCategoria.objects.get(slug=slug)
		posts = Post_SubCategorias.objects.filter(subcategoria=subcategoria.id)
		for post in posts:
			postagens += Postagem.objects.filter(id=post.post.id)
	except Exception, e:
		pass
	posts = postagens
	postagens = []
	if posts:
		if len(posts) > 6:
			npag = int(len(posts)/6)
			for post in posts[:6]:
				post.categorias = Post_Categorias.objects.filter(post=post.id)[:].categoria
				post.subcategorias = Post_SubCategorias.objects.filter(post=post.id)
				postagens.append(post)
		else:
			for post in posts[0:len(posts)]:
				post.categorias = Post_Categorias.objects.filter(post=post.id)
				post.subcategorias = Post_SubCategorias.objects.filter(post=post.id)
				postagens.append(post)
	post_categoria = {}
	for postagem in postagens:
		post_categoria[postagem.id] = Post_Categorias.objects.filter(post=postagem.id)
		post_categoria[postagem.id] = [post_categoria[postagem.id]] + [(Post_SubCategorias.objects.filter(post=postagem.id))]

	context = {'posts': postagens,'sobre':sobre, 'categorias': categoriasdb
				, 'subcategorias': subcategoriasdb, 
				'post_categoria':post_categoria, 'npag':npag}
	return render_to_response('blog.html', context,
								context_instance=RequestContext(request))

def postagem(request, slug):
	post = Postagem.objects.get(slug=slug)
	sobre = Autor.objects.get(nome='Elias')
	sobre.conteudo = sobre.biografia

	categoriasdb = Categoria.objects.all()
	subcategoriasdb = SubCategoria.objects.all()
	categorias = {}
	post.categorias = Post_Categorias.objects.filter(post=post.id)
	post.subcategorias = Post_SubCategorias.objects.filter(post=post.id)
	
	for categoria in categoriasdb:
		categorias[categoria.nome] = categoria

	context = {'post': post,'sobre':sobre,'categorias': categoriasdb
				, 'subcategorias': subcategoriasdb, }
	return render_to_response('blog.html', context,
								context_instance=RequestContext(request))

