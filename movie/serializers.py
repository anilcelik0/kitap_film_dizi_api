from.models import movies
from rest_framework import serializers

class User_Modal(serializers.ModelSerializer):
    class Meta:
        model = movies
        fields = "__all__"
