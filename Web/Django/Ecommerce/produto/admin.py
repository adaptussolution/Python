from django.contrib import admin
from . import models

class VariacaoInline(admin.TabularInline):
    model = models.Variacao
    extra = 1

@admin.register(models.Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = 'nome', 'descricao_curta','get_preco_formatado', 'get_preco_promocional_formatado',
    inlines = [
        VariacaoInline
    ]

# Register your models here.
admin.site.register(models.Variacao)