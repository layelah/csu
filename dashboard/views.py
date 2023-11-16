from django.shortcuts import render
from pharmacien.models import Pharmacien
from django.contrib.auth.decorators import login_required


@login_required(login_url='connexion')
def vue_dashboard(request):
    count_pharmacien = Pharmacien.objects.all().count()
    context = {'count_pharmacien': count_pharmacien}
    return render(request, 'dashboard/dashboard.html', context)
