from rest_framework import serializers
from .models import DatabaseConnection


class DatabaseConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatabaseConnection
        fields = ["id", "name", "host", "port", "database_name", "username", "created_at"]