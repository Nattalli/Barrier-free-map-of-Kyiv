from django.db import models
from django.utils.translation import gettext_lazy as _


class Addition(models.Model):
    title = models.CharField(_("Назва"), max_length=127)

    class Meta:
        verbose_name = _("Особливість")
        verbose_name_plural = _("Особливості")

    def __str__(self) -> str:
        return self.title


class MapPointCategory(models.Model):
    title = models.CharField(_("Назва"), max_length=255)

    class Meta:
        verbose_name = _("Категорія точки на мапі")
        verbose_name_plural = _("Категорії точок на мапі")

    def __str__(self) -> str:
        return self.title


class MapPoint(models.Model):
    title = models.CharField(_("Назва"), max_length=255)
    comment = models.TextField(_("Коментар"), blank=True, null=True)
    address = models.CharField(_("Адреса"), max_length=255, default=_('Невідомо'))
    longitude = models.FloatField(_("Довгота"), default=0.0)
    latitude = models.FloatField(_("Широта"), default=0.0)
    source = models.CharField(_("Джерело"), max_length=255, blank=True, null=True)
    is_approved = models.BooleanField(_("Затверджено"), default=False)
    addition = models.ManyToManyField(Addition, verbose_name=_("Особливості"), blank=True)
    schedule = models.CharField(_("Розклад"), max_length=127, blank=True, null=True)
    category = models.ForeignKey(MapPointCategory, verbose_name=_("Категорія"), on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = _("Точка на мапі")
        verbose_name_plural = _("Точки на мапі")

    def __str__(self) -> str:
        return f"{self.title} за адресою {self.address}"
