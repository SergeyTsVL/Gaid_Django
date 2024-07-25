from django.db import models
from django.utils import timezone   #Часовые пояса
from django.contrib.auth.models import User  #Аутентификация пользователя

# Делаем каждый раз когда изменяем этот файл
# python manage.py makemigrations blog
# python manage.py sqlmigrate blog 0001
# python manage.py migrate

# python manage.py createsuperuser
# cd mysite

# Username (leave blank to use 'tsars'): Sergey
# Email address: tsarskiytsarskiy@mail.ru
# Password:
# Password (again):
# Error: Your passwords didn't match.
# Password: 123
# Password (again): 123

# python manage.py runserver

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250) #заголовок статьи
    slug = models.SlugField(max_length=250, unique_for_date='publish')  #URL статьи использующая
    # уникальную дату публикации
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post') #внешний ключ один ко многим
    body = models.TimeField() #содержанеи статьи
    publish = models.DateField(default=timezone.now) #дата публикации статьи
    created = models.DateTimeField(auto_now_add=True)  #дата создания статьи
    updated = models.DateTimeField(auto_now=True)  #дата и период когда статья была откорректирована
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')  #сстатус статьи
    class Meta: # метаданные в порядке убывания (префикс - )
        ordering = ('-publish',)
        def __str__(self):
            return self.title #возвращает отображение понятное для человека





