from django.shortcuts import render
from .models import *
from .forms import AlunoForm

# Create your views here.
def index(request):
    aluno = Aluno.objects.all()
    return render(request, 'aluno/index.html', {'lista':aluno})
    
    
def cadastro(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = AlunoForm()
    else:
        form = AlunoForm()
    
    return render(request, 'aluno/cadastro.html', {'form':form})
    
    
    