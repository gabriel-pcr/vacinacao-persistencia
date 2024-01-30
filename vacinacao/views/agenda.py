from datetime import datetime, timedelta

from django.db.models import Value, Case, When, IntegerField
from django.http import HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from vacinacao.models import Agenda, Usuario, Vacina
from vacinacao.forms import AgendaForm


class AgendaListView(ListView):
    model = Agenda
    template_name = 'agenda/agenda_list.html'
    context_object_name = 'agendas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['situacao_choices'] = Agenda.situacao_choices[1:]
        return context

    def get(self, request, *args, **kwargs):
        status_filter = request.GET.get('status')
        date_filter = request.GET.get('date')

        agendas = Agenda.objects.all()
        if status_filter == 'canceladas':
            agendas = Agenda.objects.filter(situacao='Cancelado')
        elif status_filter == 'realizadas':
            agendas = Agenda.objects.filter(situacao='Realizado')

        if date_filter == 'hoje':
            formatted_date = datetime.now().strftime('%Y-%m-%d')
            agendas = agendas.filter(data=formatted_date)

        custom_order = Case(
            When(situacao='Agendado', then=Value(1)),
            When(situacao='Realizado', then=Value(2)),
            When(situacao='Cancelado', then=Value(3)),
            default=Value(4),
            output_field=IntegerField()
        )

        agendas = agendas.order_by(custom_order)

        context = {'agendas': agendas, 'situacao_choices': Agenda.situacao_choices[1:]}
        return render(request, self.template_name, context)


class AgendaUsuarioListView(ListView):
    model = Agenda
    template_name = 'agenda/agenda_usuario_list.html'
    context_object_name = 'agendas'

    def get(self, request, *args, **kwargs):
        usuario_id = kwargs.get('pk')
        status_filter = request.GET.get('status')
        date_filter = request.GET.get('date')

        agendas = Agenda.objects.all()
        if status_filter == 'canceladas':
            agendas = Agenda.objects.filter(situacao='Cancelado')
        elif status_filter == 'realizadas':
            agendas = Agenda.objects.filter(situacao='Realizado')

        if date_filter == 'hoje':
            formatted_date = datetime.now().strftime('%Y-%m-%d')
            agendas = agendas.filter(data=formatted_date)

        custom_order = Case(
            When(situacao='Agendado', then=Value(1)),
            When(situacao='Realizado', then=Value(2)),
            When(situacao='Cancelado', then=Value(3)),
            default=Value(4),
            output_field=IntegerField()
        )

        agendas = agendas.filter(usuario_id=usuario_id).order_by(custom_order)

        context = {'agendas': agendas, 'situacao_choices': Agenda.situacao_choices[1:],
                   'usuario': Usuario.objects.get(id=usuario_id)}
        return render(request, self.template_name, context)


class AgendaCreateView(CreateView):
    model = Agenda
    form_class = AgendaForm
    template_name = 'agenda/agenda_form.html'
    success_url = '/agenda-list/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuario_choices'] = Usuario.objects.all()
        context['vacina_choices'] = Vacina.objects.all()
        context['situacao_choices'] = Agenda.situacao_choices
        return context

    def form_invalid(self, form):
        print(form)
        return super().form_invalid(form)

    def form_valid(self, form):
        vacina = form.cleaned_data.get('vacina')

        data_agendamento = form.cleaned_data.get('data')
        for dose in range(1, vacina.doses):
            if vacina.get_periodicidade_display() == "Dia":
                data_agendamento += timedelta(
                    days=vacina.intervalo
                )
            elif vacina.get_periodicidade_display() == "Semana":
                data_agendamento += timedelta(
                    weeks=vacina.intervalo
                )
            elif vacina.get_periodicidade_display() == "Mês":
                data_agendamento += timedelta(
                    days=vacina.intervalo * 30
                )
            elif vacina.get_periodicidade_display() == "Ano":
                data_agendamento += timedelta(
                    days=vacina.intervalo * 365
                )

            Agenda.objects.create(
                data=data_agendamento,
                hora=form.cleaned_data.get('hora'),
                observacoes=form.cleaned_data.get('observacoes'),
                usuario=form.cleaned_data.get('usuario'),
                vacina=form.cleaned_data.get('vacina'),
                dose_vacina=dose + 1,
            )

        return super().form_valid(form)


class AgendaDetailView(DetailView):
    model = Agenda
    template_name = 'agenda/agenda_detail.html'
    context_object_name = 'agenda'


def agenda_delete(request, pk):
    agenda = get_object_or_404(Agenda, pk=pk)

    if request.method == 'POST':
        agenda.delete()
        return HttpResponseRedirect(reverse_lazy('agenda-list'))

    return HttpResponseNotAllowed(['POST'])


def agenda_baixa(request, pk):
    agenda = get_object_or_404(Agenda, pk=pk)

    if request.method == 'POST':
        today_date = datetime.now().date()
        agenda.data_situacao = today_date.strftime("%Y-%m-%d")
        agenda.situacao = request.POST['situacao']
        agenda.save()
        return HttpResponseRedirect(reverse_lazy('agenda-list'))

    return HttpResponseNotAllowed(['POST'])
