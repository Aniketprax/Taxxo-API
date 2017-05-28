from rest_framework import serializers
from ledgers.models import Ledgers


class Ledgersserializers(serializers.ModelSerializer):
    class Meta:
        model = Ledgers
        fields = ('id','company','name','primary_group','secondary_group','tertiary_group','opening_balance','date','credit_amount','debit_amount','added_by')
