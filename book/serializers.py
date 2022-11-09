from.models import books
from rest_framework import serializers

class User_Modal(serializers.ModelSerializer):
    class Meta:
        model = books
        fields = "__all__"
