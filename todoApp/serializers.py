from rest_framework import serializers
from .models import Todos

class TodosSerializer(serializers.Serializer):
    #inserisce model nel serializers ( interessante ) 
    #class Meta:
    #    model = Todos
    #    fields = ["id","stato", "testo"]

    id = serializers.IntegerField(read_only=True)
    stato = serializers.BooleanField()
    testo = serializers.CharField(max_length=200)

    def create(self, validated_data):
        """
        Create and return a new `Todos` instance, given the validated data.
        """
        return Todos.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.stato = validated_data.get("stato", instance.stato)
        instance.testo = validated_data.get("testo", instance.testo)
        instance.save()
        return instance
