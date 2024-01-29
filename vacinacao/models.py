from django.core.exceptions import ValidationError
from django.db import models


class Alergia(models.Model):
    nome = models.CharField(max_length=40)


class Usuario(models.Model):
    nome = models.CharField(max_length=40)
    data_nascimento = models.DateField()
    logradouro = models.CharField(max_length=60, blank=True, null=True)
    numero = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    setor = models.CharField(max_length=40, blank=True, null=True)
    cidade = models.CharField(max_length=40, blank=True, null=True)
    uf_choices = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins')
    ]
    uf = models.CharField(max_length=2, choices=uf_choices, blank=True, null=True)
    sexo_choices = [('M', 'Masculino'), ('F', 'Feminino')]
    sexo = models.CharField(max_length=1, choices=sexo_choices)
    alergias = models.ManyToManyField('Alergia', related_name='usuarios')


class Vacina(models.Model):
    titulo = models.CharField(max_length=60)
    descricao = models.CharField(max_length=200, blank=True, null=True)
    doses = models.IntegerField()
    periodicidade_choices = [
        (1, 'Dia'),
        (2, 'Semana'),
        (3, 'Mês'),
        (4, 'Ano'),
    ]
    periodicidade = models.IntegerField(choices=periodicidade_choices, blank=True, null=True)
    intervalo = models.IntegerField(blank=True, null=True)

    def clean(self):
        if self.doses is not None and self.doses == 1:
            if self.periodicidade is not None:
                raise ValidationError("Periodicidade só é permitida quando doses for maior do que 1.")
            if self.intervalo is not None:
                raise ValidationError("Periodicidade só é permitido quando doses for maior do que 1.")
        super().clean()


class Agenda(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    situacao_choices = [
        ('Agendado', 'Agendado'),
        ('Cancelado', 'Cancelado'),
        ('Realizado', 'Realizado'),
    ]
    situacao = models.CharField(max_length=10, choices=situacao_choices, default=situacao_choices[0][0])
    data_situacao = models.DateField(blank=True, null=True)
    observacoes = models.CharField(max_length=200, blank=True, null=True)

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    vacina = models.ForeignKey(Vacina, on_delete=models.CASCADE)
    dose_vacina = models.IntegerField(default=1)
