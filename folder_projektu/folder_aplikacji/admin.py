from django.contrib import admin
from .models import Team, Person, Osoba, Stanowisko

# Rejestracja modelu Person z konfiguracją list_display i filtrami
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'shirt_size', 'team']
    list_filter = ['team']

# Rejestracja modelu Stanowisko z konfiguracją list_display i filtrami
@admin.register(Stanowisko)
class StanowiskoAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'opis']
    list_filter = ['nazwa']

# Rejestracja modelu Osoba z niestandardowym polem stanowisko_with_id
@admin.register(Osoba)
class OsobaAdmin(admin.ModelAdmin):
    @admin.display(description="Stanowisko (ID)")
    def stanowisko_with_id(self, obj):
        if obj.stanowisko:
            return f'{obj.stanowisko.nazwa} ({obj.stanowisko.id})'
        return "Brak stanowiska"

    list_display = ['imie', 'nazwisko', 'plec', 'stanowisko_with_id', 'data_dodania']
    list_filter = ['stanowisko', 'data_dodania']

# Rejestracja modelu Team bez dodatkowej konfiguracji
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass
