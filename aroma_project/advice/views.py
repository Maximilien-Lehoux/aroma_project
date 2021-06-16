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
from .manager import AdviceManager, AdminManager


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

        advice_manager = AdviceManager()
        context = advice_manager.get_context_route_condition(pathology_choose,
                                                             way_choose,
                                                             pathologies,
                                                             ways)

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

            admin_manager = AdminManager()
            admin_manager.save_new_pathology(request, pathology_name, zone,
                                  vegetable_oil, essential_oil1,
                                  essential_oil2, essential_oil3)

        context = {
                "essential_oils": essential_oils,
                "vegetable_oils": vegetable_oils
        }

        return render(request, "advice/admin_database.html", context)

    else:
        return redirect("advice:index")