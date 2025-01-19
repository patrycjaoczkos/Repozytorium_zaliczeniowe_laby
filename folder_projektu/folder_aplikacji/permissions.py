import copy
from rest_framework.permissions import DjangoModelPermissions

class CustomDjangoModelPermissions(DjangoModelPermissions):
    """
    Niestandardowa implementacja DjangoModelPermissions z modyfikacją uprawnień dla metod GET i DELETE.
    """

    def __init__(self):
        super().__init__()
        # Skopiuj perms_map, aby nie modyfikować oryginalnej mapy z klasy bazowej
        self.perms_map = copy.deepcopy(self.perms_map)
        # Dodaj niestandardowe uprawnienia
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']
        self.perms_map['DELETE'] = ['%(app_label)s.delete_%(model_name)s']
