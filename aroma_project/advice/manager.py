from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

from .models import Pathology, EssentialOil, VegetableOil, Recipe, Way, \
    NeutralProduct, MethodOfUse, SideEffect, Contraindication


class AdviceManager:
    def __init__(self):
        pass

    def get_context_route_condition(self, pathology_choose,
                                    way_choose, pathologies, ways):
        """Get context to display advices he and user's choices"""
        essentials_oils = 1
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
                protocole = MethodOfUse.objects.get(
                    name="cutanée générale")
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

        return context


class AdminManager:
    def __init__(self):
        pass

    def save_new_pathology(self, request, pathology_name, zone,
                                  vegetable_oil, essential_oil1,
                                  essential_oil2, essential_oil3):
        """the administrator adds a new pathology"""
        if Pathology.objects.filter(name=pathology_name).exists():
            messages.error(request, "la pathologie existe")
            return redirect('advice:admin_database')

        elif pathology_name == "" or \
                zone == "" or \
                vegetable_oil == "Huile végétale" or \
                vegetable_oil == "" or \
                essential_oil1 == "Huile essentielle" or \
                essential_oil1 == "":

            messages.error(request, "Les champs requis ne sont pas remplis")
            return redirect('advice:admin_database')

        else:
            vegetable_oil_id = VegetableOil.objects.get(name=vegetable_oil).id
            new_pathology = Pathology(name=pathology_name,
                                      zone=zone,
                                      vegetable_oil_id=vegetable_oil_id)
            new_pathology.save()

            essential_oil1_db = EssentialOil.objects.get(
                name=essential_oil1)

            essential_oil1_db.pathology.add(new_pathology)

            if essential_oil2 != "" and essential_oil2 != "Huile essentielle":
                essential_oil2_db = EssentialOil.objects.get(
                    name=essential_oil2)
                essential_oil2_db.pathology.add(new_pathology)

            elif essential_oil3 != "" and essential_oil3 != "Huile essentielle":
                essential_oil3_db = EssentialOil.objects.get(
                    name=essential_oil3)
                essential_oil3_db.pathology.add(new_pathology)

            messages.success(request,
                             "pathologie ajoutée avec succès")