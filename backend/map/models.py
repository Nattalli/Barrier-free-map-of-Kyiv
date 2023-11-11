from django.db import models
from django.utils.translation import gettext_lazy as _


class StreetType(models.TextChoices):
    AVENUE = 'AVENUE', _('Проспект')
    STREET = 'STREET', _('Вулиця')
    BYSTREET = 'BYSTREET', _('Бічна вулиця')


class Street(models.Model):
    id = models.CharField(_("ID"), max_length=100, primary_key=True)
    name = models.CharField(_("Назва"), max_length=255)
    type = models.CharField(_("Тип"), max_length=10, choices=StreetType.choices)
    sidewalks = models.ManyToManyField('SidewalkMap', related_name='streets', verbose_name=_("Тротуари"))
    central_walks = models.ManyToManyField('Sidewalk', related_name='central_streets', verbose_name=_("Центральні тротуари"))
    start_with_names = models.ManyToManyField('AdjacentStreet', related_name='starting_streets', verbose_name=_("Початкові вулиці"))
    end_with_names = models.ManyToManyField('AdjacentStreet', related_name='ending_streets', verbose_name=_("Кінцеві вулиці"))

    class Meta:
        verbose_name = _("Вулиця")
        verbose_name_plural = _("Вулиці")


class AdjacentStreet(models.Model):
    name = models.CharField(_("Назва"), max_length=255)
    type = models.CharField(_("Тип"), max_length=10, choices=StreetType.choices)
    id = models.CharField(_("ID"), max_length=100, primary_key=True)

    class Meta:
        verbose_name = _("Прилегла вулиця")
        verbose_name_plural = _("Прилеглі вулиці")


class Sidewalk(models.Model):
    id = models.CharField(_("ID"), max_length=100, primary_key=True)
    issues = models.ManyToManyField('SidewalkIssue', related_name='sidewalks', verbose_name=_("Проблеми"))
    crosswalks = models.ManyToManyField('Crosswalk', related_name='sidewalks', verbose_name=_("Пішохідні переходи"))
    width_in_centimeters = models.IntegerField(_("Ширина в сантиметрах"))
    commit_issues = models.ManyToManyField('CommitIssue', related_name='sidewalks', verbose_name=_("Зафіксовані проблеми"))

    class Meta:
        verbose_name = _("Тротуар")
        verbose_name_plural = _("Тротуари")


class SidewalkMap(models.Model):
    left = models.ManyToManyField(Sidewalk, related_name='left_maps', verbose_name=_("Лівий"))
    right = models.ManyToManyField(Sidewalk, related_name='right_maps', verbose_name=_("Правий"))

    class Meta:
        verbose_name = _("Карта тротуарів")
        verbose_name_plural = _("Карти тротуарів")


class IssueStatusType(models.TextChoices):
    PROCESSED = 'PROCESSED', _('Оброблено')
    INPROCESSING = 'INPROCESSING', _('В обробці')
    NEW = 'NEW', _('Новий')


class CommitIssue(models.Model):
    username = models.CharField(_("Ім'я користувача"), max_length=63)
    user_email = models.EmailField(_("Електронна пошта користувача"))
    status = models.CharField(_("Статус"), max_length=15, choices=IssueStatusType.choices)
    date = models.DateTimeField(_("Дата"), auto_now=True)
    issue = models.TextField(_("Проблема"))

    class Meta:
        verbose_name = _("Зафіксована проблема")
        verbose_name_plural = _("Зафіксовані проблеми")


class SidewalkIssue(models.Model):
    borders = models.ManyToManyField('SidewalkIssueBorder', related_name='issues', verbose_name=_("Кордони"))

    class Meta:
        verbose_name = _("Проблема тротуару")
        verbose_name_plural = _("Проблеми тротуарів")


class SidewalkIssueBorder(models.Model):
    height_in_centimeters = models.IntegerField(_("Висота в сантиметрах"))
    GPS = models.CharField(_("GPS"), max_length=255)
    commit_issues = models.ManyToManyField(CommitIssue, related_name='borders', verbose_name=_("Зафіксовані проблеми"))

    class Meta:
        verbose_name = _("Проблема кордону тротуару")
        verbose_name_plural = _("Проблеми кордонів тротуарів")


class CrosswalkType(models.TextChoices):
    UNDERGROUND = 'UNDERGROUND', _('Підземний')
    OVERGROUND = 'OVERGROUND', _('Надземний')
    BY_ROAD = 'BY_ROAD', _('Біля дороги')


class Crosswalk(models.Model):
    type = models.CharField(_("Тип"), max_length=15, choices=CrosswalkType.choices)
    issues = models.ManyToManyField('CrosswalkIssue', related_name='crosswalks', verbose_name=_("Проблеми"))
    benefits = models.ManyToManyField('CrosswalkBenefit', related_name='crosswalks', verbose_name=_("Переваги"))
    GPS = models.CharField(_("GPS"), max_length=255)
    width_in_centimeters = models.IntegerField(_("Ширина в сантиметрах"))
    direction = models.ForeignKey('CrosswalkDirection', on_delete=models.CASCADE, verbose_name=_("Напрямок"))
    commit_issues = models.ManyToManyField(CommitIssue, related_name='crosswalks', verbose_name=_("Зафіксовані проблеми"))

    class Meta:
        verbose_name = _("Пішохідний перехід")
        verbose_name_plural = _("Пішохідні переходи")


class CrosswalkIssue(models.Model):
    border_height_in_centimeters = models.IntegerField(_("Висота кордону в сантиметрах"))
    commit_issues = models.ManyToManyField(CommitIssue, related_name='crosswalk_issues', verbose_name=_("Зафіксовані проблеми"))

    class Meta:
        verbose_name = _("Проблема пішохідного переходу")
        verbose_name_plural = _("Проблеми пішохідних переходів")


class CrosswalkBenefitType(models.TextChoices):
    LIFT = 'LIFT', _('Ліфт')
    SPECIAL_LIFT = 'SPECIAL_LIFT', _('Спеціальний ліфт')
    SOCIAL_WORKER = 'SOCIAL_WORKER', _('Соціальний працівник')


class CrosswalkBenefit(models.Model):
    type = models.CharField(_("Тип"), max_length=15, choices=CrosswalkBenefitType.choices)
    commit_issues = models.ManyToManyField(CommitIssue, related_name='benefits', verbose_name=_("Зафіксовані проблеми"))

    class Meta:
        verbose_name = _("Перевага пішохідного переходу")
        verbose_name_plural = _("Переваги пішохідних переходів")


class CrosswalkDirectionType(models.TextChoices):
    LEFT = 'LEFT', _('Ліворуч')
    RIGHT = 'RIGHT', _('Праворуч')
    TOP = 'TOP', _('Вгору')
    BOTTOM = 'BOTTOM', _('Вниз')


class CrosswalkDirection(models.Model):
    direction = models.CharField(_("Напрямок"), max_length=10, choices=CrosswalkDirectionType.choices)
    type = models.CharField(_("Тип"), max_length=10, choices=StreetType.choices)
    name = models.CharField(_("Назва"), max_length=255)
    id = models.CharField(_("ID"), max_length=100, primary_key=True)

    class Meta:
        verbose_name = _("Напрямок пішохідного переходу")
        verbose_name_plural = _("Напрямки пішохідних переходів")
