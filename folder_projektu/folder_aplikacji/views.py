from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Osoba, Person, Stanowisko, Team
<<<<<<< HEAD
from .serializers import OsobaSerializer, PersonSerializer, StanowiskoSerializer, TeamSerializer
from django.http import Http404, HttpResponse
from django.http import HttpResponse
import datetime
=======
from .serializers import OsobaSerializer, PersonSerializer, StanowiskoSerializer
from rest_framework.views import APIView
>>>>>>> lab_07_feature_class_view

# określamy dostępne metody żądania dla tego endpointu
@api_view(['GET'])
def person_list(request):
    """
    Lista wszystkich obiektów modelu Person.
    """
    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def person_detail(request, pk):

    """
    :param request: obiekt DRF Request
    :param pk: id obiektu Person
    :return: Response (with status and/or object/s data)
    """
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    """
    Zwraca pojedynczy obiekt typu Person.
    """
    if request.method == 'GET':
        person = Person.objects.get(pk=pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def osoba_list(request):
    if request.method == "GET":
        osoby = Osoba.objects.all()
        serializer = OsobaSerializer(osoby, many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = OsobaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','DELETE'])
def osoba_detail(request, pk):
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = OsobaSerializer(osoba)
        return Response(serializer.data)
    elif request.method == "DELETE":
        osoba.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def osoba_search(request, substring):
    osoby = Osoba.objects.filter(imie__icontains = substring) | Osoba.objects.filter(nazwisko__icontains = substring)
    serializer = OsobaSerializer(osoby, many = True)
    return Response(serializer.data)
    
@api_view(['GET', 'POST'])
def stanowisko_list(request):
    if request.method == "GET":
        stanowisko = Stanowisko.objects.all()
        serializer = StanowiskoSerializer(stanowisko, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = StanowiskoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'DELETE'])
def stanowisko_detail(request, pk):
    try:
        stanowisko = Stanowisko.objects.get(pk=pk)
    except Stanowisko.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = StanowiskoSerializer(stanowisko)
        return Response(serializer.data)
    elif request.method == "DELETE":
        stanowisko.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)  
    
<<<<<<< HEAD
 

def welcome_view(request):
    now = datetime.datetime.now()
    html = f"""
        <html><body>
        Witaj użytkowniku! </br>
        Aktualna data i czas na serwerze: {now}.
        </body></html>"""
    return HttpResponse(html)     
    
def person_list_html(request):
    # Pobieranie wszystkich obiektów Person i Team z bazy danych
    persons = Person.objects.all()
    teams = Team.objects.all()

    # Przekazanie danych obu modeli do szablonu
    return render(request, 
                  "folder_aplikacji/person/list.html", 
                  {'persons': persons, 'teams': teams})

    
def person_detail_html(request, id):
    # pobieramy konkretny obiekt Person
    try:
        person = Person.objects.get(id=id)
    except Person.DoesNotExist:
        raise Http404("Obiekt Person o podanym id nie istnieje")

    return render(request,
                  "folder_aplikacji/person/detail.html",
                  {'person': person})

# Widok API dla listy zespołów (GET/POST)
@api_view(['GET', 'POST'])
def team_list(request):
    if request.method == 'GET':
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Widok API dla szczegółów zespołu (GET/DELETE)
@api_view(['GET', 'DELETE'])
def team_detail(request, pk):
    try:
        team = Team.objects.get(pk=pk)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TeamSerializer(team)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Widok HTML dla listy zespołów
def team_list_html(request):
    teams = Team.objects.all()
    return render(request, "folder_aplikacji/team/list.html", {'teams': teams})

# Widok HTML dla szczegółów zespołu
def team_detail_html(request, id):
    try:
        team = Team.objects.get(id=id)
    except Team.DoesNotExist:
        raise Http404("Obiekt Team o podanym id nie istnieje")
    
    return render(request, "folder_aplikacji/team/detail.html", {'team': team})
=======
class OsobaList(APIView): 
    def get(self, request):
        osoby = Osoba.objects.all()
        serializer = OsobaSerializer(osoby, many = True)
        return Response(serializer.data) 
    
    def post(self, request):
        serializer = OsobaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class OsobaDetail(APIView):
    def get(self, request, pk):  
        try:
            osoba = Osoba.objects.get(pk=pk)
        except Osoba.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = OsobaSerializer(osoba)
        return Response(serializer.data)   
    
    def delete(self, request, pk):   
        try:
            osoba = Osoba.objects.get(pk=pk)
        except Osoba.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        osoba.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
>>>>>>> lab_07_feature_class_view
