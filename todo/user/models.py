from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    """
    Auth user model.
    """

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):

        """
        Return the first_name plus the last_name, with a space in between.
        """

        if self.first_name or self.last_name:
            full_name = '%s %s' % (self.first_name, self.last_name)
            return full_name.strip().capitalize()
        else:
            return self.email
