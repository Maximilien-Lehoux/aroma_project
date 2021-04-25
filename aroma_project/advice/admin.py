from django.contrib import admin

from .models import Pathology, EssentialOil, CurativeEffect, Legislation, \
    SideEffect, MethodOfUse, Way, Contraindication, VegetableOil

admin.site.register(Pathology)
admin.site.register(EssentialOil)
admin.site.register(CurativeEffect)
admin.site.register(Legislation)
admin.site.register(SideEffect)
admin.site.register(MethodOfUse)
admin.site.register(Way)
admin.site.register(Contraindication)
admin.site.register(VegetableOil)

