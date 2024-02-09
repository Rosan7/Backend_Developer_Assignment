from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email,name,dob, password=None, **extra_fields):
        if not email:
            raise ValueError("Email Number is required")
        email = self.normalize_email(email)
        user = self.model(email=email,name=name,dob=dob,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name,dob,password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email,name,dob, password, **extra_fields)
