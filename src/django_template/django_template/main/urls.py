from django.urls import path

from .views import HomePageView

# The app_name below creates a namespace. This allows us to refrence urls
# as 'main:home', etc. See here for more details:
# https://docs.djangoproject.com/en/3.0/topics/http/urls/#url-namespaces
app_name = "main"
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]
