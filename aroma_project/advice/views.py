from django.http import HttpResponse
from django.shortcuts import render

from .models import Pathology, EssentialOil


def index(request):
    patologies = Pathology.objects.all()

    if request.method == 'POST':
        pathology_choose = request.POST.get("pathology_choose")
        print(pathology_choose)

    context = {
        "patologies": patologies
    }



    return render(request, "advice/index.html", context)

