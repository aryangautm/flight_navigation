# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
# ]

from django.urls import path
from .views import home, RoutePlanningView

urlpatterns = [
    path('', home, name='home'),
    path('route-planning/', RoutePlanningView.as_view(), name='route_planning'),
]
