
from django.conf import settings

from .models import Pathology, EssentialOil


class DataBase:
    def __init__(self):
        pass

    def entry_data_db(self):
        insomnia = Pathology(name="insomnie", zone="general")
        lavender = EssentialOil(
            name="lavande officinale",
            image="static/user/img/essential_oil/lavande.png")

        insomnia.save()
        lavender.save()


# ex_instance = DataBase()
# ex_instance.entry_data_db()
