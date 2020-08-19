from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.MoviesView.as_view()),
    path('filter/', views.FilterMoviesView.as_view(), name='filter'),
    path('search/', views.Search.as_view(), name='search'),
    path('genre/', views.FilterGenre.as_view(), name='genre'),
    path('slider/', views.Slider.as_view(), name='slider'),
    path('category/', views.FilterCategory.as_view(), name='category'),
    path('random/', views.RandomAnime.as_view(), name='random'),
    re_path('(?P<id>\d+)/favorite/$', views.favourite_post, name='favourite'),
    path('favorites/', views.favourite_list, name='favourite_list'),
    path('like_posts/', views.like_list, name='like_list'),
    path('accounts/profile/', views.accountSettings, name='profile'),
    path('last_update/', views.LastUpdate.as_view(), name='last_update'),
    path("<slug:slug>/", views.MovieDetailView.as_view(), name='anime_main'),
    path('movies/<slug:slug>', views.CategoryModel.as_view(), name='category_model'),
    path('like/$', views.like_post, name='like_post'),
    ]
