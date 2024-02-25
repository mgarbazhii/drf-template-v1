from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError


@receiver(pre_save, sender=User)
def validate_user_email(sender, instance, **kwargs):
    if not instance.email:
        raise ValidationError(
            "Вы не указали email. Это поле обязательно для заполнения.")

    # Проверка уникальности email
    if User.objects.filter(email=instance.email).exclude(pk=instance.pk).exists():
        raise ValidationError("Пользователь с таким email уже существует.")
