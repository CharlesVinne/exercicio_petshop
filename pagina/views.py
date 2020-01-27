from django.shortcuts import render, redirect
from pagina.models import Pet, Pessoa, Ong
from pagina.forms import PetForm, PessoaForm, OngForm
# Create your views here.
def index(request):
    form = PessoaForm(request.POST or None)
    args = {
        'form': form
    }
    if form.is_valid():
        form.save()
        args = {
            'msg': 'Dados cadastrados'
        }

    return render(request, 'index.html', args)


def pessoas(request):
    lista_clientes = Pessoa.objects.filter().all()
    args = {
        'pessoas': lista_clientes
    }

    return render(request, 'pessoas.html', args)


def cadastrar_pet(request):
    form = PetForm(request.POST or None)
    args = {
        'form':form
    }
    if form.is_valid():
        form.save()
        args = {
            'msg': 'Cadastro realizado com sucesso'
        }

    return render(request, 'cadastro-pet.html', args)

def login(request):
    if request.method == 'POST':
        email_formulario = request.POST.get('email')
        banco_dados = Pessoa.objects.filter(email=email_formulario).first()
        if banco_dados is not None:
            args = {
                'pessoa': banco_dados
            }
            return redirect('lista/')


    return render(request, 'login.html', {'msg': 'Seja bem-vindo'})

def cadastrar_ong(request):
    form = OngForm(request.POST or None)
    args = {
        'form':form
    }
    if form.is_valid():
        form.save()
        args = {
            'msg': 'Cadastro realizado com sucesso'
        }
    return render(request, 'cadastro-ong.html', args)

def lista_ongs(request):
    lista_ong = Ong.objects.all()
    args = {
        'lista_ongs':lista_ong
    }
    return render (request, 'lista-ongs.html', args)











