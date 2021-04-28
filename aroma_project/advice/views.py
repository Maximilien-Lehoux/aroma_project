from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse

from .models import Pathology, EssentialOil, VegetableOil, Recipe, Way


def index(request):
    pathologies = Pathology.objects.all()
    ways = Way.objects.all()

    if request.method == 'POST':
        return redirect('advice:advice_he')
    context = {
        "pathologies": pathologies,
        "ways": ways,
    }
    return render(request, "advice/index.html", context)


def advice_he(request):
    pathology_choose = request.POST.get("pathology_choose")
    pathology_choose = Pathology.objects.get(name=pathology_choose)
    ways = pathology_choose.way.all()
    way_choose = request.POST.get("way_choose")
    pathologies = Pathology.objects.all()
    essentials_oils = pathology_choose.essential_oil.all()

    if request.method == "POST" and way_choose is not None:

        way_choose = Way.objects.get(name=way_choose)
        essentials_oils = EssentialOil.objects.filter(
            pathology__name=pathology_choose.name).filter(
            way__name=way_choose.name
        )
        vegetable_oil = pathology_choose.vegetable_oil
        print(essentials_oils)

        context = {
            "pathology_choose": pathology_choose,
            "essentials_oils": essentials_oils,
            "vegetable_oil": vegetable_oil,
            "way_choose": way_choose,
            "ways": ways,
            "pathologies": pathologies
        }
        return render(request, "advice/advice.html", context)

    else:

        context = {
            "pathology_choose": pathology_choose,
            "ways": ways,
            "pathologies": pathologies
        }
        return render(request, "advice/advice.html", context)

