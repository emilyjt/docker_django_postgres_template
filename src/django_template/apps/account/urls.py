from django.urls import path, include

# https://docs.djangoproject.com/en/dev/topics/auth/default/#module-django.contrib.auth.views

app_name = "account"
urlpatterns = [
    path("", include("django.contrib.auth.urls")),
]

# This is a list of the included urls
# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']
