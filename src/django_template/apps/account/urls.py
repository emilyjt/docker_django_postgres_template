from django.contrib.auth import views
from django.urls import include, path

from .views import MyLoginView, MyRegisterView

# The app_name below creates a namespace. This allows us to refrence urls
# as 'account:login', etc. See here for more details:
# https://docs.djangoproject.com/en/3.0/topics/http/urls/#url-namespaces
app_name = "account"
urlpatterns = [
    path("login/", MyLoginView.as_view(), name="login"),
    path("register/", MyRegisterView.as_view(), name="register"),
    # These are copied and pasted from `django.contrib.auth.urls`
    # alternative implementation could have been:
    # `path("", include("django.contrib.auth.urls")),`
    # see the official docs for me, here:
    # https://docs.djangoproject.com/en/dev/topics/auth/default/#module-django.contrib.auth.views
    # path('login/', views.LoginView.as_view(), name='login'),
    # To find out why this default implementation of `login/` has
    # been commented out, see `views.py`
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path(
        "password_change/", views.PasswordChangeView.as_view(), name="password_change"
    ),
    path(
        "password_change/done/",
        views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]

