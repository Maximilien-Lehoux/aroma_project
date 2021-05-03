from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from .form import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from .models import Pathology, EssentialOil, VegetableOil, Recipe, Way, \
    NeutralProduct, MethodOfUse, SideEffect, Contraindication


def index(request):
    pathologies = Pathology.objects.all().order_by('name')
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
    pathologies = Pathology.objects.all().order_by('name')
    ways = pathology_choose.way.all()
    way_choose = request.POST.get("way_choose")

    if request.method == "POST" and way_choose is not None:

        way_choose = Way.objects.get(name=way_choose)

        if way_choose.name == "orale":
            essentials_oils = EssentialOil.objects.filter(
                pathology__name=pathology_choose.name).filter(
                way__name=way_choose.name)[0:2]

            vegetable_oil = NeutralProduct.objects.get(name="miel")
            protocole = MethodOfUse.objects.get(name="orale")

        elif way_choose.name == "bain":
            essentials_oils = EssentialOil.objects.filter(
                pathology__name=pathology_choose.name).filter(
                way__name=way_choose.name)[0:1]

            vegetable_oil = NeutralProduct.objects.get(name="gel douche")
            protocole = MethodOfUse.objects.get(name="bain")

        elif way_choose.name == "diffusion":
            essentials_oils = EssentialOil.objects.filter(
                pathology__name=pathology_choose.name).filter(
                way__name=way_choose.name)

            vegetable_oil = NeutralProduct.objects.get(name="alcool")
            protocole = MethodOfUse.objects.get(name="diffusion")

        elif way_choose.name == "Inhalation":
            essentials_oils = EssentialOil.objects.filter(
                pathology__name=pathology_choose.name).filter(
                way__name=way_choose.name)

            vegetable_oil = NeutralProduct.objects.get(name="bol d'eau")
            protocole = MethodOfUse.objects.get(name="inhalation")

        elif way_choose.name == "cutanée":
            essentials_oils = EssentialOil.objects.filter(
                pathology__name=pathology_choose.name).filter(
                way__name=way_choose.name)

            vegetable_oil = pathology_choose.vegetable_oil

            if pathology_choose.zone == "general":
                protocole = MethodOfUse.objects.get(name="cutanée générale")
            else:
                protocole = MethodOfUse.objects.get(name="cutanée")

        number_he = essentials_oils.count()
        amount = Recipe.objects.filter(
            way__name=way_choose.name).get(number_he=number_he)
        sides_effects = SideEffect.objects.filter(
            essential_oil__in=essentials_oils)
        contraindication = Contraindication.objects.filter(
            essential_oil__in=essentials_oils)

        context = {
            "pathologies": pathologies,
            "pathology_choose": pathology_choose,
            "essentials_oils": essentials_oils,
            "vegetable_oil": vegetable_oil,
            "way_choose": way_choose,
            "ways": ways,
            "amount": amount,
            "protocole": protocole,
            "sides_effects": sides_effects,
            "contraindications": contraindication,
        }
        return render(request, "advice/advice.html", context)

    else:
        context = {
            "pathology_choose": pathology_choose,
            "ways": ways,
            "pathologies": pathologies,
        }
        return render(request, "advice/advice.html", context)
