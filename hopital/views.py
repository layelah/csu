from django.http import JsonResponse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import HopitalForm
from .models import Hopital
from localisation.models import Departement, Commune
from .filters import HopitalFilter


def vue_liste_hopital(request):
    liste_hopital = Hopital.objects.all().order_by('-date_ajout')
    my_filter = HopitalFilter(request.GET, queryset=liste_hopital)
    liste_hopital = my_filter.qs
    context = {'liste_hopital': liste_hopital, 'my_filter': my_filter}
    return render(request, 'hopital/liste_hopital.html', context)


def vue_details_hopital():
    return HttpResponseRedirect(reverse('liste_hopital'))


def vue_ajouter_hopital(request):
    if request.method == 'POST':
        form = HopitalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Le nouveau hopital a été ajouté avec succès.', extra_tags='ajout_hopital')
            if 'save_and_add_another' in request.POST:
                return redirect('ajouter_hopital')
            else:
                return redirect('liste_hopital')
    else:
        form = HopitalForm()
    return render(request, 'hopital/ajouter_hopital.html', {'form': form})


def vue_modification_hopital(request, pk):
    hopital = Hopital.objects.get(id=pk)

    if request.method == 'POST':
        form = HopitalForm(request.POST, request.FILES, instance=hopital)
        if form.is_valid():
            form.save()
            messages.success(request, 'Les informations de hopital ont été mises à jour avec succès.',
                             extra_tags='modification_hopital')
            return redirect('liste_hopital')
    else:
        form = HopitalForm(instance=hopital)

    return render(request, 'hopital/ajouter_hopital.html', {
        'form': form
    })


def vue_supprimer_hopital(request, pk):
    if request.method == 'POST':
        hopital = Hopital.objects.get(id=pk)
        hopital.delete()

        messages.success(request, "L'hopital a été supprimé avec succès.", extra_tags='suppression_hopital')

    return HttpResponseRedirect(reverse('liste_hopital'))


# AJAX
def chargement_departement(request):
    region_id = request.GET.get('region_id')
    departements = Departement.objects.filter(region_id=region_id).all()
    return render(request, 'localisation/liste_options_departement.html', {'departements': departements})


def chargement_commune(request):
    departement_id = request.GET.get('departement_id')
    communes = Commune.objects.filter(departement_id=departement_id).all()
    return render(request, 'localisation/liste_options_commune.html', {'communes': communes})
