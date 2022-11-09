from.models import seriess
from rest_framework import serializers

class User_Modal(serializers.ModelSerializer):
    class Meta:
        model = seriess
        fields = "__all__"
