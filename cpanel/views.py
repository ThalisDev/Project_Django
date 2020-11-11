from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from .forms import RegistrationForm
from .models import RegistrationData
from django.contrib import messages

#Define pagina inicial e CRUD
def Home (request):
    obj = RegistrationData.objects.get(id = 1)#consulta banco de dados e exibe na seção 2
    context = {
        "form":RegistrationForm, #retorna formulario
        "object":obj #orienta variavel
        }
    return render(request,'index.html',context)


#Registra usuario
def addUser (request):
    form = RegistrationForm(request.POST)

    if form.is_valid():
        myregister = RegistrationData(nome = form.cleaned_data['nome'],
                                    telefone = form.cleaned_data['telefone'],
                                    email = form.cleaned_data['email'],
                                    atuacao = form.cleaned_data['atuacao'])
        myregister.save()
        messages.add_message(request, messages.SUCCESS, "Seu cadastro foi concluido com sucesso!")#retorna mensagem de sucesso ao cadastrar
        
    return redirect(Home)