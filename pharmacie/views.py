from django.http import JsonResponse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import PharmacieForm
from .models import Pharmacie
from localisation.models import Departement, Commune
from .filters import PharmacieFilter


def vue_liste_pharmacie(request):
    liste_pharmacie = Pharmacie.objects.all().order_by('-date_ajout')
    my_filter = PharmacieFilter(request.GET, queryset=liste_pharmacie)
    liste_pharmacie = my_filter.qs
    context = {'liste_pharmacie': liste_pharmacie, 'my_filter': my_filter}
    return render(request, 'pharmacie/liste_pharmacie.html', context)


def vue_details_pharmacie():
    return HttpResponseRedirect(reverse('liste_pharmacie'))


def vue_ajouter_pharmacie(request):
    if request.method == 'POST':
        form = PharmacieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'La nouvelle pharmacie a été ajouté avec succès.', extra_tags='ajout_pharmacie')
            if 'save_and_add_another' in request.POST:
                return redirect('ajouter_pharmacie')
            else:
                return redirect('liste_pharmacie')
    else:
        form = PharmacieForm()
    return render(request, 'pharmacie/ajouter_pharmacie.html', {
        'form': form
    })


def vue_modification_pharmacie(request, pk):
    pharmacie = Pharmacie.objects.get(id=pk)

    if request.method == 'POST':
        form = PharmacieForm(request.POST, request.FILES, instance=pharmacie)
        if form.is_valid():
            form.save()
            messages.success(request, 'Les informations de la pharmacie ont été mises à jour avec succès.',
                             extra_tags='modification_pharmacie')
            return redirect('liste_pharmacie')
    else:
        form = PharmacieForm(instance=pharmacie)

    return render(request, 'pharmacie/ajouter_pharmacie.html', {
        'form': form
    })


def vue_supprimer_pharmacie(request, pk):
    if request.method == 'POST':
        pharmacie = Pharmacie.objects.get(id=pk)
        pharmacie.delete()

        messages.success(request, 'La pharmacie a été supprimé avec succès.', extra_tags='suppression_pharmacie')

    return HttpResponseRedirect(reverse('liste_pharmacie'))


# AJAX
def chargement_departement(request):
    region_id = request.GET.get('region_id')
    departements = Departement.objects.filter(region_id=region_id).all()
    return render(request, 'localisation/liste_options_departement.html', {'departements': departements})


def chargement_commune(request):
    departement_id = request.GET.get('departement_id')
    communes = Commune.objects.filter(departement_id=departement_id).all()
    return render(request, 'localisation/liste_options_commune.html', {'communes': communes})
