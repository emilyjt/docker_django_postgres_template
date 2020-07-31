from django.urls import path

from .views import (
    MyLoginView,
    MyLogoutView,
    MyPasswordChangeDoneView,
    MyPasswordChangeView,
    MyPasswordResetCompleteView,
    MyPasswordResetConfirmView,
    MyPasswordResetDoneView,
    MyPasswordResetView,
    MyRegisterView,
)

# The app_name below creates a namespace. This allows us to refrence urls
# as 'account:login', etc. See here for more details:
# https://docs.djangoproject.com/en/3.0/topics/http/urls/#url-namespaces
app_name = "account"
urlpatterns = [
    # These are copied and pasted from `django.contrib.auth.urls`
    # alternative implementation could have been:
    # `path("", include("django.contrib.auth.urls")),`
    # see the official docs for me, here:
    # https://docs.djangoproject.com/en/dev/topics/auth/default/#module-django.contrib.auth.views
    # To find out why this default implementations are not been used,
    # see `views.py`
    path("register/", MyRegisterView.as_view(), name="register"),
    path("login/", MyLoginView.as_view(), name="login"),
    path("logout/", MyLogoutView.as_view(), name="logout"),
    # password change
    path("password_change/", MyPasswordChangeView.as_view(), name="password_change"),
    path(
        "password_change/done/",
        MyPasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    # password reset
    path("password_reset/", MyPasswordResetView.as_view(), name="password_reset"),
    path(
        "password_reset/done/",
        MyPasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        MyPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        MyPasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
