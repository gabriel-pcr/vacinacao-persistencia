from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from vacinacao.models import Alergia
from vacinacao.forms import AlergiaForm


class AlergiaListView(ListView):
    model = Alergia
    template_name = 'alergia/alergia_list.html'
    context_object_name = 'alergias'


class AlergiaCreateView(CreateView):
    model = Alergia
    form_class = AlergiaForm
    template_name = 'alergia/alergia_form.html'
    success_url = '/alergia-list/'


class AlergiaUpdateView(UpdateView):
    model = Alergia
    form_class = AlergiaForm
    template_name = 'alergia/alergia_form.html'

    def get_success_url(self):
        return reverse('alergia-list')


class AlergiaDetailView(DetailView):
    model = Alergia
    template_name = 'alergia/alergia_detail.html'
    context_object_name = 'alergia'


def alergia_delete(request, pk):
    alergia = get_object_or_404(Alergia, pk=pk)

    if request.method == 'POST':
        alergia.delete()
        return HttpResponseRedirect(reverse_lazy('alergia-list'))

    return HttpResponseNotAllowed(['POST'])
