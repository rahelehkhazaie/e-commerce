from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, phone, username, password=None):
        """
        Creates and saves a User with the given phone number and password.
        """
        if not phone:
            raise ValueError("Users must have an phone number")

        user = self.model(
            phone=phone,
            username=username
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, username, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            phone,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        null=True,
        blank=True,
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=50, unique=True, verbose_name="username")
    phone = models.CharField(max_length=12, unique=True, verbose_name="phone number")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    
class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    fullname = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    email = models.EmailField(blank=True, null=True)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=400)
    zip_code = models.CharField(max_length=30)
    
    def __str__(self):
        return self.user.phone
    
    
class Otp(models.Model):
    token = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=11)
    code = models.SmallIntegerField()
    expiration_date = models.DateTimeField(auto_now_add=True)   
    

class Contact(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=500)
   