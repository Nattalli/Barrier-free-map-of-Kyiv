from django.db import models


class Addition(models.Model):
    title = models.CharField(max_length=127)

    def __str__(self) -> str:
        return self.title


class MapPoint(models.Model):
    title = models.CharField(max_length=127)
    comment = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255)
    longitude = models.FloatField()
    latitude = models.FloatField()
    source = models.CharField(max_length=255, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    addition = models.ManyToManyField(Addition, blank=True)

    def __str__(self) -> str:
        return f"{self.title} at {self.address}"
