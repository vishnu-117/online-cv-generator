from django.urls import path
from .views import accept, resume, allresume

urlpatterns = [
    path("", accept, name="home"),
    path("<int:id>/", resume, name="resume"),
    path("resume/", allresume, name="allresume"),
]
