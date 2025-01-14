from folder_aplikacji.models import Osoba, Stanowisko
from folder_aplikacji.serializers import OsobaSerializer, StanowiskoSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

# Tworzenie nowych obiektów
stanowisko = Stanowisko.objects.create(nazwa="Kierownik", opis="Zarządza tymi co zarządzają")
osoba = Osoba.objects.create(imie="Jan", nazwisko="Malinowski", plec=2, stanowisko=stanowisko)

# Serializacja obiektu Osoba
osoba_serializer = OsobaSerializer(osoba)
print(osoba_serializer.data)

# Serializacja do formatu JSON
osoba_json = JSONRenderer().render(osoba_serializer.data)
print(osoba_json)

# Deserializacja JSON do słownika
stream = io.BytesIO(osoba_json)
data = JSONParser().parse(stream)

# Tworzenie deserializera dla danych JSON
deserializer = OsobaSerializer(data=data)

# Walidacja danych
if deserializer.is_valid():
    print("Walidacja udana:", deserializer.validated_data)
    deserializer.save()
else:
    print("Błędy walidacji:", deserializer.errors)

# Błędne dane
invalid_data = {'imie': 'Adam', 'nazwisko': 'Nowak', 'plec': 'Nieznany', 'stanowisko': stanowisko.id}
invalid_serializer = OsobaSerializer(data=invalid_data)

if invalid_serializer.is_valid():
    print("Dane są poprawne!")
else:
    print("Błędy walidacji:", invalid_serializer.errors)

# Serializacja obiektu Stanowisko
stanowisko_serializer = StanowiskoSerializer(stanowisko)
print(stanowisko_serializer.data)

# Serializacja do formatu JSON
stanowisko_json = JSONRenderer().render(stanowisko_serializer.data)
print(stanowisko_json)

# Deserializacja JSON do słownika
stream = io.BytesIO(stanowisko_json)
data = JSONParser().parse(stream)

# Tworzenie deserializera dla Stanowisko
deserializer = StanowiskoSerializer(data=data)

# Walidacja danych
if deserializer.is_valid():
    print("Walidacja udana:", deserializer.validated_data)
    deserializer.save()
else:
    print("Błędy walidacji:", deserializer.errors)

