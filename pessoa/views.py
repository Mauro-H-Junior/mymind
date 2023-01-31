from django.shortcuts import render, redirect
from pessoa.models import Pessoa
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def listar_monitoramento(request):

    if request.method == 'GET':
        registros = Pessoa.objects.all()
        estados = Pessoa.avaliacao_diaria
        alertas = Pessoa.alertas_crises
        
        return render(request,'home.html', {'registros': registros, 'estados': estados, 'alertas': alertas })

    elif request.method == "POST":

        nome = request.POST.get('nome')
        acontecimento_negativo = request.POST.get('acontecimento_negativo')
        acontecimento_positivo = request.POST.get('acontecimento_positivo')
        estado_mental = request.POST.getlist('estado_mental')[0]
        alerta_crises = request.POST.getlist('alerta_crises')[0]
        data_acontecimento = request.POST.get('data_acontecimento')
        data_superacao = request.POST.get('data_superacao')
                                          

        atendimento = Pessoa(
            nome = nome,
            acontecimento_negativo = acontecimento_negativo,
            acontecimento_positivo = acontecimento_positivo,
            estado_mental = estado_mental,
            alerta_crises = alerta_crises,
            data_acontecimento = data_acontecimento,
            data_superacao = data_superacao,

        )

        atendimento.save()
        messages.success(request, 'Resgistro Adicionado ')
        print('salvei')
        return redirect('/')




