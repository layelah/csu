from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import MedecinForm
from .models import Medecin
from .filters import MedecinFilter


def vue_liste_medecin(request):
    liste_medecin = Medecin.objects.all().order_by('-date_ajout')
    my_filter = MedecinFilter(request.GET, queryset=liste_medecin)
    liste_medecin = my_filter.qs
    context = {'liste_medecin': liste_medecin, 'my_filter': my_filter}
    return render(request, 'medecin/liste_medecin.html', context)


def vue_details_medecin():
    return HttpResponseRedirect(reverse('liste_medecin'))


def vue_ajouter_medecin(request):
    if request.method == 'POST':
        form = MedecinForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Le nouveau medecin a été ajouté avec succès.', extra_tags='ajout_medecin')
            if 'save_and_add_another' in request.POST:
                return redirect('ajouter_medecin')
            else:
                return redirect('liste_medecin')
    else:
        form = MedecinForm()
    return render(request, 'medecin/ajouter_medecin.html', {
        'form': form
    })


def vue_modification_medecin(request, pk):
    medecin = Medecin.objects.get(id=pk)

    if request.method == 'POST':
        form = MedecinForm(request.POST, request.FILES, instance=medecin)
        if form.is_valid():
            form.save()
            messages.success(request, 'Les informations du medecin ont été mises à jour avec succès.',
                             extra_tags='modification_medecin')
            return redirect('liste_medecin')
    else:
        form = MedecinForm(instance=medecin)

    return render(request, 'medecin/ajouter_medecin.html', {
        'form': form
    })


def vue_supprimer_medecin(request, pk):
    if request.method == 'POST':
        medecin = Medecin.objects.get(id=pk)
        medecin.delete()

        messages.success(request, 'Le medecin a été supprimé avec succès.', extra_tags='suppression_medecin')

    return HttpResponseRedirect(reverse('liste_medecin'))
