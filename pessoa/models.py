from django.db import models

class Pessoa(models.Model):

    avaliacao_diaria = (
        ('P', 'PÉSSIMO'),    
        ('R', 'RUIM'),    
        ('B', 'BOM'),
        ('E', 'EXCELENTE'),
    )

    alertas_crises = (
        ('P', 'PANICO'),    
        ('A', 'ANSIEDADE'),    
        ('D', 'DEPRESSAO'),
    )

    nome = models.CharField(max_length=100)
    acontecimento_negativo = models.TextField('Acontecimento Negativo',max_length=100)
    acontecimento_positivo = models.TextField('Acontecimento Positivo',max_length=100)
    estado_mental =  models.CharField("Selecione o seu estado mental atual", max_length=2,choices=avaliacao_diaria)
    alerta_crises = models.CharField("Selecione o seu estado de crise", max_length=2,choices=alertas_crises)
    data_atual = models.DateTimeField(auto_now=True)
    data_acontecimento = models.CharField(max_length=100)
    data_superaçao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
