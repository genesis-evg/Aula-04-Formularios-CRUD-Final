from django.shortcuts import redirect, render

from meu_trenzinho.models import ranking

from .forms import rankingForm


# Create your views here.
def dados_carregados(request):
  ranking_func = ranking.objects.get(pk=1)
  return render(
    request,
    'index.html',
    
    { 'rankinkg_func' : ranking,
      'nome': 'Genesis da Silva Evangelista',
    }
  )



def adc_ranking (request):
  formulario = rankingForm()

  if request.method == 'POST' and request.POST:
    formulario = rankingForm(request.POST)
    if formulario.is_valid():
      formulario.save()
      return redirect("index")

  return render(
    request,
    "Adicionar_Dado.html",
    {'formulario': formulario}
  )

def editar_raking(request, id):
  ranking_func = ranking.objects.get(id=id)
  formulario = rankingForm(instance=ranking_func)
  print(ranking_func)

  if request.method == 'POST' and request.POST:
    formulario = rankingForm(request.POST, instance = ranking)
    if formulario.is_valid():
      formulario.save()
      return redirect("index")

  return render(
    request,
    'editar_dado.html',
    {'formulario': formulario}
  )

def remover_ranking(request, id): 
  ranking = ranking.objects.get(id=id)
  
  if request.method == 'POST' and request.POST: 
    ranking.delete() 
    return redirect("/home") 
    
  return render( 
    request, 
    'remover_Dado.html', 
    {'ranking': ranking} 
  )