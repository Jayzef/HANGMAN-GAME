from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from .forms import *

class IndexView(View):
    def get(self, request):
        form = CadastroForm()
        rank = Jogo.objects.order_by('-sequencia')
        return render(request, 'index.html', {'form': form, 'rank': rank})
    
    def post(self, request):
        rank = Jogo.objects.order_by('-sequencia')
        form = CadastroForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data.get('nome')
            
            senha = form.cleaned_data.get('senha')
            
            usuario_existente = Usuario.objects.filter(nome=nome).exists()
            senha_correta = Usuario.objects.filter(nome=nome, senha=senha).exists()
            
            if usuario_existente and senha_correta:
                request.session['nome'] = nome
                return redirect('jogo')
            elif not usuario_existente:
                form.save()
                messages.success(request, 'Usuário cadastrado com sucesso!')
                return redirect('index')
            else:
                messages.error(request, 'Senha incorreta!')
        else:
            messages.error(request, 'Formulário inválido!')
        
        return render(request, 'index.html', {'form': form, 'rank': rank})

class HangmanView(View):
    def get(self, request):
        nome = request.session.get('nome')
        form = JogoForm()
        
        palavra = Palavra.objects.order_by('?').first()
        dica = palavra.dica
        palavraP = palavra.palavra
        
        return render(request, 'hangmangame.html', {'form': form, 'nome': nome, 'palavra': palavra, 'dica': dica, 'palavraP': palavraP})

    def post(self, request):
        form = JogoForm(request.POST)
        if form.is_valid():
            jogador = form.cleaned_data.get('jogador')  # Assumindo que o nome do jogador está no campo 'jogador'
            sequencia = form.cleaned_data.get('sequencia')
            
            jogo, created = Jogo.objects.update_or_create(
                jogador=jogador,
                defaults={'sequencia': sequencia}
            )
            
            return redirect('jogo')
        
        return render(request, 'hangmangame.html', {'form': form})
    
class SenhaView(View):
    def get(self, request):
        form = SenhaForm()
        return render(request, 'senha.html', {'form':form})
    def post(self, request):
        form = SenhaForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('usuario')
            senha = form.cleaned_data.get('senha')
            
            if(usuario == 'admin' and senha == 'admin'):
                administra = True
            else:
                administra = False
            
            request.session['ADM'] = administra
            if(administra == True):
                return redirect('lista')
        return render(request, 'senha.html', {'form':form, 'ADM':administra})
    
class ListaView(View):
    def get(self, request):
        if request.session.get('ADM') == True:
            palavras = Palavra.objects.all()
            jogadores = Usuario.objects.all()
            jogos = Jogo.objects.all()
            return render(request, 'lista.html', {'palavras': palavras, 'jogadores': jogadores, 'jogos': jogos})
        else:
            return redirect('senha')
    def post(self):
        return
    
class DeletePalavra(View):
    def get(self, request, id, *args, **kwargs):
        try:
            palavra = Palavra.objects.get(id=id)
            palavra.delete()
        except Palavra.DoesNotExist:
            messages.error(request, 'Palavra não encontrada.')
        return redirect('lista')

class DeleteUsuario(View):
    def get(self, request, id, *args, **kwargs):
        try:
            jogador = Usuario.objects.get(id=id)
            jogador.delete()
        except Usuario.DoesNotExist:
            messages.error(request, 'Usuário não encontrado.')
        return redirect('lista')

class DeleteJogo(View):
    def get(self, request, id, *args, **kwargs):
        try:
            jogo = Jogo.objects.get(id=id)
            jogo.delete()
        except Jogo.DoesNotExist:
            messages.error(request, 'Jogo não encontrado.')
        return redirect('lista')
    
class InserirView(View):
    def get(self, request):
        if request.session.get('ADM') == True:
            form1 = palavraForm(request.POST)
            form2 = cdpForm(request.POST)
            return render(request, 'inserir.html', {'form1': form1, 'form2': form2})
        else:
            return redirect('senha')
    def post(self, request):
        form1 = palavraForm(request.POST)
        form2 = cdpForm(request.POST)

        if form1.is_valid():
            palavra = form1.cleaned_data.get('palavra')

            palavra_existente = Palavra.objects.filter(palavra=palavra).exists()

            if palavra_existente:
                messages.error(request, 'Essa palavra já existe')
            else:
                form1.save()
                messages.success(request, 'Palavra registrada com sucesso!')
                return redirect('lista')
            
        if form2.is_valid():
            ndc = form1.cleaned_data.get('NDC')

            classe_existente = ClasseDePalavra.objects.filter(NDC=ndc).exists()

            if classe_existente:
                messages.error(request, 'Essa classe já existe')
            else:
                form2.save()
                messages.success(request, 'Classe registrada com sucesso!')
                return redirect('lista')

        return render(request, 'inserir.html', {'form1': form1, 'form2': form2})