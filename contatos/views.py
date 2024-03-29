from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import Http404
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages
from django.views.generic import TemplateView
from django.http import HttpResponse


def index(request):
    contatos = Contato.objects.all()
    paginator = Paginator(contatos, 5)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def ver_contato(request, contato_id):
    try:
        contato = Contato.objects.get(id=contato_id)
        if not contato.mostrar:
            raise Http404()  # mostra o erro 404 caso nao esteja marcado o mostrar, afim de nao visualizar por inserção na url
        return render(request, 'contatos/ver_contato.html', {
            'contato': contato
        })

    except Contato.DoesNotExist as e:
        raise Http404()


def busca(request):
    termo = request.GET.get('termo')

    if termo is None or not termo:
        messages.add_message(
            request,
            messages.ERROR,
            'Campo termo não pode ficar vazio'
        )
        return redirect('index')

    campos = Concat('nome', Value(' '), 'sobrenome')

    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        # buscará o nome parcial, não precisando ser o termo exato
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    )

    paginator = Paginator(contatos, 5)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })


def delete_contato(request, contato_id):
    agenda = Contato.objects.get(pk=contato_id)
    if request.method == 'POST':
        agenda.delete()
        return redirect('index')
    return render(request,'contatos/exclusao.html', {'item': agenda})
