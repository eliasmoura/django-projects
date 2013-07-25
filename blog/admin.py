# -*- coding: utf8 -*-
from django.contrib import admin
from blog.models import *


admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(SubCategoria)
admin.site.register(Post_SubCategorias)
admin.site.register(Post_Categorias)
admin.site.register(Postagem)