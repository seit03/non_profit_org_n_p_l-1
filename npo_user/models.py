# from django.contrib.auth.base_user import AbstractBaseUser
# from django.contrib.auth.models import PermissionsMixin, UserManager
# from django.db import models
#
#
# ADMIN = 1
# CLIENT = 2
# USER_TYPE = (
#     (ADMIN, 'ADMIN'),
#     (CLIENT, 'CLIENT'),
# )
#
#
# class NPOUser(AbstractBaseUser, PermissionsMixin):
#
#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователь'
#
#     user_type = models.IntegerField(choices=USER_TYPE,
#                                     verbose_name='Тип пользовотеля',
#                                     default=CLIENT)
#
#     user_name = models.CharField('user_name', unique=True, max_length=100)
#     email = models.EmailField('email', null=True, max_length=100)
#     first_name = models.CharField('first_name', max_length=30, blank=True)
#     last_name = models.CharField('last_name', max_length=30, blank=True)
#     data_joined = models.DateTimeField('data_joined', auto_now_add=True)
#     is_active = models.DateTimeField('is_active', default=True)
#     is_staff = models.DateTimeField(default=True)
#     objects = UserManager()
#
#     USERNAME_FIELD = 'user_name'
#     REQUIRED_FIELDS = ['email']