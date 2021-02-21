from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project

    Quote:
        If you’re starting a new project, it’s highly recommended to set up a custom user model,
        even if the default User model is sufficient for you. This model behaves identically to
        the default user model, but you’ll be able to customize it in the future if the need arises.
    """

    pass
