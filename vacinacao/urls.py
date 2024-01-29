from django.urls import path
from vacinacao.views import alergia, usuario, vacina, agenda

urlpatterns = [
    # base
    path('', agenda.AgendaListView.as_view(), name='index'),

    # alergia
    path('alergia-detail/<int:pk>/', alergia.AlergiaDetailView.as_view(), name='alergia-detail'),
    path('alergia-list/', alergia.AlergiaListView.as_view(), name='alergia-list'),
    path('alergia-create/', alergia.AlergiaCreateView.as_view(), name='alergia-create'),
    path('alergia-update/<int:pk>/', alergia.AlergiaUpdateView.as_view(), name='alergia-update'),
    path('alergia-delete/<int:pk>/', alergia.alergia_delete, name='alergia-delete'),

    # usuario
    path('usuario-detail/<int:pk>/', usuario.UsuarioDetailView.as_view(), name='usuario-detail'),
    path('usuario-list/', usuario.UsuarioListView.as_view(), name='usuario-list'),
    path('usuario-create/', usuario.UsuarioCreateView.as_view(), name='usuario-create'),
    path('usuario-update/<int:pk>/', usuario.UsuarioUpdateView.as_view(), name='usuario-update'),
    path('usuario-delete/<int:pk>/', usuario.usuario_delete, name='usuario-delete'),

    # vacina
    path('vacina-detail/<int:pk>/', vacina.VacinaDetailView.as_view(), name='vacina-detail'),
    path('vacina-list/', vacina.VacinaListView.as_view(), name='vacina-list'),
    path('vacina-create/', vacina.VacinaCreateView.as_view(), name='vacina-create'),
    path('vacina-update/<int:pk>/', vacina.VacinaUpdateView.as_view(), name='vacina-update'),
    path('vacina-delete/<int:pk>/', vacina.vacina_delete, name='vacina-delete'),

    # agenda
    path('agenda-detail/<int:pk>/', agenda.AgendaDetailView.as_view(), name='agenda-detail'),
    path('agenda-list/', agenda.AgendaListView.as_view(), name='agenda-list'),
    path('agenda-create/', agenda.AgendaCreateView.as_view(), name='agenda-create'),
    path('agenda-delete/<int:pk>/', agenda.agenda_delete, name='agenda-delete'),
    path('agenda-baixa/<int:pk>/', agenda.agenda_baixa, name='agenda-baixa'),
    path('agenda-usuario/<int:pk>/', agenda.AgendaUsuarioListView.as_view(), name='agenda-usuario'),

]
