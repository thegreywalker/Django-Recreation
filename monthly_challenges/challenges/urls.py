from django.urls import path
from . import views

urlpatterns = [
    path("<int:month>", views.month_challenge_by_number, name="Monthly Challange ny Number"),
    path("<str:month>", views.monthly_challenge, name="Monthly Challenge"),
]