from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=150)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=150)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_model', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Actor(models.Model):
    """Актеры и режисеры"""
    name = models.CharField('Имя', max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0, blank=True)
    description = models.TextField('Описание')
    image = models.ImageField("Изображение", upload_to='actors/', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актеры и режиссеры'
        verbose_name_plural = 'Актеры и режиссеры'
        ordering = ('name', )

class Genre(models.Model):
    """Жанры"""
    name = models.CharField('Имя', max_length=100)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=100, unique=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ('name',)




class Movie(models.Model):
    """Аниме"""
    title = models.CharField('Название', max_length=150)
    name = models.CharField('Оригинальное название', max_length=150, default=' ')
    description = models.TextField('Описание')
    poster = models.ImageField('Постер', upload_to='movies/')
    year = models.PositiveSmallIntegerField('Дата выхода', default=2020)
    directors = models.ManyToManyField(Actor, verbose_name='режиссер', related_name='film_director')
    genres = models.ManyToManyField(Genre, verbose_name='жанры')
    category = models.ForeignKey(Category, verbose_name='категория', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField('Черновик', default=False)
    """Счетчик просмотров новости(не обязательный)"""
    views = models.IntegerField(default=0)
    ongoing = models.BooleanField('Слайдер', default=False)
    time = models.DateTimeField(default=datetime.now)
    favor = models.ManyToManyField(User, related_name='favor', blank=True)
    likes = models.ManyToManyField(User, related_name='blog_posts', blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('anime_main', kwargs={"slug": self.url})

    def get_comment(self):
        return self.comment_set.filter(reply=None).order_by('-id')

    def total_likes(self):
        return self.likes.count()

    class Meta:
        verbose_name = 'Аниме'
        verbose_name_plural = 'Аниме'



class MovieShots(models.Model):
    """Скриншоты"""
    title = models.CharField('Заголовок', max_length=100)
    description = models.TextField('Описание', blank=True)
    image = models.ImageField('Изображение', upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Скриншот'
        verbose_name_plural = 'Скриншоты'





class Serias(models.Model):
    """Серии"""
    name = models.CharField('Название', max_length=150)
    description = models.TextField('Кинопоиск', blank=True)
    dataplayer = models.CharField('Iframe', max_length=250, blank=True)
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Серия'
        verbose_name_plural = "Серии"


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    avatar = models.ImageField("Аватарка", null=True, upload_to="user_avatars/", blank=True, default='user_avatars/1.jpg')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class Comment(models.Model):
    post = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.ForeignKey('Comment', null=True, related_name="replies", on_delete=models.CASCADE, blank=True)
    content = models.TextField('Комментарий:', max_length=500)
    time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.post.title

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

