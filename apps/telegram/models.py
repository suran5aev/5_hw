from django.db import models
from apps.telegram.forms import TIME_CHOISE, PERSONE_CHOISE

# Create your models here.

class Telegram(models.Model):
    phone = models.CharField(
        max_length=50,
        verbose_name="Номер телефона"
    )
    persone = models.CharField(
        max_length=20,
        choices=PERSONE_CHOISE,
        verbose_name="Количество людей"
    )
    date = models.DateField(
        verbose_name="Дата"
    )
    time = models.CharField(
        max_length=20,
        choices=TIME_CHOISE,
        verbose_name="Время"
    )
    
    def __str__(self) -> str:
        return f"{self.phone} - {self.persone} - {self.date} - {self.time}"
    
    class Meta:
        verbose_name = "Резервация"
        verbose_name_plural = "Резервации"
        
        
        
class TelegramUser(models.Model):
    id_user = models.CharField(
        max_length=100,
        verbose_name="ID пользователя telegram"
    )
    username = models.CharField(
        max_length=255,
        verbose_name="Имя пользователя",
        blank=True, null=True
    )
    first_name = models.CharField(
        max_length=255,
        verbose_name="Имя",
        blank=True, null=True
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name="Фамилия",
        blank=True, null=True
    )
    chat_id = models.CharField(
        max_length=100,
        verbose_name="Чат ID"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата регистрации"
    )

    def __str__(self):
        return str(self.username)
    
    class Meta:
        verbose_name = "Пользователь телеграм"
        verbose_name_plural = "Пользователи телеграма"