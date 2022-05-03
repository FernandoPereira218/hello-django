from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} que tem {} anos</h1>'.format(nome, idade))

def soma(request, n1, n2):
    return HttpResponse('<h1> A soma de {} e {} é: {}'.format(n1, n2, n1+n2))

def multiplicacao(request, n1, n2):
    return HttpResponse('<h1> A multiplicacao de {} e {} é: {}'.format(n1, n2, n1*n2))

def divisao(request, n1, n2):
    return HttpResponse('<h1> A divisao de {} e {} é: {}'.format(n1, n2, n1/n2))

def subtracao(request, n1, n2):
    return HttpResponse('<h1> A subtracao de {} e {} é: {}'.format(n1, n2, n1-n2))