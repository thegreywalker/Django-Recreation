from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("<int:month>", views.month_challenge_by_number, name="Monthly Challange_by_Number"),
    path("<str:month>", views.monthly_challenge, name="Monthly_Challenge"),
]