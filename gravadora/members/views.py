from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import View
from django.views.generic.edit import FormView
from .forms import AddMusicaForm, AddMusicoForm, AddBandaForm, AddInstrumentoForm, AddDiscoForm, addProdutorForm
from .models import Musico, Musica, Disco
# Create your views here.

class ShowPlayListView(View):
    template_name = 'index.htm'
    #if Musico.objects.all()
    d = Disco.objects.all().get(id=1)
    musicas = Musica.objects.all().filter(aparece__id=d.id).values()
    context = {
        'musico': Musico.objects.all().values(), #get(id=1), 
        'musica' : Musica.objects.all().filter(aparece__id=d.id).first(), # música atual
        'disco': d,
        'musicas' : musicas # selecionar futuramente apenas musicas da playlist/disco
    }
    def get(self, request, *args, **kwargs):
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(self.context, request))

class SaveMusicoForm(FormView):
    template_name = 'add.htm'
    form_class = AddMusicoForm
    success_url = '/success/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SaveMusicoForm, self).get_context_data(**kwargs)
        context['pagetitle'] = 'Cadastro de Músico'
        return context

class SaveBandaForm(FormView):
    template_name = 'add.htm'
    form_class = AddBandaForm
    success_url = '/success/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SaveBandaForm, self).get_context_data(**kwargs)
        context['pagetitle'] = 'Cadastro de Banda'
        return context

class SaveInstrumentoForm(FormView):
    template_name = 'add.htm'
    form_class = AddInstrumentoForm
    success_url = '/success/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SaveInstrumentoForm, self).get_context_data(**kwargs)
        context['pagetitle'] = 'Cadastro de Instrumento'
        return context

class SaveDiscoForm(FormView):
    template_name = 'add.htm'
    form_class = AddDiscoForm
    success_url = '/success/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(SaveDiscoForm, self).get_context_data(**kwargs)
        context['pagetitle'] = 'Cadastro de Disco'
        return context

class SaveProdutorForm(FormView):
    template_name = 'add.htm'
    form_class = addProdutorForm
    success_url = '/success/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(SaveProdutorForm, self).get_context_data(**kwargs)
        context['pagetitle'] = 'Cadastro de Produtor'
        return context

class SaveMusicaForm(FormView): # multiple select box is not showing as expected
    template_name = 'add.htm'
    form_class = AddMusicaForm
    success_url = '/success/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs): # it's not showing title for some reason
        context = super(SaveMusicaForm, self).get_context_data(**kwargs)
        context['pagetitle'] = 'Cadastro de Musica'
        return context