from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="home"),
    path("login/", views.login, name="login"),
    path('logout/', views.logout, name='logout'),
    path("", include("dashboard.urls")),
]


