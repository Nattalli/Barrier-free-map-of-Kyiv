from django.db import models


class Addition(models.Model):
    title = models.CharField(max_length=127)

    def __str__(self) -> str:
        return self.title


class MapPointCategory(models.Model):
    title = models.CharField(max_length=127)

    class Meta:
        verbose_name = 'Map Point Categories'

    def __str__(self) -> str:
        return self.title


class MapPoint(models.Model):
    title = models.CharField(max_length=127)
    comment = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255, default='Unknown')
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)
    source = models.CharField(max_length=255, blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    addition = models.ManyToManyField(Addition, blank=True)
    schedule = models.CharField(max_length=127, blank=True, null=True)
    category = models.ForeignKey(MapPointCategory, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.title} at {self.address}"
