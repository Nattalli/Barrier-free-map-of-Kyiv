from rest_framework import generics
from .models import *
from .serializers import *


class StreetListCreateView(generics.ListCreateAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer


class StreetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer


class AdjacentStreetListCreateView(generics.ListCreateAPIView):
    queryset = AdjacentStreet.objects.all()
    serializer_class = AdjacentStreetSerializer


class AdjacentStreetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AdjacentStreet.objects.all()
    serializer_class = AdjacentStreetSerializer


class SidewalkListCreateView(generics.ListCreateAPIView):
    queryset = Sidewalk.objects.all()
    serializer_class = SidewalkSerializer


class SidewalkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sidewalk.objects.all()
    serializer_class = SidewalkSerializer


class SidewalkMapListCreateView(generics.ListCreateAPIView):
    queryset = SidewalkMap.objects.all()
    serializer_class = SidewalkMapSerializer


class SidewalkMapDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SidewalkMap.objects.all()
    serializer_class = SidewalkMapSerializer


class CommitIssueListCreateView(generics.ListCreateAPIView):
    queryset = CommitIssue.objects.all()
    serializer_class = CommitIssueSerializer


class CommitIssueDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommitIssue.objects.all()
    serializer_class = CommitIssueSerializer


class SidewalkIssueListCreateView(generics.ListCreateAPIView):
    queryset = SidewalkIssue.objects.all()
    serializer_class = SidewalkIssueSerializer


class SidewalkIssueDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SidewalkIssue.objects.all()
    serializer_class = SidewalkIssueSerializer


class SidewalkIssueBorderListCreateView(generics.ListCreateAPIView):
    queryset = SidewalkIssueBorder.objects.all()
    serializer_class = SidewalkIssueBorderSerializer


class SidewalkIssueBorderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SidewalkIssueBorder.objects.all()
    serializer_class = SidewalkIssueBorderSerializer


class CrosswalkListCreateView(generics.ListCreateAPIView):
    queryset = Crosswalk.objects.all()
    serializer_class = CrosswalkSerializer


class CrosswalkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Crosswalk.objects.all()
    serializer_class = CrosswalkSerializer


class CrosswalkIssueListCreateView(generics.ListCreateAPIView):
    queryset = CrosswalkIssue.objects.all()
    serializer_class = CrosswalkIssueSerializer


class CrosswalkIssueDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CrosswalkIssue.objects.all()
    serializer_class = CrosswalkIssueSerializer


class CrosswalkBenefitListCreateView(generics.ListCreateAPIView):
    queryset = CrosswalkBenefit.objects.all()
    serializer_class = CrosswalkBenefitSerializer


class CrosswalkBenefitDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CrosswalkBenefit.objects.all()
    serializer_class = CrosswalkBenefitSerializer


class CrosswalkDirectionListCreateView(generics.ListCreateAPIView):
    queryset = CrosswalkDirection.objects.all()
    serializer_class = CrosswalkDirectionSerializer


class CrosswalkDirectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CrosswalkDirection.objects.all()
    serializer_class = CrosswalkDirectionSerializer
