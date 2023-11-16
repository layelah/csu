from django.shortcuts import render, redirect
from pharmacien.models import Pharmacien
from pharmacien.filters import PharmacienFilter


def vue_accueil(request):
    les_pharmaciens = Pharmacien.objects.all()
    my_filter = PharmacienFilter(request.GET, queryset=les_pharmaciens)
    les_pharmaciens = my_filter.qs
    context = {'les_pharmaciens': les_pharmaciens, 'my_filter': my_filter}
    return render(request, 'accueil/accueil.html', context)


def handel404(request, exception):
    return render(request, '404.html')
