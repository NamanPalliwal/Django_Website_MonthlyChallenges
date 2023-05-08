from django.urls import path
from . import views

urlpatterns = [
         path("<int:month>", views.monthly_challenges_by_number),
         
         # Give unique name to path with <name> arg
         path("<str:month>", views.monthly_challenges, name = 'month-challenge'),  
         
         path("", views.index)          # /challenges/  -  default path
]