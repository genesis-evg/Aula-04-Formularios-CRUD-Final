from django.contrib import admin

# Register your models here.
from .models import link, ranking


class rankingAdmin(admin.ModelAdmin):
  list_display= ['nome','icone', 'descricao','modalidade', 'relevancia']
  ordering = ['nome']
admin.site.register(ranking, rankingAdmin)

class linkAdmin(admin.ModelAdmin):
  list_display= ['nome','link', 'ref_ranking', 'descricao', 'cadastrado']
  ordering = ['nome']
admin.site.register(link, linkAdmin)