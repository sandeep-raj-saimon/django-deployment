from django.urls import path

from . import views
urlpatterns = [
    path('',views.index),
    path('createuser/',views.createUser),
    path("getAll/",views.getAll)
]