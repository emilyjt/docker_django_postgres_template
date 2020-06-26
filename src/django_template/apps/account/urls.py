from django.urls import include, path

from .views import RegisterView

# https://docs.djangoproject.com/en/dev/topics/auth/default/#module-django.contrib.auth.views

app_name = "account"
urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("", include("django.contrib.auth.urls")),
]

# This is a list of the included urls
# account/login/ [name='login']
# account/logout/ [name='logout']
# account/password_change/ [name='password_change']
# account/password_change/done/ [name='password_change_done']
# account/password_reset/ [name='password_reset']
# account/password_reset/done/ [name='password_reset_done']
# account/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# account/reset/done/ [name='password_reset_complete']
