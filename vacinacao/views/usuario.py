from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from vacinacao.models import Usuario, Alergia
from vacinacao.forms import UsuarioForm


class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuario/usuario_list.html'
    context_object_name = 'usuarios'


class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuario/usuario_form.html'
    success_url = '/usuario-list/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['uf_choices'] = Usuario.uf_choices
        context['alergia_choices'] = Alergia.objects.all()
        context['sexo_choices'] = Usuario.sexo_choices
        return context


class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuario/usuario_form.html'

    def get_success_url(self):
        return reverse('usuario-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['uf_choices'] = Usuario.uf_choices
        context['alergia_choices'] = Alergia.objects.all()
        context['sexo_choices'] = Usuario.sexo_choices
        return context


class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = 'usuario/usuario_detail.html'
    context_object_name = 'usuario'


def usuario_delete(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)

    if request.method == 'POST':
        usuario.delete()
        return HttpResponseRedirect(reverse_lazy('usuario-list'))

    return HttpResponseNotAllowed(['POST'])
