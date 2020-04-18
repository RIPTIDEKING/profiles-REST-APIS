from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, moNo, password=None):
        """create user"""
        if not email:
            raise ValueError('User mush have a email')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, moNo=moNo)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, moNo, password):
        """Create Super User"""

        user = create_user(email, name, moNo, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """User Database Model"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    moNo = models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return (self.email+self.name)
