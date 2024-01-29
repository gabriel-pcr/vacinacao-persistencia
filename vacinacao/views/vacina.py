from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from vacinacao.models import Vacina
from vacinacao.forms import VacinaForm


class VacinaListView(ListView):
    model = Vacina
    template_name = 'vacina/vacina_list.html'
    context_object_name = 'vacinas'


class VacinaCreateView(CreateView):
    model = Vacina
    form_class = VacinaForm
    template_name = 'vacina/vacina_form.html'
    success_url = '/vacina-list/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['periodicidade_choices'] = Vacina.periodicidade_choices
        return context


class VacinaUpdateView(UpdateView):
    model = Vacina
    form_class = VacinaForm
    template_name = 'vacina/vacina_form.html'

    def get_success_url(self):
        return reverse('vacina-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['periodicidade_choices'] = Vacina.periodicidade_choices
        return context


class VacinaDetailView(DetailView):
    model = Vacina
    template_name = 'vacina/vacina_detail.html'
    context_object_name = 'vacina'


def vacina_delete(request, pk):
    vacina = get_object_or_404(Vacina, pk=pk)

    if request.method == 'POST':
        vacina.delete()
        return HttpResponseRedirect(reverse_lazy('vacina-list'))

    return HttpResponseNotAllowed(['POST'])
