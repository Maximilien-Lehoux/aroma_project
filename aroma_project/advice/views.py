from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from .models import Pathology, EssentialOil


def index(request):
    pathologies = Pathology.objects.all()

    if request.method == 'POST':
        return redirect('advice:advice_he')
    context = {
        "pathologies": pathologies
    }
    return render(request, "advice/index.html", context)


def advice_he(request):
    pathology_choose = request.POST.get("pathology_choose")
    pathology_choose = Pathology.objects.get(name=pathology_choose)
    print(pathology_choose.name)

    essentials_oils = pathology_choose.essential_oil.all()
    # print(essentials_oils)

    context = {
        "pathology_choose": pathology_choose,
        "essentials_oils": essentials_oils
    }
    return render(request, "advice/advice.html", context)

