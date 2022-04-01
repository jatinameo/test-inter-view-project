from rest_framework import serializers, viewsets

from programs import models


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Program
        fields = ("id", "name", "currency", "return_percentage", "bank")


class ProgramViewSet(viewsets.ModelViewSet,):
    queryset = models.Program.objects.all()
    serializer_class = ProgramSerializer
