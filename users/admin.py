from django.contrib import admin
from .models import Perfil, Monografia, Tese, Dissertacao, Artigo, Livro

# Register your models here.
admin.site.register(Perfil)
admin.site.register(Monografia)
admin.site.register(Tese)
admin.site.register(Dissertacao)
admin.site.register(Artigo)
admin.site.register(Livro)


