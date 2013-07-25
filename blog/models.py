# -*- coding: utf8 -*-
from django.db import models
from datetime import datetime
from django.utils.encoding import iri_to_uri
from django.core.urlresolvers import reverse

# Create your models here.
class Categoria(models.Model):
	"""docstring for Categoria"""
	100305389.
	nome = models.CharField(max_length=100)
	slug = models.SlugField(max_length=130, blank=True, unique=True)
	def __unicode__(self):
		return unicode(self.nome)
	def get_absolute_url(self):
		return reverse(
			'blog.views.categoria', kwargs={'slug':self.slug}
			)

class SubCategoria(models.Model):
	"""docstring for SCategoria"""
	
	nome = models.CharField(max_length=100)
	categoria = models.ForeignKey(Categoria)
	slug = models.SlugField(max_length=130, blank=True, unique=True)
	def __unicode__(self):
		return u'%s=>%s' %(unicode(self.nome), unicode(self.categoria))
	def get_absolute_url(self):
		return reverse(
			'blog.views.categoria', kwargs={'slug':self.slug}
			)
class Categoria_Subcategoria(models.Model):
	categoria = models.ForeignKey(Categoria)
	SubCategoria = models.ForeignKey(SubCategoria)
	def __unicode__(self):
		return u'%s:%s' %(unicode(self.categoria.nome), unicode(self.subcategoria.nome))

class Autor(models.Model):
	"""docstring for Autor"""
	nome = models.CharField('Nome',max_length=100)
	unome = models.CharField('Ultimo nome',max_length=100)
	mnome = models.CharField('Nome do meio',max_length=100)
	data_entrada = models.DateTimeField(default=datetime.now, blank=True)
	biografia = models.TextField()
	foto = models.FileField(upload_to='avatar/autor/%s%s/'%(nome,unome), blank=True)
	def __unicode__(self):
		return u"%s, %s" %(unicode(self.unome),unicode(self.nome))

class Postagem(models.Model):
	class Meta:
		ordering = ('-publicacao',)
	titulo = models.CharField(max_length=100)
	conteudo = models.TextField('Conteudo')
	publicacao = models.DateTimeField('publicacao',default=datetime.now, blank=True)
	autor = models.ForeignKey(Autor)
	slug = models.SlugField(max_length=130, blank=True, unique=True)

	def get_absolute_url(self):
		return reverse(
			'blog.views.postagem', kwargs={'slug':self.slug}
			)
	def __unicode__(self):
		return u'"%s" by %s'  %(unicode(self.titulo),unicode(self.autor))

class Post_SubCategorias(models.Model):
	"""docstring for Post_SubCategorias"""
	post = models.ForeignKey(Postagem)
	subcategoria = models.ForeignKey(SubCategoria)
	def __unicode__(self):
		return u'%s:%s' %(unicode(self.post.titulo), unicode(self.subcategoria.nome))

class Post_Categorias(models.Model):
	post = models.ForeignKey(Postagem)
	categoria = models.ForeignKey(Categoria)
	def __unicode__(self):
		return u'%s:%s' %(unicode(self.post.titulo), unicode(self.categoria.nome))

def retira_acento_upload(a,b):
    import re
    import unicodedata
    import inspect
    from datetime import datetime
    
    l =  locals()
    path = "%s/%s" % (l['a'].__class__._meta.verbose_name_plural.lower(),     datetime.now().year)

    ext = b.split('.')[-1] #pega ultima ocorrência do split
    url = unicodedata.normalize('NFKD', b).encode('ascii', 'ignore')
    url = re.sub(r'[^\w\d-]', '', url.replace(' ', '-').replace('--', '').lower())
    return 'avatar/autor/%s/%s' % (a.nome, url[:-4]+'.'+ext)

def retira_acento_palavra(palavra):
    import re
    import unicodedata
    import inspect
    from datetime import datetime
    
    l =  locals()

    ext = palavra.split('.')[-1] #pega ultima ocorrência do split
    palavra = unicodedata.normalize('NFKD', b).encode('ascii', 'ignore')
    palavra = re.sub(r'[^\w\d-]', '', palavra.replace(' ', '-').replace('--', '').lower())
    return '%s' % (palavra[:-4]+'.'+ext)

from django.db.models import signals
from django.template.defaultfilters import slugify

def post_pre_save(signal, instance, sender, **kwargs):
	"""Este signal gera um slug automaticamente. Ele verifica se
	ja existe um artigo com o mesmo slug e acrescenta um numero ao
	final para evitar duplicidade"""
	if not instance.slug:
		slug = slugify(instance.titulo)
		novo_slug = slug
		contador = 0

		while Postagem.objects.filter(
		slug=novo_slug
		).exclude(id=instance.id).count() > 0:
			contador += 1
			novo_slug = '%s-%d' %(slug,contador)
		instance.slug = novo_slug


signals.pre_save.connect(post_pre_save, sender=Postagem)

def categoria_pre_save(signal, instance, sender, **kwargs):
	instance.slug = slugify(instance.nome)

signals.pre_save.connect(categoria_pre_save, sender=Categoria)

def subcategoria_pre_save(signal, instance, sender, **kwargs):
	instance.slug = slugify(instance.nome)

signals.pre_save.connect(subcategoria_pre_save, sender=SubCategoria)