from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

urlpatterns = [
    path("register",views.register,name="register"),
    path("login",views.LoginView.as_view(),name="login"),
]
urlpatterns+= router.urls
