from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('reg/',views.regis),
    path('success/',views.suc)
]