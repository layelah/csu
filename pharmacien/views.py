from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import PharmacienForm
from .models import Pharmacien
from .filters import PharmacienFilter


def vue_liste_pharmacien(request):
    liste_pharmacien = Pharmacien.objects.all().order_by('-date_ajout')
    my_filter = PharmacienFilter(request.GET, queryset=liste_pharmacien)
    liste_pharmacien = my_filter.qs
    context = {'liste_pharmacien': liste_pharmacien, 'my_filter': my_filter}
    return render(request, 'pharmacien/liste_pharmacien.html', context)


def vue_details_pharmacien():
    return HttpResponseRedirect(reverse('liste_pharmacien'))


def vue_ajouter_pharmacien(request):
    if request.method == 'POST':
        form = PharmacienForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Le nouveau pharmacien a été ajouté avec succès.', extra_tags='ajout_pharmacien')
            if 'save_and_add_another' in request.POST:
                return redirect('ajouter_pharmacien')
            else:
                return redirect('liste_pharmacien')
    else:
        form = PharmacienForm()
    return render(request, 'pharmacien/ajouter_pharmacien.html', {
        'form': form
    })


def vue_modification_pharmacien(request, pk):
    pharmacien = Pharmacien.objects.get(id=pk)

    if request.method == 'POST':
        form = PharmacienForm(request.POST, request.FILES, instance=pharmacien)
        if form.is_valid():
            form.save()
            messages.success(request, 'Les informations du pharmacien ont été mises à jour avec succès.',
                             extra_tags='modification_pharmacien')
            return redirect('liste_pharmacien')
    else:
        form = PharmacienForm(instance=pharmacien)

    return render(request, 'pharmacien/ajouter_pharmacien.html', {
        'form': form
    })


def vue_supprimer_pharmacien(request, pk):
    if request.method == 'POST':
        pharmacien = Pharmacien.objects.get(id=pk)
        pharmacien.delete()

        messages.success(request, 'Le pharmacien a été supprimé avec succès.', extra_tags='suppression_pharmacien')

    return HttpResponseRedirect(reverse('liste_pharmacien'))
