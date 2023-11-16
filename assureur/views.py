from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import AssureurForm
from .models import Assureur
from .filters import AssureurFilter


def vue_liste_assureur(request):
    liste_assureur = Assureur.objects.all().order_by('-date_ajout')
    my_filter = AssureurFilter(request.GET, queryset=liste_assureur)
    liste_assureur = my_filter.qs
    context = {'liste_assureur': liste_assureur, 'my_filter': my_filter}
    return render(request, 'assureur/liste_assureur.html', context)


def vue_details_assureur():
    return HttpResponseRedirect(reverse('liste_assureur'))


def vue_ajouter_assureur(request):
    if request.method == 'POST':
        form = AssureurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Le nouveau assureur a été ajouté avec succès.', extra_tags='ajout_assureur')
            if 'save_and_add_another' in request.POST:
                return redirect('ajouter_assureur')
            else:
                return redirect('liste_assureur')
    else:
        form = AssureurForm()
    return render(request, 'assureur/ajouter_assureur.html', {'form': form})


def vue_modification_assureur(request, pk):
    assureur = Assureur.objects.get(id=pk)

    if request.method == 'POST':
        form = AssureurForm(request.POST, request.FILES, instance=assureur)
        if form.is_valid():
            form.save()
            messages.success(request, 'Les informations sur l\'assureur ont été mises à jour avec succès.',
                             extra_tags='modification_assureur')
            return redirect('liste_assureur')
    else:
        form = AssureurForm(instance=assureur)

    return render(request, 'assureur/ajouter_assureur.html', {
        'form': form
    })


def vue_supprimer_assureur(request, pk):
    if request.method == 'POST':
        assureur = Assureur.objects.get(id=pk)
        assureur.delete()

        messages.success(request, 'L\'assureur a été supprimé avec succès.', extra_tags='suppression_assureur')

    return HttpResponseRedirect(reverse('liste_assureur'))
