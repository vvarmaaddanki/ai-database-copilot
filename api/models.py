from django.db import models

# Create your models here.
class DatabaseConnection(models.Model):
    name = models.CharField(max_length=100)
    host = models.CharField(max_length=255)
    port = models.IntegerField(default=5432)
    database_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name
