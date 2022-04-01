from rest_framework import mixins, serializers, viewsets

from banks.models import *
from programs.models import *
from rest_framework.response import Response
from rest_framework import status

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ["id", "name", "countries"]


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class TransactionSerializer(serializers.Serializer):
    program = serializers.CharField()
    currency = serializers.CharField()
    country = serializers.CharField()
    bank = serializers.CharField()
    # is_eligible = serializers.BooleanField()

    def create(self, validated_data):
        # validated_data = {'program': 'test 2', 'currency': 'INR', 'country': ['India'], 'bank': 'PNB'}
        bank_name = validated_data.get("bank")
        country = validated_data.get("country")
        countries = country if isinstance(country, list) else eval(str(country))
        currency = validated_data.get("currency")
        program_name = validated_data.get("program")

        try:
            bank_obj = Bank.objects.filter(name=bank_name, countries=countries).last()
            if bank_obj:
                Program.objects.get(
                        name=program_name, 
                        currency=currency, 
                        bank=bank_obj
                    )
                return True
            else:
                return False
        except Program.DoesNotExist:
            return False

        # we will perfore code for add data in db here  

    def update(self, instance, validated_data):
        pass


class TransactionViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
):
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        data_status = serializer.create(serializer.data)
        result = serializer.data
        if data_status:
            result['is_eligible'] = True
            return Response(result, status.HTTP_201_CREATED)
        else:
            result['is_eligible'] = False
            return Response(result, status=status.HTTP_400_BAD_REQUEST)



