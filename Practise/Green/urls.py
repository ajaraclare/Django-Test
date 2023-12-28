from django.urls import path, include
from.import views

urlpatterns = [
    path('', views.leaf, name="leaf"),
    path('warm/', include("Sunny.urls"))
]