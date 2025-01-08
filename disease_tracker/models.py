from django.db import models

class Disease(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    is_usa = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.location}"