from django.db import models


class VegetableOil(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    image = models.ImageField(upload_to="essential_oils")

    def __str__(self):
        return self.name


class NeutralProduct(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="neutral_product")

    def __str__(self):
        return self.name


class Pathology(models.Model):
    """creation of the pathologies table"""
    name = models.CharField(max_length=200)
    zone = models.CharField(max_length=200)
    vegetable_oil = models.ForeignKey(VegetableOil, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class EssentialOil(models.Model):
    """creation of the essential oils table"""
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="essential_oils")
    pathology = models.ManyToManyField(
        Pathology, related_name='essential_oil', blank=True)

    def __str__(self):
        return self.name


class CurativeEffect(models.Model):
    name = models.CharField(max_length=200)
    essential_oil = models.ManyToManyField(
        EssentialOil, related_name="curative_effect", blank=True)

    def __str__(self):
        return self.name


class SideEffect(models.Model):
    name = models.CharField(max_length=200)
    essential_oil = models.ManyToManyField(
        EssentialOil, related_name="side_effect", blank=True)

    def __str__(self):
        return self.name


class Contraindication(models.Model):
    """creation of the contraindication table"""
    name = models.CharField(max_length=200)
    essential_oil = models.ManyToManyField(
        EssentialOil, related_name="contraindication", blank=True)

    def __str__(self):
        return self.name


class Way(models.Model):
    name = models.CharField(max_length=200)
    essential_oil = models.ManyToManyField(
        EssentialOil, related_name="way", blank=True)
    pathology = models.ManyToManyField(
        Pathology, related_name="way", blank=True)

    def __str__(self):
        return self.name


class MethodOfUse(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    quantity = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    number_he = models.IntegerField()
    amount_he = models.CharField(max_length=200)
    mount_hv = models.CharField(max_length=200)
    way = models.ForeignKey(Way, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Legislation(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

