from django.shortcuts import render, redirect, get_object_or_404
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


def nave_nodriza_create(request, template_name='nave_nodriza/crear_nave.html'):
    form = nave_nodrizaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('naves_list')
    return render(request, template_name, {'form': form})

def nave_nodriza_delete(request, pk, template_name='nave_nodriza/borrar_nave.html'):
    post = get_object_or_404(nave_nodriza, pk=pk)
    if request.method=='POST':
        post.delete()
        return redirect('naves_list')
    return render(request, template_name, {'object': post})
