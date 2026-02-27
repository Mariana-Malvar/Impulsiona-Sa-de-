from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import PessoaForm
from .models import Pessoa

def index(request, id=None):
    # Se vier um ID na URL, estamos EDITANDO
    if id:
        instance = get_object_or_404(Pessoa, id=id) if id else None
    else:
        instance = None

    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            msg = 'Atualizado!' if instance else 'Cadastrado!'
            messages.success(request, msg)
            return redirect('index')
    else:
        form = PessoaForm(instance=instance)
    
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoa_form.html', {'form': form, 'pessoas': pessoas})

def excluir(request, id):
    pessoa = get_object_or_404(Pessoa, id=id)
    pessoa.delete()
    messages.success(request, 'Removido com sucesso!')
    return redirect('index')
