from django.shortcuts import render
from django.forms import ModelForm

from marcianos.models import nave_nodriza

# Create your views here.
class nave_nodrizaForm(ModelForm):
    class Meta:
        model = nave_nodriza
        fields = ['nombre']

def nave_nodrizaList(request, template_name = 'nave_nodriza/lista.html'):
    naves_nodrizas = nave_nodriza.objects.all() #Obtengo la lista de naves
    data = {}
    data['object_list'] = naves_nodrizas #Devuelvo los objetos que voy a pintar
    return render(request, template_name, data)
