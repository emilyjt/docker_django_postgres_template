from django.urls import path

from . import views

# The app_name below creates a namespace. This allows us to refrence urls
# as 'core:home', etc. See here for more details:
# https://docs.djangoproject.com/en/3.0/topics/http/urls/#url-namespaces
app_name = "core"
urlpatterns = [
    path("", views.home, name="home"),
]
