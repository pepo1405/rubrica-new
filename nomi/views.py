from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect

from .models import Rubrica, Rubricar
from .forms import RubricaForm, RubricarForm
from django.views import generic

# Create your views here.
def rubrica_list(request):
	rubricas = Rubrica.objects.order_by('nome')
	return render(request, 'nomi/rubrica_list.html', {'rubricas': rubricas})

def rubrica_detail(request, pk):
	rubrica = get_object_or_404(Rubrica, pk=pk)
	return render(request, 'nomi/rubrica_detail.html', {'rubrica': rubrica})

def rubrica_new(request):
    if request.method == "POST":
        form = RubricaForm(request.POST)
        if form.is_valid():
            rubrica = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            rubrica.save()
            return redirect('rubrica_list')
    else:
        form = RubricaForm()
    return render(request, 'nomi/rubrica_edit.html', {'form': form})
	
def rubrica_edit(request, pk):
    rubrica = get_object_or_404(Rubrica, pk=pk)
    if request.method == "POST":
        form = RubricaForm(request.POST, instance=rubrica)
        if form.is_valid():
            rubrica = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            rubrica.save()
            return redirect('rubrica_list')
    else:
        form = RubricaForm(instance=rubrica)
    return render(request, 'nomi/rubrica_edit.html', {'form': form})  

def rubricaProfileView(request, pk):
    rubrica = get_object_or_404(Rubrica, pk=pk)
    rubricar_rubrica = Rubricar.objects.filter(ragione_sociale=pk).order_by("-pk")
    context = {"rubrica": rubrica, "rubricar_rubrica": rubricar_rubrica}
    return render(request, 'nomi/rubrica_dettaglio.html', context)

def rubricar_new(request):
	if request.method == "POST":
		form = RubricarForm(request.POST)
		if form.is_valid():
			rubricar = form.save(commit=False)
			#rubricar.ragione_sociale=rubrica.nome
			#post.author = request.user
			#post.published_date = timezone.now()
			rubricar.save()
			return redirect('rubrica_list')
	else:
		form = RubricarForm()
	return render(request, 'nomi/rubricar_edit.html', {'form': form})

def rubricar_edit(request, pk):
    rubricar = get_object_or_404(Rubricar, pk=pk)
    if request.method == "POST":
        form = RubricarForm(request.POST, instance=rubricar)
        if form.is_valid():
            rubricar = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            rubricar.save()
            return redirect('rubrica_list')
    else:
        form = RubricarForm(instance=rubricar)
    return render(request, 'nomi/rubricar_edit.html', {'form': form})  

def rubrica_delete(request, pk):
	one_rubrica = Rubrica.objects.get(pk = pk)
	one_rubrica.delete() # line pk
	#return render(request, 'en/public/index.html', {'action' : 'Delete tasks'})
	return redirect('rubrica_list')

def rubricar_delete(request, pk):
	one_rubricar = Rubricar.objects.get(pk = pk)
	one_rubricar.delete() # line pk
	#return render(request, 'en/public/index.html', {'action' : 'Delete tasks'})
	return redirect('rubrica_list')
