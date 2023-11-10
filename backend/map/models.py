from django.db import models


class StreetType(models.TextChoices):
    AVENUE = 'AVENUE', 'Avenue'
    STREET = 'STREET', 'Street'
    BYSTREET = 'BYSTREET', 'Bystreet'


class Street(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=StreetType.choices)
    sidewalks = models.ManyToManyField('SidewalkMap', related_name='streets')
    central_walks = models.ManyToManyField('Sidewalk', related_name='central_streets')
    start_with_names = models.ManyToManyField('AdjacentStreet', related_name='starting_streets')
    end_with_names = models.ManyToManyField('AdjacentStreet', related_name='ending_streets')


class AdjacentStreet(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=10, choices=StreetType.choices)


class Sidewalk(models.Model):
    issues = models.ManyToManyField('SidewalkIssue', related_name='sidewalks')
    crosswalks = models.ManyToManyField('Crosswalk', related_name='sidewalks')
    width_in_centimeters = models.IntegerField()
    commit_issues = models.ManyToManyField('CommitIssue', related_name='sidewalks')


class SidewalkMap(models.Model):
    left = models.ManyToManyField(Sidewalk, related_name='left_maps')
    right = models.ManyToManyField(Sidewalk, related_name='right_maps')


class IssueStatusType(models.TextChoices):
    PROCESSED = 'PROCESSED', 'Processed'
    INPROCESSING = 'INPROCESSING', 'Inprocessing'
    NEW = 'NEW', 'New'


class CommitIssue(models.Model):
    username = models.CharField(max_length=63)
    user_email = models.EmailField()
    status = models.CharField(max_length=15, choices=IssueStatusType.choices)
    date = models.DateTimeField()
    issue = models.TextField()


class SidewalkIssue(models.Model):
    borders = models.ManyToManyField('SidewalkIssueBorder', related_name='issues')


class SidewalkIssueBorder(models.Model):
    height_in_centimeters = models.IntegerField()
    GPS = models.CharField(max_length=255)
    commit_issues = models.ManyToManyField(CommitIssue, related_name='borders')


class CrosswalkType(models.TextChoices):
    UNDERGROUND = 'UNDERGROUND', 'Underground'
    OVERGROUND = 'OVERGROUND', 'Overground'
    BY_ROAD = 'BY_ROAD', 'By Road'


class Crosswalk(models.Model):
    type = models.CharField(max_length=15, choices=CrosswalkType.choices)
    issues = models.ManyToManyField('CrosswalkIssue', related_name='crosswalks')
    benefits = models.ManyToManyField('CrosswalkBenefit', related_name='crosswalks')
    GPS = models.CharField(max_length=255)
    width_in_centimeters = models.IntegerField()
    direction = models.ForeignKey('CrosswalkDirection', on_delete=models.CASCADE)
    commit_issues = models.ManyToManyField(CommitIssue, related_name='crosswalks')


class CrosswalkIssue(models.Model):
    border_height_in_centimeters = models.IntegerField()
    commit_issues = models.ManyToManyField(CommitIssue, related_name='crosswalk_issues')


class CrosswalkBenefitType(models.TextChoices):
    LIFT = 'LIFT', 'Lift'
    SPECIAL_LIFT = 'SPECIAL_LIFT', 'Special Lift'
    SOCIAL_WORKER = 'SOCIAL_WORKER', 'Social Worker'


class CrosswalkBenefit(models.Model):
    type = models.CharField(max_length=15, choices=CrosswalkBenefitType.choices)
    commit_issues = models.ManyToManyField(CommitIssue, related_name='benefits')


class CrosswalkDirectionType(models.TextChoices):
    LEFT = 'LEFT', 'Left'
    RIGHT = 'RIGHT', 'Right'
    TOP = 'TOP', 'Top'
    BOTTOM = 'BOTTOM', 'Bottom'


class CrosswalkDirection(models.Model):
    direction = models.CharField(max_length=10, choices=CrosswalkDirectionType.choices)
    type = models.CharField(max_length=10, choices=StreetType.choices)
    name = models.CharField(max_length=255)
