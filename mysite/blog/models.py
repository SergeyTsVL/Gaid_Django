from django.db import models
from django.utils import timezone   #Часовые пояса
from django.contrib.auth.models import User  #Аутентификация пользователя
from django.urls import reverse

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

# python manage.py shell

# >>> # from django.contrib.auth.models import User
# >>> # from blog.models import Post
# >>> # user = User.objects.get(username='admin')
# >>> # post = Post(title='Another post', slug='another-post', body='Post body.', author=user)
# >>> # post.save()

# >>> post = Post(title='Another post', slug='another-post', body='Post body.', author=user)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'user' is not defined. Did you mean: 'User'?
# >>> all_posts = Post.objects.all()
# >>> Post.objects.all()
# <QuerySet []>
# >>> Post.objects.filter(publish__year=2017, author__username='admin')
# <QuerySet []>
# >>> Post.objects.filter(publish__year=2023).exclude(title__startswith='Title')

# https://docs.djangoproject.com/en/2.0/ref/templates/ Список встроенных тегов и шаблонов теги и шаблоны

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

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
    objects = models.Manager() # менеджер по умолчанию
    published = PublishedManager()  # Наш новый менеджер

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year,
                                                 self.publish.month, self.publish.day, self.publish.slug])

    class Meta: # метаданные в порядке убывания (префикс - )
        ordering = ('-publish',)
        def __str__(self):
            return self.title #возвращает отображение понятное для человека

# Post.published.filter()



