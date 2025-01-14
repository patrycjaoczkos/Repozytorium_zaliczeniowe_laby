from rest_framework import serializers
from .models import Person, Team, MONTHS, SHIRT_SIZES, Stanowisko, Osoba


class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    shirt_size = serializers.ChoiceField(choices=SHIRT_SIZES, default=SHIRT_SIZES[0][0])
    miesiac_dodania = serializers.ChoiceField(choices=MONTHS.choices, default=MONTHS.choices[0][0])
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    pseudonim = serializers.CharField(required=False)

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.shirt_size = validated_data.get('shirt_size', instance.shirt_size)
        instance.miesiac_dodania = validated_data.get('miesiac_dodania', instance.miesiac_dodania)
        instance.team = validated_data.get('team', instance.team)
        instance.pseudonim = validated_data.get('pseudonim', instance.pseudonim)
        instance.save()
        return instance


class StanowiskoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stanowisko
        fields = ['id', 'nazwa', 'opis']


class OsobaSerializer(serializers.ModelSerializer):  # Uwaga: poprawiona nazwa
    class Meta:
        model = Osoba
        fields = ['id', 'imie', 'nazwisko', 'plec', 'stanowisko', 'data_dodania']
        read_only_fields = ['id', 'data_dodania']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'country']
        read_only_fields = ['id']


    