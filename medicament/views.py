from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import MedicamentForm
from .models import Medicament
from .filters import MedicamentFilter


def vue_liste_medicament(request):
    liste_medicament = Medicament.objects.all().order_by('-date_ajout')
    my_filter = MedicamentFilter(request.GET, queryset=liste_medicament)
    liste_medicament = my_filter.qs
    context = {'liste_medicament': liste_medicament, 'my_filter': my_filter}
    return render(request, 'medicament/liste_medicament.html', context)


def vue_details_medicament():
    return HttpResponseRedirect(reverse('liste_medicament'))


def vue_ajouter_medicament(request):
    if request.method == 'POST':
        form = MedicamentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Le nouveau medicament a été ajouté avec succès.', extra_tags='ajout_medicament')
            if 'save_and_add_another' in request.POST:
                return redirect('ajouter_medicament')
            else:
                return redirect('liste_medicament')
    else:
        form = MedicamentForm()
    return render(request, 'medicament/ajouter_medicament.html', {
        'form': form
    })


def vue_modification_medicament(request, pk):
    medicament = Medicament.objects.get(id=pk)

    if request.method == 'POST':
        form = MedicamentForm(request.POST, request.FILES, instance=medicament)
        if form.is_valid():
            form.save()
            messages.success(request, 'Les informations sur le medicament ont été mises à jour avec succès.',
                             extra_tags='modification_medicament')
            return redirect('liste_medicament')
    else:
        form = MedicamentForm(instance=medicament)

    return render(request, 'medicament/ajouter_medicament.html', {
        'form': form
    })


def vue_supprimer_medicament(request, pk):
    if request.method == 'POST':
        medicament = Medicament.objects.get(id=pk)
        medicament.delete()

        messages.success(request, 'Le médicament a été supprimé avec succès.', extra_tags='suppression_medicament')

    return HttpResponseRedirect(reverse('liste_medicament'))
