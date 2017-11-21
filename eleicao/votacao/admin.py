from django.contrib import admin

from votacao.models import *


admin.site.register(Eleicao)
admin.site.register(Eleitor)
admin.site.register(Vaga)
admin.site.register(Candidato)
admin.site.register(Urna)
admin.site.register(Token)
