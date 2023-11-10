from django.urls import path
from .views import MapPointList, MapPointCreate


urlpatterns = [
    path('', MapPointList.as_view(), name='points-list'),
    path('create/', MapPointCreate.as_view(), name='point-create'),
]
