from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, nickname, password=None, phone=None,
                    date_of_birth=None, avatar=None, role=None, **extra_fields):
        """
        Создаёт и сохраняет пользователя с указанным email, nickname и паролем.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not nickname:
            raise ValueError('Users must have a nickname')

        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)

        user = self.model(
            email=email,
            nickname=nickname,
            phone=phone,
            date_of_birth=date_of_birth,
            avatar=avatar,
            role=role,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password=None, **extra_fields):
        """
        Создаёт и сохраняет суперпользователя.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, nickname, password, **extra_fields, role='Admin')

    def create_doctor(self, email, nickname, password=None, **extra_fields):
        """
        Создаёт и сохраняет пользователя с ролью 'Doctor'.
        """
        extra_fields.setdefault('is_staff', True)
        return self.create_user(email, nickname, password, role='Doctor', **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    DoesNotExist = None
    ROLE_CHOICES = [
        # ('Admin', 'Администратор'),
        ('Doctor', 'Доктор'),
        ('User', 'Пользователь'),
    ]

    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    nickname = models.CharField(max_length=30, unique=True, verbose_name='Никнейм')
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Телефон')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    avatar = models.ImageField(upload_to='users_avatar/', blank=True, null=True, verbose_name='Аватар пользователя')

    first_name = models.CharField(max_length=30, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=30, blank=True, verbose_name='Фамилия')
    date_joined = models.DateTimeField(default=timezone.now, verbose_name='Дата регистрации')

    speciality = models.CharField(max_length=255, blank=True, null=True, verbose_name='Специализация')  # Для докторов
    description = models.TextField(blank=True, null=True, verbose_name='Описание')  # Описание доктора
    experience = models.PositiveIntegerField(blank=True, null=True, verbose_name='Опыт (в годах)')  # Для докторов
    education = models.TextField(blank=True, null=True, verbose_name='Образование')

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='User', verbose_name='Роль')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    is_staff = models.BooleanField(default=False, verbose_name='Сотрудник')
    is_superuser = models.BooleanField(default=False, verbose_name='Суперпользователь')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.nickname} ({self.email})"

    def has_perm(self, perm, obj=None):
        return self.is_superuser or self.has_module_perms(perm)

    def has_module_perms(self, app_label):
        return self.is_superuser

    def get_user_permissions(self, obj=None):
        return []

    def get_group_permissions(self, obj=None):
        return []


class Profile(models.Model):
    pass
