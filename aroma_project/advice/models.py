from django.db import models


class Pathology(models.Model):
    """creation of the pathologies table"""
    name = models.CharField(max_length=200)
    zone = models.CharField(max_length=200)


class EssentialOil(models.Model):
    """creation of the essential oils table"""
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="essential_oils")
    pathology = models.ManyToManyField(
        Pathology, related_name='essential_oil', blank=True)


class CurativeEffect(models.Model):
    name = models.CharField(max_length=200)
    essential_oil = models.ManyToManyField(
        EssentialOil, related_name="curative_effect", blank=True)


class SideEffect(models.Model):
    name = models.CharField(max_length=200)
    essential_oil = models.ManyToManyField(
        EssentialOil, related_name="side_effect", blank=True)


class Contraindication(models.Model):
    """creation of the contraindication table"""
    name = models.CharField(max_length=200)
    essential_oil = models.ManyToManyField(
        EssentialOil, related_name="contraindication", blank=True)


class Way(models.Model):
    name = models.CharField(max_length=200)
    essential_oil = models.ManyToManyField(
        EssentialOil, related_name="way", blank=True)


class MethodOfUse(models.Model):
    description = models.CharField(max_length=1000)
    way = models.OneToOneField(Way, on_delete=models.CASCADE)


class Legislation(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

