from django.urls import path
from . import views
urlpatterns =[
    path("",views.home , name="home"),
      path("Dcandidate",views.Dcandidate , name="Dcandidate"),
       path("Rcandidate",views.Rcandidate , name="Rcandidate"),
       path("Rvoter", views.Rvoter, name="Rvoter")
]