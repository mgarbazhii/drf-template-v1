from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Community(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, through="Membership")
    description = models.TextField(blank=True, null=True)
    community_admin = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='community_admin', verbose_name='Администратор сообщества')

    class Meta:
        verbose_name = 'Сообщество'
        verbose_name_plural = 'Сообщества'

    @property
    def members_count(self):
        return self.members.count()


class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    date_joined = models.DateField(blank=True, null=True)
    invite_reason = models.CharField(max_length=64, blank=True, null=True)


class Profile(models.Model):
    user = models.OneToOneField(
        User, models.CASCADE, related_name='user_profile',
        verbose_name='Пользователь', primary_key=True,
    )
    phone_number = models.IntegerField(blank=True, null=True)
    telegram_id = models.CharField(max_length=100, blank=True)
    card_number = models.IntegerField(blank=False, null=False)
    is_suspend = models.BooleanField(default=False)
    comments = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
