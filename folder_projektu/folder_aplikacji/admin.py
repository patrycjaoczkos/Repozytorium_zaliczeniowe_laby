from django.contrib import admin
from .models import Team, Person, Osoba, Stanowisko

# Rejestracja modeli w panelu administracyjnym z konfiguracją list_display i filtrami
class PersonAdmin(admin.ModelAdmin):
    # list_display przechowuje pola wyświetlane w tabeli
    list_display = ['name', 'shirt_size', 'team']
    list_filter = ['team']

admin.site.register(Person, PersonAdmin)

class StanowiskoAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'opis']
    list_filter = ['nazwa']

admin.site.register(Stanowisko, StanowiskoAdmin)

class OsobaAdmin(admin.ModelAdmin):
    @admin.display(description="Stanowisko (ID)")
    def stanowisko_with_id(self, obj):
        if obj.stanowisko:
            return f'{obj.stanowisko.nazwa} ({obj.stanowisko.id})'
        return "Brak stanowiska"

    list_display = ['imie', 'nazwisko', 'plec', 'stanowisko_with_id', 'data_dodania']
    list_filter = ['stanowisko', 'data_dodania']

admin.site.register(Osoba, OsobaAdmin)

# Rejestracja pozostałych modeli bez dodatkowej konfiguracji
admin.site.register(Team)
