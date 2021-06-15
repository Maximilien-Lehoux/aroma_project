from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from .form import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Pathology, EssentialOil, VegetableOil, Recipe, Way, \
    NeutralProduct, MethodOfUse, SideEffect, Contraindication


def index(request):
    """receives "true" when data bar searches for and displays index"""
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
    """Displays advices he and user's choices"""
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
            essential_oil__in=essentials_oils).distinct()
        contraindication = Contraindication.objects.filter(
            essential_oil__in=essentials_oils).distinct()

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


def admin_database(request):
    """receives "true" when data bar searches for and displays index"""
    if request.user.is_authenticated and request.user.is_staff:

        essential_oils = EssentialOil.objects.all().order_by('name')
        vegetable_oils = VegetableOil.objects.all().order_by('name')

        if request.method == 'POST':
            pathology_name = request.POST.get("pathology")
            zone = request.POST.get("zone")
            vegetable_oil = request.POST.get("vegetable_oil")
            essential_oil1 = request.POST.get("essential_oil1")
            essential_oil2 = request.POST.get("essential_oil2")
            essential_oil3 = request.POST.get("essential_oil3")

            if Pathology.objects.filter(name=pathology_name).exists():
                messages.error(request, "la pathologie existe")
                print("nooooooon")
                return redirect('advice:admin_database')

            else:
                print(pathology_name)
                print(zone)
                print(vegetable_oil)
                print(essential_oil1)
                print(essential_oil2)
                print(essential_oil3)


        context = {
                "essential_oils": essential_oils,
                "vegetable_oils": vegetable_oils
        }

        return render(request, "advice/admin_database.html", context)

    else:
        return redirect("advice:index")
